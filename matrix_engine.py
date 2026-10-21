"""
Module tính toán ma trận và đặc tả đề kiểm tra Tin học THCS theo chuẩn GDPT 2018.
Đảm bảo 100% tính toán chính xác tỷ lệ 4:3:3 (40% Biết - 30% Hiểu - 30% Vận dụng).
Hỗ trợ cả Mẫu 1 (Chuẩn trường THCS: TN 6.0đ + Đúng/Sai 1.0đ + Tự luận 3.0đ)
và Mẫu 2 (Khung tập huấn mới của Bộ GD&ĐT do TS. Vũ Cẩm Tú hướng dẫn).
"""

from functools import lru_cache
from curriculum_data import CURRICULUM_DATA

# Centralized Pedagogical Constants
RATIO_BIET = 40.0
RATIO_HIEU = 30.0
RATIO_VD = 30.0
TOTAL_POINTS = 10.0

def calculate_exam_blueprint(
    grade: int,
    exam_period: str,
    selected_topic_keys: list = None,
    template_type: str = "mau_2",
    selected_lessons: list = None
) -> dict:
    """
    Sinh cấu trúc ma trận và bản đặc tả phân bổ chi tiết cho từng đơn vị kiến thức/bài học.
    Được tối ưu hóa bộ đệm (cached) và đảm bảo an toàn biên (edge-case hardened).
    """
    topics_tuple = tuple(selected_topic_keys) if selected_topic_keys else ()
    lessons_tuple = tuple(selected_lessons) if selected_lessons else ()
    return _calculate_blueprint_cached(grade, exam_period, topics_tuple, template_type, lessons_tuple)


@lru_cache(maxsize=128)
def _calculate_blueprint_cached(
    grade: int,
    exam_period: str,
    selected_topics_tuple: tuple,
    template_type: str = "mau_2",
    selected_lessons_tuple: tuple = ()
) -> dict:
    grade_data = CURRICULUM_DATA.get(grade, CURRICULUM_DATA[6])
    topics = grade_data["chu_de"]
    
    units = []
    
    # 1. Ưu tiên lấy theo danh sách bài học cụ thể do giáo viên tích chọn
    if selected_lessons_tuple:
        for t_key, t_info in topics.items():
            for u_name, u_yccd in t_info["noi_dung"].items():
                if u_name in selected_lessons_tuple:
                    units.append({
                        "chu_de_key": t_key,
                        "chu_de_ten": t_key,
                        "don_vi_kien_thuc": u_name,
                        "yccd": u_yccd
                    })
                    
    # 2. Nếu không có selected_lessons_tuple thì lấy theo chủ đề hoặc kỳ kiểm tra mặc định
    if not units:
        valid_topics = [k for k in selected_topics_tuple if k in topics]
        if not valid_topics:
            default_items = grade_data["ky_kiem_tra"].get(exam_period, [])
            for t_key, t_info in topics.items():
                for u_name, u_yccd in t_info["noi_dung"].items():
                    if u_name in default_items or t_key in default_items:
                        units.append({
                            "chu_de_key": t_key,
                            "chu_de_ten": t_key,
                            "don_vi_kien_thuc": u_name,
                            "yccd": u_yccd
                        })
            if not units:
                valid_topics = list(topics.keys())[:2]
                for t_key in valid_topics:
                    t_info = topics[t_key]
                    for u_name, u_yccd in t_info["noi_dung"].items():
                        units.append({
                            "chu_de_key": t_key,
                            "chu_de_ten": t_key,
                            "don_vi_kien_thuc": u_name,
                            "yccd": u_yccd
                        })
        else:
            for t_key in valid_topics:
                t_info = topics[t_key]
                for u_name, u_yccd in t_info["noi_dung"].items():
                    units.append({
                        "chu_de_key": t_key,
                        "chu_de_ten": t_key,
                        "don_vi_kien_thuc": u_name,
                        "yccd": u_yccd
                    })

    num_units = len(units)
    if num_units == 0:
        first_k = next(iter(topics.keys()))
        first_t = topics[first_k]
        for u_name, u_yccd in first_t["noi_dung"].items():
            units.append({
                "chu_de_key": first_k,
                "chu_de_ten": first_k,
                "don_vi_kien_thuc": u_name,
                "yccd": u_yccd
            })
        num_units = len(units)

    if template_type == "mau_2":
        # MẪU 2 (Chuẩn tập huấn mới của Bộ GD&ĐT do TS. Vũ Cẩm Tú hướng dẫn):
        # 1. Nhiều lựa chọn: 12 câu = 3.0đ (0.25đ/câu) -> 8 Biết (2.0đ), 4 Hiểu (1.0đ)
        # 2. Đúng/Sai: 2 câu lớn = 2.0đ (1.0đ/câu, mỗi câu 4 ý a,b,c,d) -> 1 Biết (1.0đ), 1 Hiểu (1.0đ)
        # 3. Trả lời ngắn: 4 câu = 2.0đ (0.5đ/câu) -> 2 Biết (1.0đ), 2 Hiểu (1.0đ)
        # 4. Tự luận: 2 câu = 3.0đ -> 2 câu Vận dụng (1 câu VD 2.0đ, 1 câu VDC 1.0đ)
        # TỔNG MỨC ĐỘ:
        # Biết: 2.0 (TN) + 1.0 (Đ/S) + 1.0 (TLN) = 4.0 điểm (40%)
        # Hiểu: 1.0 (TN) + 1.0 (Đ/S) + 1.0 (TLN) = 3.0 điểm (30%)
        # Vận dụng: 3.0 (Tự luận) = 3.0 điểm (30%)
        # Tổng điểm: 10.0 điểm
        
        target_counts = {
            "tn_biet": 8,
            "tn_hieu": 4,
            "ds_biet": 1,
            "ds_hieu": 1,
            "tln_biet": 2,
            "tln_hieu": 2,
            "tl_vd": 2
        }
        
        matrix_rows = []
        for i, u in enumerate(units):
            matrix_rows.append({
                "tt": i + 1,
                "chu_de": u["chu_de_ten"],
                "don_vi": u["don_vi_kien_thuc"],
                "yccd": u["yccd"],
                "tn_biet": 0, "tn_hieu": 0, "tn_vd": 0,
                "ds_biet": 0, "ds_hieu": 0, "ds_vd": 0,
                "tln_biet": 0, "tln_hieu": 0, "tln_vd": 0,
                "tl_biet": 0, "tl_hieu": 0, "tl_vd": 0,
            })
            
        # Phân bổ sư phạm công bằng:
        # 1. Tự luận: 2 câu VD (1.5đ mỗi câu = 3.0đ) -> rải đều theo các mốc đơn vị
        for i in range(target_counts["tl_vd"]):
            idx = (i * num_units // 2) % num_units
            matrix_rows[idx]["tl_vd"] += 1

        # 2. Đúng/Sai: 2 câu (1 Biết, 1 Hiểu) -> bố trí lệch pha với Tự luận
        matrix_rows[(1 * num_units // 2 + 1) % num_units]["ds_biet"] += 1
        matrix_rows[(0 * num_units // 2 + 1) % num_units]["ds_hieu"] += 1

        # 3. Trả lời ngắn: 4 câu (2 Biết, 2 Hiểu) -> xoay vòng theo con trỏ
        cursor = 2 % num_units
        for _ in range(target_counts["tln_biet"]):
            matrix_rows[cursor]["tln_biet"] += 1
            cursor = (cursor + 1) % num_units
        for _ in range(target_counts["tln_hieu"]):
            matrix_rows[cursor]["tln_hieu"] += 1
            cursor = (cursor + 1) % num_units

        # 4. TNKQ nhiều lựa chọn: 8 Biết, 4 Hiểu -> xoay vòng phủ đều
        cursor = 1 % num_units
        for _ in range(target_counts["tn_biet"]):
            matrix_rows[cursor]["tn_biet"] += 1
            cursor = (cursor + 1) % num_units
        for _ in range(target_counts["tn_hieu"]):
            matrix_rows[cursor]["tn_hieu"] += 1
            cursor = (cursor + 1) % num_units

        for row in matrix_rows:
            row["tong_biet"] = row["tn_biet"] + row["ds_biet"] + row["tln_biet"]
            row["tong_hieu"] = row["tn_hieu"] + row["ds_hieu"] + row["tln_hieu"]
            row["tong_vd"] = row["tl_vd"]
            row["tong_cau"] = row["tong_biet"] + row["tong_hieu"] + row["tong_vd"]
            row["diem"] = (
                (row["tn_biet"] + row["tn_hieu"]) * 0.25 +
                (row["ds_biet"] + row["ds_hieu"]) * 1.0 +
                (row["tln_biet"] + row["tln_hieu"]) * 0.5 +
                row["tl_vd"] * 1.5
            )
            row["ti_le"] = round((row["diem"] / 10.0) * 100, 1)

        summary = {
            "template": "mau_2",
            "ten_mau": "Mẫu 2 (Khung tập huấn mới Bộ GD&ĐT: TN 4 lựa chọn + Đúng/Sai + Trả lời ngắn + Tự luận)",
            "so_cau_tn": 12, "diem_tn": 3.0,
            "so_cau_ds": 2, "diem_ds": 2.0,
            "so_cau_tln": 4, "diem_tln": 2.0,
            "so_cau_tl": 2, "diem_tl": 3.0,
            "tong_diem_biet": 4.0, "ti_le_biet": 40.0,
            "tong_diem_hieu": 3.0, "ti_le_hieu": 30.0,
            "tong_diem_vd": 3.0, "ti_le_vd": 30.0,
            "tong_diem": 10.0
        }

    else:
        # MẪU 1 (Theo chuẩn quy định trường THCS: TN 6.0đ, Đúng/Sai 1.0đ, Tự luận 3.0đ):
        # 1. Nhiều lựa chọn: 24 câu = 6.0đ (0.25đ/câu) -> 14 Biết (3.5đ), 10 Hiểu (2.5đ)
        # 2. Đúng/Sai: 1 câu (4 ý) = 1.0đ -> 1 ý/câu Biết (0.5đ), 1 ý/câu Hiểu (0.5đ)
        # 3. Tự luận: 3 câu = 3.0đ (1.0đ/câu) -> 3 câu Vận dụng (3.0đ)
        # TỔNG MỨC ĐỘ:
        # Biết: 3.5 (TN) + 0.5 (Đ/S) = 4.0 điểm (40%)
        # Hiểu: 2.5 (TN) + 0.5 (Đ/S) = 3.0 điểm (30%)
        # Vận dụng: 3.0 (Tự luận Vận dụng) = 3.0 điểm (30%)
        # TỔNG TOÀN BÀI: 10.0 điểm (100%)
        # Tỉ lệ dạng thức: TN 6.0đ (60%) + Đ/S 1.0đ (10%) + TL 3.0đ (30%) = 10.0đ (100%)
        target_counts = {
            "tn_biet": 14,
            "tn_hieu": 10,
            "ds_biet": 1,
            "ds_hieu": 1,
            "tl_vd": 3
        }
        
        matrix_rows = []
        for i, u in enumerate(units):
            matrix_rows.append({
                "tt": i + 1,
                "chu_de": u["chu_de_ten"],
                "don_vi": u["don_vi_kien_thuc"],
                "yccd": u["yccd"],
                "tn_biet": 0, "tn_hieu": 0, "tn_vd": 0,
                "ds_biet": 0, "ds_hieu": 0, "ds_vd": 0,
                "tl_biet": 0, "tl_hieu": 0, "tl_vd": 0,
            })
            
        # Phân bổ sư phạm công bằng:
        # 1. Tự luận Vận dụng: 3 câu (1.0đ mỗi câu = 3.0đ) -> rải đều theo các mốc đơn vị
        for i in range(target_counts["tl_vd"]):
            idx = (i * num_units // 3) % num_units
            matrix_rows[idx]["tl_vd"] += 1

        # 2. Đúng/Sai: 1 câu (1 ý Biết 0.5đ, 1 ý Hiểu 0.5đ) -> bố trí lệch pha với Tự luận
        matrix_rows[(1 * num_units // 2) % num_units]["ds_biet"] += 1
        matrix_rows[(1 * num_units // 2 + 1) % num_units]["ds_hieu"] += 1

        # 3. TNKQ nhiều lựa chọn: 14 Biết, 10 Hiểu -> xoay vòng phủ đều toàn bộ các đơn vị
        cursor = 0
        for _ in range(target_counts["tn_biet"]):
            matrix_rows[cursor]["tn_biet"] += 1
            cursor = (cursor + 1) % num_units
        for _ in range(target_counts["tn_hieu"]):
            matrix_rows[cursor]["tn_hieu"] += 1
            cursor = (cursor + 1) % num_units

        for row in matrix_rows:
            row["tong_biet"] = row["tn_biet"] + row["ds_biet"]
            row["tong_hieu"] = row["tn_hieu"] + row["ds_hieu"]
            row["tong_vd"] = row["tl_vd"]
            row["tong_cau"] = row["tong_biet"] + row["tong_hieu"] + row["tong_vd"]
            row["diem"] = (
                (row["tn_biet"] + row["tn_hieu"]) * 0.25 +
                (row["ds_biet"] + row["ds_hieu"]) * 0.5 +
                row["tl_vd"] * 1.0
            )
            row["ti_le"] = round((row["diem"] / 10.0) * 100, 1)

        summary = {
            "template": "mau_1",
            "ten_mau": "Mẫu 1 (Theo cấu trúc trường: TN 6.0đ + Đúng/Sai 1.0đ + Tự luận 3.0đ)",
            "so_cau_tn": 24, "diem_tn": 6.0,
            "so_cau_ds": 1, "diem_ds": 1.0,
            "so_cau_tl": 3, "diem_tl": 3.0,
            "tong_diem_biet": 4.0, "ti_le_biet": 40.0,
            "tong_diem_hieu": 3.0, "ti_le_hieu": 30.0,
            "tong_diem_vd": 3.0, "ti_le_vd": 30.0,
            "tong_diem": 10.0
        }

    return {
        "grade": grade,
        "grade_title": grade_data["ten_khoi"],
        "exam_period": exam_period,
        "template_type": template_type,
        "summary": summary,
        "matrix_rows": matrix_rows
    }
