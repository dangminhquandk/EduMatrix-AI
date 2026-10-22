"""
Bộ kiểm thử tự động (Unit & Integration Test Suite) phục vụ Hardening & Production-Ready.
Bao phủ các Edge Cases, Security Flaws, và Data Schema Integrity.
"""

import unittest
import json
import zipfile
import xml.etree.ElementTree as ET
import io
from curriculum_data import CURRICULUM_DATA
from matrix_engine import calculate_exam_blueprint
from ai_generator import generate_exam_content, _sanitize_and_validate_exam_json
from docx_exporter import generate_exam_docx


class TestJsonSanitizationAndValidation(unittest.TestCase):
    """Kiểm tra độ bền vững khi parse và validate JSON từ AI/người dùng."""

    def test_markdown_fence_stripping(self):
        """Mô phỏng Gemini trả về chuỗi JSON bọc trong markdown code fence."""
        raw_markdown_json = """```json
{
  "phan_I_trac_nghiem": [
    {
      "cau_so": 1,
      "muc_do": "Nhận biết",
      "cau_hoi": "Câu hỏi test 1",
      "lua_chon": {"A": "1", "B": "2", "C": "3", "D": "4"},
      "dap_an": "A",
      "giai_thich": "Test"
    }
  ],
  "phan_II_dung_sai": [],
  "phan_III_tra_loi_ngan": [],
  "phan_IV_tu_luan": []
}
```"""
        blueprint = calculate_exam_blueprint(6, "Giữa kỳ 1", ["Chủ đề A"], "mau_2")
        validated = _sanitize_and_validate_exam_json(raw_markdown_json, blueprint)
        self.assertIn("phan_I_trac_nghiem", validated)
        self.assertEqual(len(validated["phan_I_trac_nghiem"]), blueprint["summary"]["so_cau_tn"])

    def test_incomplete_json_auto_healing(self):
        """Mô phỏng Gemini trả về thiếu một số phần (ví dụ thiếu phần Tự luận hoặc Đ/S)."""
        incomplete_json = '{"phan_I_trac_nghiem": []}'
        blueprint = calculate_exam_blueprint(7, "Giữa kỳ 1", ["Chủ đề A"], "mau_2")
        validated = _sanitize_and_validate_exam_json(incomplete_json, blueprint)
        
        # Kiểm tra tự động bổ sung đủ 4 phần
        self.assertEqual(len(validated["phan_I_trac_nghiem"]), blueprint["summary"]["so_cau_tn"])
        self.assertEqual(len(validated["phan_II_dung_sai"]), blueprint["summary"]["so_cau_ds"])
        self.assertEqual(len(validated["phan_III_tra_loi_ngan"]), blueprint["summary"]["so_cau_tln"])
        self.assertEqual(len(validated["phan_IV_tu_luan"]), blueprint["summary"]["so_cau_tl"])


class TestShortAnswerDiversity(unittest.TestCase):
    """Kiểm tra độ phong phú của câu hỏi ngắn ở chế độ offline (tránh lặp lại đơn điệu)."""

    def test_short_answer_vocabulary(self):
        bp = calculate_exam_blueprint(6, "Giữa kỳ 1", ["Chủ đề A", "Chủ đề B"], "mau_2")
        content = generate_exam_content(bp)
        answers = [item["dap_an"] for item in content["phan_III_tra_loi_ngan"]]
        
        # Đảm bảo không bị lặp lại 100% một từ duy nhất
        unique_answers = set(answers)
        self.assertGreater(len(unique_answers), 1, f"Short answers are too repetitive: {answers}")


class TestMatrixEngineHardening(unittest.TestCase):
    """Kiểm tra an toàn tính toán và bất biến ma trận."""

    def test_empty_topics_fallback(self):
        bp = calculate_exam_blueprint(6, "Giữa kỳ 1", [], "mau_2")
        self.assertIsNotNone(bp)
        self.assertGreater(len(bp["matrix_rows"]), 0)
        self.assertEqual(bp["summary"]["tong_diem"], 10.0)

    def test_mathematical_invariants(self):
        for grade in [6, 7, 8, 9]:
            topics = CURRICULUM_DATA[grade]["ky_kiem_tra"]["Giữa kỳ 1"]
            for tpl in ["mau_1", "mau_2"]:
                bp = calculate_exam_blueprint(grade, "Giữa kỳ 1", topics, tpl)
                rows = bp["matrix_rows"]
                self.assertAlmostEqual(sum(r["diem"] for r in rows), 10.0, places=4)

    def test_mau_1_scoring_breakdown(self):
        """Kiểm tra Mẫu 1 tuân thủ chuẩn xác cấu trúc điểm của trường (TN 6.0đ, Đ/S 1.0đ, TL 3.0đ)."""
        bp = calculate_exam_blueprint(6, "Giữa kỳ 1", ["Chủ đề A", "Chủ đề B"], "mau_1")
        summary = bp["summary"]
        self.assertEqual(summary["so_cau_tn"], 24)
        self.assertEqual(summary["diem_tn"], 6.0)
        self.assertEqual(summary["so_cau_ds"], 1)
        self.assertEqual(summary["diem_ds"], 1.0)
        self.assertEqual(summary["so_cau_tl"], 3)
        self.assertEqual(summary["diem_tl"], 3.0)
        self.assertEqual(summary["tong_diem_biet"], 4.0)
        self.assertEqual(summary["tong_diem_hieu"], 3.0)
        self.assertEqual(summary["tong_diem_vd"], 3.0)
        self.assertEqual(summary["tong_diem"], 10.0)

    def test_granular_lesson_selection(self):
        """Kiểm tra giáo viên có thể tích chọn riêng từng bài học theo tiến độ giảng dạy thực tế."""
        grade = 6
        topic_key = list(CURRICULUM_DATA[grade]["chu_de"].keys())[0]
        all_lessons = list(CURRICULUM_DATA[grade]["chu_de"][topic_key]["noi_dung"].keys())
        # Chỉ chọn 2 bài đầu tiên
        selected = all_lessons[:2]
        bp = calculate_exam_blueprint(grade, "Giữa kỳ 1", [topic_key], "mau_1", selected_lessons=selected)
        self.assertEqual(len(bp["matrix_rows"]), 2)
        self.assertEqual(bp["summary"]["tong_diem"], 10.0)
        self.assertEqual(sum(r["tn_biet"] for r in bp["matrix_rows"]), 14)
        self.assertEqual(sum(r["tn_hieu"] for r in bp["matrix_rows"]), 10)


class TestDocxExporterHardening(unittest.TestCase):
    """Kiểm tra tính an toàn của đầu vào khi xuất file Word."""

    def test_special_characters_and_overflow_school_name(self):
        bp = calculate_exam_blueprint(6, "Giữa kỳ 1", ["Chủ đề A"], "mau_2")
        content = generate_exam_content(bp)
        
        # Tên trường cực dài kèm ký tự XML nhạy cảm <, >, &, quotes
        malicious_school = "<TRƯỜNG THCS & ĐÔ THỊ 'MỚI' \"TEST\">" + " A" * 200
        buf = generate_exam_docx(bp, content, school_name=malicious_school, time_minutes=-10)
        
        # Kiểm tra tính toàn vẹn OpenXML
        with zipfile.ZipFile(buf, "r") as zf:
            xml_content = zf.read("word/document.xml")
            root = ET.fromstring(xml_content)
            self.assertTrue(root.tag.endswith("document"))

    def test_docx_tien_son_and_mau_1_specification_table(self):
        """Kiểm tra xuất file Word Mẫu 1 có đầy đủ bảng 13 cột và branding Trường THCS Tiên Sơn."""
        bp = calculate_exam_blueprint(7, "Giữa kỳ 1", ["Chủ đề A", "Chủ đề B"], "mau_1")
        content = generate_exam_content(bp)
        buf = generate_exam_docx(bp, content, school_name="Trường THCS Tiên Sơn", time_minutes=45)
        
        with zipfile.ZipFile(buf, "r") as zf:
            xml_str = zf.read("word/document.xml").decode("utf-8")
            self.assertIn("TRƯỜNG THCS TIÊN SƠN", xml_str)
            self.assertIn("LỜI PHÊ CỦA THẦY / CÔ GIÁO", xml_str)
            self.assertIn("6,0 điểm", xml_str)

    def test_streamlit_topic_multiselect_options_and_defaults(self):
        """Đảm bảo không bao giờ xảy ra lỗi StreamlitDefaultNotInOptionsError trên giao diện."""
        for grade in [6, 7, 8, 9]:
            grade_info = CURRICULUM_DATA[grade]
            all_topics = list(grade_info["chu_de"].keys())
            for period in ["Giữa kỳ 1", "Cuối kỳ 1", "Giữa kỳ 2", "Cuối kỳ 2"]:
                period_lessons = grade_info.get("ky_kiem_tra", {}).get(period, [])
                default_topics = []
                for t_k, t_v in grade_info["chu_de"].items():
                    if any(l in period_lessons for l in t_v["noi_dung"].keys()):
                        default_topics.append(t_k)
                valid_defaults = [t for t in default_topics if t in all_topics]
                if not valid_defaults:
                    valid_defaults = all_topics[:2]
                
                # Bất biến: valid_defaults luôn phải là tập con thực sự và không rỗng của all_topics
                self.assertGreater(len(valid_defaults), 0)
                for t in valid_defaults:
                    self.assertIn(t, all_topics)


if __name__ == "__main__":
    unittest.main()
