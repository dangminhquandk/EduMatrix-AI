"""
Module tính toán ma trận và đặc tả đề kiểm tra Tin học THCS theo chuẩn GDPT 2018.
Đảm bảo 100% tính toán chính xác tỷ lệ 4:3:3 (40% Biết - 30% Hiểu - 30% Vận dụng).
Hỗ trợ cả Mẫu 1 (Truyền thống/docx trường) và Mẫu 2 (Khung tập huấn mới của Bộ GD&ĐT).
"""

from functools import lru_cache
from curriculum_data import CURRICULUM_DATA

# Centralized Pedagogical Constants
RATIO_BIET = 40.0
RATIO_HIEU = 30.0
RATIO_VD = 30.0
TOTAL_POINTS = 10.0

def calculate_exam_blueprint(grade: int, exam_period: str, selected_topic_keys: list, template_type: str = "mau_2"):
    """
    Sinh cấu trúc ma trận và bản đặc tả phân bổ chi tiết cho từng đơn vị kiến thức.
    Được tối ưu hóa bộ đệm (cached) và đảm bảo an toàn biên (edge-case hardened).
    """
    topics_tuple = tuple(selected_topic_keys) if selected_topic_keys else ()
    return _calculate_blueprint_cached(grade, exam_period, topics_tuple, template_type)


@lru_cache(maxsize=128)
def _calculate_blueprint_cached(grade: int, exam_period: str, selected_topics_tuple: tuple, template_type: str = "mau_2"):
    grade_data = CURRICULUM_DATA.get(grade, CURRICULUM_DATA[6])
    topics = grade_data["chu_de"]
    
    # Lọc các chủ đề được chọn
    valid_topics = [k for k in selected_topics_tuple if k in topics]
    if not valid_topics:
        valid_topics = grade_data["ky_kiem_tra"].get(exam_period, list(topics.keys())[:2])
        valid_topics = [k for k in valid_topics if k in topics]
        if not valid_topics:
            valid_topics = list(topics.keys())[:2]
        
    # Tổng hợp tất cả các đơn vị kiến thức
    units = []
    for t_key in valid_topics:
        t_info = topics[t_key]
        for u_name, u_yccd in t_info["noi_dung"].items():
            units.append({
                "chu_de_key": t_key,
                "chu_de_ten": f"{t_key}: {t_info['ten']}",
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
                "chu_de_ten": f"{first_k}: {first_t['ten']}",
                "don_vi_kien_thuc": u_name,
                "yccd": u_yccd
            })
        num_units = len(units)

    if template_type == "mau_2":
        # MẪU 2 (Chuẩn tập huấn mới của Bộ GD&ĐT):
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
            
        # Phân bổ sư phạm công bằng (Fair-share Pedagogical Distribution):
        # 1. Tự luận: 2 câu VD (1.5đ mỗi câu) -> rải đều theo các mốc đơn vị
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

        # 4. TNKQ nhiều lựa chọn: 8 Biết, 4 Hiểu -> xoay vòng phủ đều toàn bộ các đơn vị
        for _ in range(target_counts["tn_biet"]):
            matrix_rows[cursor]["tn_biet"] += 1
            cursor = (cursor + 1) % num_units
        for _ in range(target_counts["tn_hieu"]):
            matrix_rows[cursor]["tn_hieu"] += 1
            cursor = (cursor + 1) % num_units
        
        # Tính toán tổng dòng và điểm
        for row in matrix_rows:
            row["tong_biet"] = row["tn_biet"] + row["ds_biet"] + row["tln_biet"] + row["tl_biet"]
            row["tong_hieu"] = row["tn_hieu"] + row["ds_hieu"] + row["tln_hieu"] + row["tl_hieu"]
            row["tong_vd"] = row["tn_vd"] + row["ds_vd"] + row["tln_vd"] + row["tl_vd"]
            row["tong_cau"] = row["tong_biet"] + row["tong_hieu"] + row["tong_vd"]
            # Điểm tính theo trọng số từng loại
            row["diem"] = (
                (row["tn_biet"] + row["tn_hieu"]) * 0.25 +
                (row["ds_biet"] + row["ds_hieu"]) * 1.0 +
                (row["tln_biet"] + row["tln_hieu"]) * 0.5 +
                row["tl_vd"] * 1.5
            )
            row["ti_le"] = round((row["diem"] / 10.0) * 100, 1)

        summary = {
            "template": "mau_2",
            "ten_mau": "Mẫu 2 (Chuẩn tập huấn mới Bộ GD&ĐT: TN 4 lựa chọn + Đúng/Sai + Trả lời ngắn + Tự luận)",
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
        # MẪU 1 (Truyền thống theo file docx của trường):
        # 1. Nhiều lựa chọn: 16 câu = 4.0đ (0.25đ/câu) -> 10 Biết (2.5đ), 6 Hiểu (1.5đ)
        # 2. Đúng/Sai: 2 câu = 2.0đ (1.0đ/câu) -> 1 Biết (1.0đ), 1 Hiểu (1.0đ)
        # 3. Tự luận: 3 câu = 4.0đ (hoặc 2 câu = 3.0đ và TN 5.0đ, ở đây chuẩn 16 TN 4đ + 2 Đ/S 2đ + 2 TL 4đ = 10đ)
        # TỔNG MỨC ĐỘ:
        # Biết: 2.5 (TN) + 1.0 (Đ/S) + 0.5 (TL Biết) = 4.0 điểm (40%)
        # Hiểu: 1.5 (TN) + 1.0 (Đ/S) + 0.5 (TL Hiểu) = 3.0 điểm (30%)
        # Vận dụng: 3.0 (Tự luận Vận dụng) = 3.0 điểm (30%)
        target_counts = {
            "tn_biet": 10,
            "tn_hieu": 6,
            "ds_biet": 1,
            "ds_hieu": 1,
            "tl_biet": 1, # 0.5đ
            "tl_hieu": 1, # 0.5đ
            "tl_vd": 2    # 3.0đ
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
            
        # Phân bổ sư phạm công bằng (Fair-share Pedagogical Distribution):
        # 1. Tự luận Vận dụng: 2 câu (1.5đ mỗi câu = 3.0đ) -> rải đều theo các mốc đơn vị
        for i in range(target_counts["tl_vd"]):
            idx = (i * num_units // 2) % num_units
            matrix_rows[idx]["tl_vd"] += 1

        # 2. Tự luận Biết (1 câu 0.5đ) và Tự luận Hiểu (1 câu 0.5đ) -> bố trí lệch pha 1
        matrix_rows[(1 * num_units // 2 + 1) % num_units]["tl_biet"] += 1
        matrix_rows[(0 * num_units // 2 + 1) % num_units]["tl_hieu"] += 1

        # 3. Đúng/Sai: 2 câu (1 Biết, 1 Hiểu) -> bố trí lệch pha 2
        matrix_rows[(0 * num_units // 2 + 2) % num_units]["ds_biet"] += 1
        matrix_rows[(1 * num_units // 2 + 2) % num_units]["ds_hieu"] += 1

        # 4. TNKQ nhiều lựa chọn: 10 Biết, 6 Hiểu -> xoay vòng phủ đều toàn bộ các đơn vị
        cursor = 3 % num_units
        for _ in range(target_counts["tn_biet"]):
            matrix_rows[cursor]["tn_biet"] += 1
            cursor = (cursor + 1) % num_units
        for _ in range(target_counts["tn_hieu"]):
            matrix_rows[cursor]["tn_hieu"] += 1
            cursor = (cursor + 1) % num_units

        for row in matrix_rows:
            row["tong_biet"] = row["tn_biet"] + row["ds_biet"] + row["tl_biet"]
            row["tong_hieu"] = row["tn_hieu"] + row["ds_hieu"] + row["tl_hieu"]
            row["tong_vd"] = row["tn_vd"] + row["ds_vd"] + row["tl_vd"]
            row["tong_cau"] = row["tong_biet"] + row["tong_hieu"] + row["tong_vd"]
            row["diem"] = (
                (row["tn_biet"] + row["tn_hieu"]) * 0.25 +
                (row["ds_biet"] + row["ds_hieu"]) * 1.0 +
                row["tl_biet"] * 0.5 + row["tl_hieu"] * 0.5 + row["tl_vd"] * 1.5
            )
            row["ti_le"] = round((row["diem"] / 10.0) * 100, 1)

        summary = {
            "template": "mau_1",
            "ten_mau": "Mẫu 1 (Theo cấu trúc docx trường: TN 4 lựa chọn + Đúng/Sai + Tự luận)",
            "so_cau_tn": 16, "diem_tn": 4.0,
            "so_cau_ds": 2, "diem_ds": 2.0,
            "so_cau_tl": 4, "diem_tl": 4.0,
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
        "matrix_rows": matrix_rows,
        "summary": summary
    }
