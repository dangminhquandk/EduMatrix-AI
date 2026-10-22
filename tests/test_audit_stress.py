"""
Script kiểm thử tự động chuyên sâu (Deep Audit & Stress Test Suite) cho EduMatrix AI.
Kiểm tra toàn bộ 4 trục yêu cầu:
1. Combinatorial Stress Testing (32 tổ hợp chuẩn + 4 kịch bản biên + AppTest UI).
2. Mathematical & Constraint Audit (Bảo toàn 10.0đ, tỷ lệ 4:3:3, cấu trúc Mẫu 1 và Mẫu 2).
3. Document Format & XML Safety (.docx integrity, Nghị định 30/2020/NĐ-CP).
4. Error-free verification (Zero KeyError, IndexError, ZeroDivisionError).
"""

import unittest
import zipfile
import xml.etree.ElementTree as ET
import re
from curriculum_data import CURRICULUM_DATA
from matrix_engine import calculate_exam_blueprint
from ai_generator import generate_exam_content, _safe_choice
from docx_exporter import generate_exam_docx
from streamlit.testing.v1 import AppTest


class TestCombinatorialAndEdgeCases(unittest.TestCase):
    """Trục 1 & 2: Kiểm thử tổ hợp toàn diện và kiểm toán toán học."""

    def test_all_32_standard_combinations(self):
        """Quét qua 4 Khối x 4 Kỳ x 2 Mẫu = 32 tổ hợp tiêu chuẩn."""
        grades = [6, 7, 8, 9]
        periods = ["Giữa kỳ 1", "Cuối kỳ 1", "Giữa kỳ 2", "Cuối kỳ 2"]
        templates = ["mau_1", "mau_2"]
        
        passed_count = 0
        for g in grades:
            for p in periods:
                for tpl in templates:
                    topics = CURRICULUM_DATA[g]["ky_kiem_tra"][p]
                    bp = calculate_exam_blueprint(g, p, topics, tpl)
                    
                    # 1. Kiểm tra cấu trúc blueprint
                    self.assertIn("summary", bp)
                    self.assertIn("matrix_rows", bp)
                    rows = bp["matrix_rows"]
                    self.assertGreater(len(rows), 0)
                    
                    # 2. Kiểm toán bất biến toán học: Tổng điểm = 10.0
                    tot_score = sum(r["diem"] for r in rows)
                    self.assertAlmostEqual(tot_score, 10.0, places=5)
                    
                    # 3. Kiểm toán tỷ lệ nhận thức: 4.0 Biết - 3.0 Hiểu - 3.0 Vận dụng
                    if tpl == "mau_1":
                        biet = sum(r["tn_biet"] * 0.25 + r["ds_biet"] * 0.5 for r in rows)
                        hieu = sum(r["tn_hieu"] * 0.25 + r["ds_hieu"] * 0.5 for r in rows)
                        vd = sum(r["tl_vd"] * 1.0 for r in rows)
                        
                        # Cấu trúc Mẫu 1
                        self.assertEqual(sum(r["tn_biet"] for r in rows), 14)
                        self.assertEqual(sum(r["tn_hieu"] for r in rows), 10)
                        self.assertEqual(sum(r["tl_vd"] for r in rows), 3)
                    else:
                        biet = sum(r["tn_biet"] * 0.25 + r["ds_biet"] * 1.0 + r["tln_biet"] * 0.5 for r in rows)
                        hieu = sum(r["tn_hieu"] * 0.25 + r["ds_hieu"] * 1.0 + r["tln_hieu"] * 0.5 for r in rows)
                        vd = sum(r["tl_vd"] * 1.5 for r in rows)
                        
                        # Cấu trúc Mẫu 2
                        self.assertEqual(sum(r["tn_biet"] for r in rows), 8)
                        self.assertEqual(sum(r["tn_hieu"] for r in rows), 4)
                        self.assertEqual(sum(r["tln_biet"] for r in rows), 2)
                        self.assertEqual(sum(r["tln_hieu"] for r in rows), 2)
                        self.assertEqual(sum(r["tl_vd"] for r in rows), 2)
                        
                    self.assertAlmostEqual(biet, 4.0, places=5)
                    self.assertAlmostEqual(hieu, 3.0, places=5)
                    self.assertAlmostEqual(vd, 3.0, places=5)
                    
                    passed_count += 1
                    
        self.assertEqual(passed_count, 32)

    def test_edge_case_empty_selection(self):
        """Kịch bản biên 1: Không chọn chủ đề hay bài học nào -> Phải fallback an toàn 10.0đ."""
        for g in [6, 7, 8, 9]:
            for tpl in ["mau_1", "mau_2"]:
                bp = calculate_exam_blueprint(g, "Giữa kỳ 1", [], tpl, selected_lessons=[])
                self.assertGreater(len(bp["matrix_rows"]), 0)
                self.assertAlmostEqual(sum(r["diem"] for r in bp["matrix_rows"]), 10.0, places=5)

    def test_edge_case_full_selection(self):
        """Kịch bản biên 2: Chọn toàn bộ tất cả bài học trong năm (lên tới 22 bài)."""
        for g in [6, 7, 8, 9]:
            all_units = [u for t in CURRICULUM_DATA[g]["chu_de"].values() for u in t["noi_dung"].keys()]
            for tpl in ["mau_1", "mau_2"]:
                bp = calculate_exam_blueprint(g, "Cuối kỳ 2", list(CURRICULUM_DATA[g]["chu_de"].keys()), tpl, selected_lessons=all_units)
                self.assertEqual(len(bp["matrix_rows"]), len(all_units))
                self.assertAlmostEqual(sum(r["diem"] for r in bp["matrix_rows"]), 10.0, places=5)

    def test_edge_case_single_unit_selection(self):
        """Kịch bản biên 3: Chọn đúng 1 bài học duy nhất (N=1) -> Phải gánh toàn bộ 10.0 điểm mà không lỗi."""
        for g in [6, 7, 8, 9]:
            first_unit = list(next(iter(CURRICULUM_DATA[g]["chu_de"].values()))["noi_dung"].keys())[0]
            for tpl in ["mau_1", "mau_2"]:
                bp = calculate_exam_blueprint(g, "Giữa kỳ 1", [], tpl, selected_lessons=[first_unit])
                self.assertEqual(len(bp["matrix_rows"]), 1)
                self.assertAlmostEqual(sum(r["diem"] for r in bp["matrix_rows"]), 10.0, places=5)

    def test_edge_case_malformed_empty_yccd(self):
        """Kịch bản biên 4: YCCĐ bị rỗng danh sách -> Không được văng IndexError."""
        # Tạo blueprint giả lập có đơn vị bị rỗng yccd
        bp = calculate_exam_blueprint(6, "Giữa kỳ 1", [], "mau_1")
        bp["matrix_rows"][0]["yccd"] = {"biet": [], "hieu": [], "van_dung": []}
        
        # Thử sinh nội dung đề thi ngoại tuyến
        content = generate_exam_content(bp)
        self.assertIn("phan_I_trac_nghiem", content)
        self.assertIn("phan_IV_tu_luan", content)
        self.assertGreater(len(content["phan_I_trac_nghiem"]), 0)


class TestStreamlitAppTestCrossInteractions(unittest.TestCase):
    """Trục 1 (Kịch bản 4): Kiểm thử chuyển đổi chéo liên tục trên giao diện Streamlit."""

    def test_rapid_cross_selection_and_generation(self):
        """Mô phỏng: Lớp 6 Giữa kỳ 1 -> Lớp 9 Cuối kỳ 2 -> Lớp 7 Giữa kỳ 1 -> Bấm tạo đề."""
        at = AppTest.from_file("app.py")
        at.run()
        self.assertEqual(len(at.exception), 0)

        # Chuyển Lớp 9
        at.sidebar.selectbox[0].select(9)
        at.run()
        self.assertEqual(len(at.exception), 0)

        # Chuyển Cuối kỳ 2
        at.sidebar.selectbox[1].select("Cuối kỳ 2")
        at.run()
        self.assertEqual(len(at.exception), 0)

        # Chuyển sang Mẫu 2
        at.sidebar.radio[0].set_value("mau_2")
        at.run()
        self.assertEqual(len(at.exception), 0)

        # Chuyển về Lớp 7 Giữa kỳ 1
        at.sidebar.selectbox[0].select(7)
        at.sidebar.selectbox[1].select("Giữa kỳ 1")
        at.run()
        self.assertEqual(len(at.exception), 0)

        # Kích hoạt nút tạo đề
        at.button[0].click()
        at.run()
        self.assertEqual(len(at.exception), 0)


class TestDocxFormattingAndAdministration(unittest.TestCase):
    """Trục 3: Rà soát định dạng xuất bản Word (.docx) theo thể thức hành chính."""

    def test_random_docx_generation_and_xml_safety(self):
        """Render ngẫu nhiên các kịch bản và kiểm tra độ vẹn toàn XML."""
        test_cases = [
            (6, "Giữa kỳ 1", "mau_1"),
            (7, "Cuối kỳ 1", "mau_2"),
            (8, "Giữa kỳ 2", "mau_1"),
            (9, "Cuối kỳ 2", "mau_2"),
            (6, "Cuối kỳ 2", "mau_1"),
        ]
        
        for grade, period, tpl in test_cases:
            topics = CURRICULUM_DATA[grade]["ky_kiem_tra"][period]
            bp = calculate_exam_blueprint(grade, period, topics, tpl)
            content = generate_exam_content(bp)
            buf = generate_exam_docx(bp, content, school_name="Trường THCS Tiên Sơn", time_minutes=45)
            
            with zipfile.ZipFile(buf, "r") as zf:
                xml_str = zf.read("word/document.xml").decode("utf-8")
                root = ET.fromstring(xml_str)
                self.assertTrue(root.tag.endswith("document"))
                
                # 1. Kiểm tra không còn biến rác kiểu {variable}
                matches = re.findall(r"\{[a-zA-Z0-9_]+\}", xml_str)
                suspicious = [m for m in matches if "openxmlformats" not in m]
                self.assertEqual(len(suspicious), 0, f"Unformatted variables found: {suspicious}")
                
                # 2. Kiểm tra không có chuỗi 'None' hoặc 'undefined'
                for t_el in root.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t"):
                    if t_el.text:
                        self.assertNotIn("None", t_el.text)
                        self.assertNotIn("undefined", t_el.text)
                        
                # 3. Kiểm tra các thành phần văn bản hành chính
                self.assertIn("TRƯỜNG THCS TIÊN SƠN", xml_str)
                self.assertIn("LỜI PHÊ CỦA THẦY / CÔ GIÁO", xml_str)
                self.assertIn("ĐIỂM", xml_str)


if __name__ == "__main__":
    unittest.main()
