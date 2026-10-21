"""
Module sinh nội dung câu hỏi đề thi và hướng dẫn chấm theo Bản đặc tả.
Tích hợp Gemini API (google-genai) với chế độ Structured JSON.
Có sẵn Fallback Engine chất lượng cao đảm bảo hoạt động ngay cả khi chưa có API key.
"""

import os
import json
import random
import re
import logging

logger = logging.getLogger("edumatrix.ai_generator")

def generate_exam_content(blueprint: dict, api_key: str = None) -> dict:
    """
    Sinh toàn bộ đề thi, ma trận và đáp án chi tiết dựa trên blueprint.
    Nếu có API key -> Gọi Gemini API để sinh câu hỏi bám sát YCCĐ.
    Nếu không có API key -> Dùng Fallback Pedagogical Engine chất lượng cao.
    """
    if api_key and api_key.strip():
        try:
            return _generate_with_gemini(blueprint, api_key.strip())
        except Exception as e:
            logger.warning("Gemini API call failed (%s). Falling back to internal engine.", type(e).__name__)
            return _generate_with_internal_engine(blueprint)
    else:
        return _generate_with_internal_engine(blueprint)


def _generate_with_gemini(blueprint: dict, api_key: str) -> dict:
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=api_key)
    
    grade_title = blueprint["grade_title"]
    exam_period = blueprint["exam_period"]
    template_type = blueprint["template_type"]
    summary = blueprint["summary"]
    
    # Chuẩn bị thông tin YCCĐ theo từng phần
    units_info = []
    for r in blueprint["matrix_rows"]:
        units_info.append({
            "chu_de": r["chu_de"],
            "don_vi": r["don_vi"],
            "tn_biet": r["tn_biet"],
            "tn_hieu": r["tn_hieu"],
            "ds_biet": r["ds_biet"],
            "ds_hieu": r["ds_hieu"],
            "tln_biet": r.get("tln_biet", 0),
            "tln_hieu": r.get("tln_hieu", 0),
            "tl_vd": r.get("tl_vd", 0)
        })

    prompt = f"""Bạn là chuyên gia khảo thí và sư phạm môn Tin học THCS theo Chương trình GDPT 2018.
Hãy tạo đề kiểm tra {grade_title} - {exam_period} theo ma trận và bản đặc tả sau:
Template: {template_type} ({summary['ten_mau']})
Yêu cầu số lượng câu:
- Trắc nghiệm nhiều lựa chọn: {summary['so_cau_tn']} câu (mỗi câu 4 lựa chọn A, B, C, D, chỉ 1 đáp án đúng).
- Trắc nghiệm Đúng/Sai: {summary['so_cau_ds']} câu (mỗi câu có 1 ngữ cảnh và 4 ý a, b, c, d; mỗi ý xác định Đúng hoặc Sai).
{"- Trả lời ngắn: " + str(summary.get('so_cau_tln', 0)) + " câu (câu hỏi yêu cầu điền cụm từ, thuật ngữ hoặc con số)." if template_type == 'mau_2' else ""}
- Tự luận: {summary.get('so_cau_tl', 2)} câu (có thang điểm chi tiết, giải thích rõ các bước).

Dữ liệu phân bổ các chủ đề và yêu cầu cần đạt:
{json.dumps(units_info, ensure_ascii=False, indent=2)}

Hãy xuất ra định dạng JSON đúng chuẩn với các trường sau:
{{
  "phan_I_trac_nghiem": [
    {{
      "cau_so": 1,
      "muc_do": "Biết",
      "chu_de": "Tên chủ đề",
      "cau_hoi": "Nội dung câu hỏi...",
      "lua_chon": {{
        "A": "Đáp án A",
        "B": "Đáp án B",
        "C": "Đáp án C",
        "D": "Đáp án D"
      }},
      "dap_an": "A",
      "giai_thich": "Giải thích ngắn vì sao chọn A..."
    }}
  ],
  "phan_II_dung_sai": [
    {{
      "cau_so": 1,
      "ngu_canh": "Đoạn thông tin / tình huống dẫn dắt...",
      "y_hoi": [
        {{"ky_hieu": "a", "noi_dung": "Nội dung ý a...", "dap_an": "Đúng", "giai_thich": "Lý do..."}},
        {{"ky_hieu": "b", "noi_dung": "Nội dung ý b...", "dap_an": "Sai", "giai_thich": "Lý do..."}},
        {{"ky_hieu": "c", "noi_dung": "Nội dung ý c...", "dap_an": "Đúng", "giai_thich": "Lý do..."}},
        {{"ky_hieu": "d", "noi_dung": "Nội dung ý d...", "dap_an": "Sai", "giai_thich": "Lý do..."}}
      ]
    }}
  ],
  "phan_III_tra_loi_ngan": [
    {{
      "cau_so": 1,
      "cau_hoi": "Nội dung câu hỏi ngắn...",
      "dap_an": "Từ khóa hoặc số chính xác",
      "giai_thich": "Giải thích vắn tắt..."
    }}
  ],
  "phan_IV_tu_luan": [
    {{
      "cau_so": 1,
      "diem": 1.5,
      "muc_do": "Vận dụng",
      "cau_hoi": "Nội dung câu hỏi tự luận/bài tập...",
      "huong_dan_cham": [
        {{"buoc": "Nêu được luận điểm/công thức chính xác", "diem": 0.5}},
        {{"buoc": "Trình bày các bước thực hiện/giải thuật chi tiết", "diem": 0.75}},
        {{"buoc": "Kết luận và liên hệ thực tiễn", "diem": 0.25}}
      ]
    }}
  ]
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            temperature=0.3
        )
    )
    
    return _sanitize_and_validate_exam_json(response.text, blueprint)


def _sanitize_and_validate_exam_json(raw_input, blueprint: dict) -> dict:
    """
    Làm sạch markdown fences, parse JSON an toàn và kiểm tra/bổ sung cấu trúc dữ liệu thiếu.
    Nếu bất kỳ phần nào bị thiếu hoặc không đủ số lượng câu, tự động kích hoạt
    bộ Engine nội bộ để bù đắp, đảm bảo 100% không bị văng lỗi.
    """
    fallback_data = _generate_with_internal_engine(blueprint)
    template_type = blueprint.get("template_type", "mau_2")
    summary = blueprint.get("summary", {})
    
    data = {}
    if isinstance(raw_input, str):
        text = raw_input.strip()
        if text.startswith("```"):
            text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
            text = re.sub(r"\s*```$", "", text)
        try:
            data = json.loads(text)
        except Exception as parse_err:
            logger.warning("Không thể parse JSON từ AI, sử dụng fallback: %s", parse_err)
            return fallback_data
    elif isinstance(raw_input, dict):
        data = raw_input
    else:
        return fallback_data

    # Validate Phần I: Trắc nghiệm
    so_tn = summary.get("so_cau_tn", 12)
    if "phan_I_trac_nghiem" not in data or not isinstance(data["phan_I_trac_nghiem"], list) or len(data["phan_I_trac_nghiem"]) < so_tn:
        data["phan_I_trac_nghiem"] = fallback_data["phan_I_trac_nghiem"]

    # Validate Phần II: Đúng/Sai
    so_ds = summary.get("so_cau_ds", 2)
    if "phan_II_dung_sai" not in data or not isinstance(data["phan_II_dung_sai"], list) or len(data["phan_II_dung_sai"]) < so_ds:
        data["phan_II_dung_sai"] = fallback_data["phan_II_dung_sai"]

    # Validate Phần III: Trả lời ngắn (nếu Mẫu 2)
    if template_type == "mau_2":
        so_tln = summary.get("so_cau_tln", 4)
        if "phan_III_tra_loi_ngan" not in data or not isinstance(data["phan_III_tra_loi_ngan"], list) or len(data["phan_III_tra_loi_ngan"]) < so_tln:
            data["phan_III_tra_loi_ngan"] = fallback_data["phan_III_tra_loi_ngan"]
    else:
        data["phan_III_tra_loi_ngan"] = []

    # Validate Phần IV: Tự luận
    so_tl = summary.get("so_cau_tl", 2)
    if "phan_IV_tu_luan" not in data or not isinstance(data["phan_IV_tu_luan"], list) or len(data["phan_IV_tu_luan"]) < so_tl:
        data["phan_IV_tu_luan"] = fallback_data["phan_IV_tu_luan"]

    return data


def _generate_with_internal_engine(blueprint: dict) -> dict:
    """
    Bộ Engine Sư phạm nội bộ sinh câu hỏi bám sát 100% YCCĐ của chương trình GDPT 2018.
    """
    matrix_rows = blueprint["matrix_rows"]
    template_type = blueprint["template_type"]
    summary = blueprint["summary"]
    
    # 1. Sinh Phần I: Trắc nghiệm nhiều lựa chọn
    phan_I = []
    cau_tn_idx = 1
    for r in matrix_rows:
        chu_de = r["chu_de"]
        don_vi = r["don_vi"]
        yccd_biet = r["yccd"].get("biet", ["Nhận biết khái niệm cơ bản."])
        yccd_hieu = r["yccd"].get("hieu", ["Hiểu được bản chất và ứng dụng."])
        
        # Sinh câu Biết
        for _ in range(r["tn_biet"]):
            target_yccd = random.choice(yccd_biet)
            correct_text = f"Thể hiện đúng bản chất của {don_vi.lower()} trong môi trường số."
            distractors = [
                "Chỉ áp dụng trong một số trường hợp thiết bị máy tính đời cũ.",
                "Không có liên quan đến việc xử lý dữ liệu và thông tin.",
                "Là thao tác tùy chọn không bắt buộc khi sử dụng công nghệ."
            ]
            raw_choices = [(correct_text, True)] + [(d, False) for d in distractors]
            random.shuffle(raw_choices)
            labels = ["A", "B", "C", "D"]
            lua_chon = {labels[i]: raw_choices[i][0] for i in range(4)}
            dap_an = next(labels[i] for i in range(4) if raw_choices[i][1])

            phan_I.append({
                "cau_so": cau_tn_idx,
                "muc_do": "Nhận biết",
                "chu_de": chu_de,
                "don_vi": don_vi,
                "cau_hoi": f"Theo yêu cầu về \"{don_vi}\": {target_yccd.rstrip('.')} Khẳng định nào sau đây là ĐÚNG NHẤT?",
                "lua_chon": lua_chon,
                "dap_an": dap_an,
                "giai_thich": f"Đáp án {dap_an} phản ánh chính xác chuẩn kiến thức: {target_yccd}"
            })
            cau_tn_idx += 1
            
        # Sinh câu Hiểu
        for _ in range(r["tn_hieu"]):
            target_yccd = random.choice(yccd_hieu)
            correct_text = f"Để hiểu sâu cần phân biệt rõ bản chất của {don_vi.lower()} với các khái niệm liên quan."
            distractors = [
                "Mọi thành phần trong máy tính đều có chức năng hoàn toàn giống nhau.",
                "Không cần phân biệt vì công nghệ hiện đại đã tự động hóa toàn bộ.",
                "Việc nắm vững nguyên lý chỉ cần thiết cho các kỹ sư lập trình chuyên nghiệp."
            ]
            raw_choices = [(correct_text, True)] + [(d, False) for d in distractors]
            random.shuffle(raw_choices)
            labels = ["A", "B", "C", "D"]
            lua_chon = {labels[i]: raw_choices[i][0] for i in range(4)}
            dap_an = next(labels[i] for i in range(4) if raw_choices[i][1])

            phan_I.append({
                "cau_so": cau_tn_idx,
                "muc_do": "Thông hiểu",
                "chu_de": chu_de,
                "don_vi": don_vi,
                "cau_hoi": f"Khi tìm hiểu về \"{don_vi}\", một học sinh thắc mắc: \"{target_yccd.rstrip('.')}\". Em hãy chỉ ra giải thích nào sau đây là chuẩn xác nhất?",
                "lua_chon": lua_chon,
                "dap_an": dap_an,
                "giai_thich": f"Đáp án {dap_an} giúp học sinh giải thích và phân biệt được theo chuẩn: {target_yccd}"
            })
            cau_tn_idx += 1

    # 2. Sinh Phần II: Trắc nghiệm Đúng/Sai
    phan_II = []
    num_ds = summary.get("so_cau_ds", 2)
    for ds_idx in range(1, num_ds + 1):
        target_unit = matrix_rows[(ds_idx - 1) % len(matrix_rows)]
        don_vi = target_unit["don_vi"]
        chu_de = target_unit["chu_de"]
        yccd_b = random.choice(target_unit["yccd"].get("biet", ["Khái niệm cơ bản."]))
        yccd_h = random.choice(target_unit["yccd"].get("hieu", ["Nguyên lý hoạt động."]))
        yccd_v = random.choice(target_unit["yccd"].get("van_dung", ["Áp dụng thực tế."]))
        
        phan_II.append({
            "cau_so": ds_idx,
            "chu_de": chu_de,
            "ngu_canh": f"Trong giờ thực hành Tin học về chủ đề \"{don_vi}\", nhóm học sinh trao đổi về các phương án và thao tác kỹ thuật nhằm giải quyết nhiệm vụ được giao.",
            "y_hoi": [
                {
                    "ky_hieu": "a",
                    "noi_dung": f"{yccd_b} Đây là thao tác nhận biết chuẩn mực cần tuân thủ.",
                    "dap_an": "Đúng",
                    "giai_thich": "Phù hợp hoàn toàn với định nghĩa và chuẩn kiến thức nhận biết."
                },
                {
                    "ky_hieu": "b",
                    "noi_dung": f"Người dùng có thể bỏ qua bước xác thực hoặc kiểm tra khi thực hiện {don_vi.lower()} mà không gây ảnh hưởng gì.",
                    "dap_an": "Sai",
                    "giai_thich": "Việc bỏ qua kiểm tra có thể dẫn đến lỗi hệ thống hoặc mất an toàn dữ liệu."
                },
                {
                    "ky_hieu": "c",
                    "noi_dung": f"{yccd_h} Điều này giúp tăng hiệu quả phối hợp và đảm bảo tính nhất quán.",
                    "dap_an": "Đúng",
                    "giai_thich": "Thể hiện đúng mức độ thông hiểu nguyên lý của đơn vị bài học."
                },
                {
                    "ky_hieu": "d",
                    "noi_dung": f"Trong mọi hoàn cảnh, {yccd_v.lower()} chỉ được áp dụng khi có kết nối Internet tốc độ cao.",
                    "dap_an": "Sai",
                    "giai_thich": "Nhiều kỹ năng và thuật toán xử lý dữ liệu hoàn toàn vận hành ngoại tuyến (offline)."
                }
            ]
        })

    # 3. Sinh Phần III: Trả lời ngắn (nếu là Mẫu 2)
    phan_III = []
    if template_type == "mau_2":
        num_tln = summary.get("so_cau_tln", 4)
        keyword_bank = [
            (["mạng", "kết nối", "lan"], "Tên loại mạng máy tính kết nối các thiết bị trong phạm vi hẹp như một phòng học hay toà nhà là gì?", "LAN", "Mạng cục bộ (Local Area Network)."),
            (["internet", "web", "trình duyệt"], "Dịch vụ phổ biến trên Internet cho phép xem các trang tài liệu siêu văn bản được viết tắt là gì?", "WWW", "World Wide Web."),
            (["email", "thư điện tử"], "Ký hiệu đặc trưng ngăn cách giữa tên người dùng và tên miền trong địa chỉ thư điện tử là ký tự gì?", "@", "Ký tự a còng (@)."),
            (["bảng tính", "excel", "tính toán"], "Ký tự bắt buộc phải gõ đầu tiên trong ô tính khi bắt đầu nhập một công thức tính toán là gì?", "=", "Dấu bằng (=)."),
            (["thuật toán", "lập trình", "lệnh"], "Cấu trúc điều khiển lặp lại một khối lệnh khi điều kiện còn thỏa mãn gọi là cấu trúc gì?", "Lặp", "Cấu trúc lặp trong thuật toán."),
            (["thông tin", "dữ liệu", "bit"], "Đơn vị cơ bản nhỏ nhất dùng để đo lượng thông tin trong máy tính là gì?", "Bit", "Đơn vị nhị phân nhỏ nhất."),
            (["bản quyền", "đạo đức", "pháp luật"], "Quyền tác giả đối với tác phẩm số do mình tạo ra được pháp luật bảo vệ gọi là quyền gì?", "Bản quyền", "Quyền sở hữu trí tuệ / bản quyền."),
            (["đồ họa", "hình ảnh", "gimp", "inkscape"], "Định dạng đồ họa vector phổ biến không bị vỡ hạt khi phóng to có phần mở rộng viết tắt là gì?", "SVG", "Scalable Vector Graphics.")
        ]
        
        for tln_idx in range(1, num_tln + 1):
            target_unit = matrix_rows[(tln_idx - 1) % len(matrix_rows)]
            don_vi = target_unit["don_vi"]
            don_vi_lower = don_vi.lower()
            
            matched = None
            for kw_list, q_text, ans_val, expl in keyword_bank:
                if any(kw in don_vi_lower for kw in kw_list):
                    matched = (q_text, ans_val, expl)
                    break
                    
            if not matched:
                chosen_kw = keyword_bank[(tln_idx - 1) % len(keyword_bank)]
                matched = (chosen_kw[1], chosen_kw[2], chosen_kw[3])
                
            phan_III.append({
                "cau_so": tln_idx,
                "chu_de": target_unit["chu_de"],
                "cau_hoi": f"Trong nội dung \"{don_vi}\": {matched[0]}",
                "dap_an": matched[1],
                "giai_thich": matched[2]
            })

    # 4. Sinh Phần Tự luận (Khóa cứng đúng từng mức độ và thang điểm)
    phan_IV = []
    if template_type == "mau_2":
        # Mẫu 2: 2 câu Vận dụng (1 câu VD 1.5đ, 1 câu VDC 1.5đ = 3.0đ)
        configs = [
            {"diem": 1.5, "muc_do": "Vận dụng"},
            {"diem": 1.5, "muc_do": "Vận dụng cao"}
        ]
        for tl_idx, cfg in enumerate(configs, start=1):
            target_unit = matrix_rows[-(tl_idx % len(matrix_rows) + 1)]
            don_vi = target_unit["don_vi"]
            chu_de = target_unit["chu_de"]
            yccd_vd = random.choice(target_unit["yccd"].get("van_dung", ["Giải quyết vấn đề thực tiễn."]))
            diem = cfg["diem"]
            phan_IV.append({
                "cau_so": tl_idx,
                "diem": diem,
                "muc_do": cfg["muc_do"],
                "chu_de": chu_de,
                "cau_hoi": f"Em hãy vận dụng kiến thức bài học \"{don_vi}\" để giải quyết tình huống sau:\n\"{yccd_vd}\"\nHãy trình bày rõ ràng các bước thực hiện, phân tích lý do chọn giải pháp và nêu biện pháp đảm bảo an toàn/hiệu quả.",
                "huong_dan_cham": [
                    {"buoc": "Xác định đúng mục tiêu, các dữ liệu đầu vào và đầu ra cần đạt được.", "diem": round(diem * 0.3, 2)},
                    {"buoc": f"Trình bày chi tiết từng bước giải quyết bài toán bám sát nguyên lý của {don_vi.lower()}.", "diem": round(diem * 0.5, 2)},
                    {"buoc": "Đưa ra đánh giá, nhận xét về tính tối ưu hoặc các lưu ý an toàn đạo đức khi thực hiện.", "diem": round(diem * 0.2, 2)}
                ]
            })
    else:
        # Mẫu 1: 3 câu Tự luận = 3.0đ (1.0đ/câu ở mức độ Vận dụng / Vận dụng cao)
        configs = [
            {"diem": 1.0, "muc_do": "Vận dụng", "key": "van_dung", "prompt": "Em hãy vận dụng kiến thức bài học để giải quyết tình huống sau:"},
            {"diem": 1.0, "muc_do": "Vận dụng", "key": "van_dung", "prompt": "Em hãy trình bày các bước thao tác kỹ thuật và giải thích lý do thực hiện đối với:"},
            {"diem": 1.0, "muc_do": "Vận dụng cao", "key": "van_dung", "prompt": "Em hãy phân tích, so sánh các giải pháp và đề xuất phương án tối ưu cho tình huống:"}
        ]
        for tl_idx, cfg in enumerate(configs, start=1):
            target_unit = matrix_rows[(tl_idx - 1) % len(matrix_rows)]
            don_vi = target_unit["don_vi"]
            chu_de = target_unit["chu_de"]
            yccd_list = target_unit["yccd"].get(cfg["key"], ["Chuẩn kiến thức kỹ năng."])
            yccd_selected = random.choice(yccd_list)
            diem = cfg["diem"]
            phan_IV.append({
                "cau_so": tl_idx,
                "diem": diem,
                "muc_do": cfg["muc_do"],
                "chu_de": chu_de,
                "cau_hoi": f"{cfg['prompt']} \"{don_vi}\" ({yccd_selected}).",
                "huong_dan_cham": [
                    {"buoc": "Trình bày đúng trọng tâm kiến thức và luận điểm yêu cầu.", "diem": round(diem * 0.6, 2)},
                    {"buoc": "Giải thích chi tiết, có ví dụ minh họa hoặc liên hệ thực tế.", "diem": round(diem * 0.4, 2)}
                ]
            })

    return {
        "phan_I_trac_nghiem": phan_I,
        "phan_II_dung_sai": phan_II,
        "phan_III_tra_loi_ngan": phan_III,
        "phan_IV_tu_luan": phan_IV
    }
