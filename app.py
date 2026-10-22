"""
Ứng dụng Web EduMatrix AI - Trợ lý Sư phạm Soạn Ma trận, Bản đặc tả & Đề thi Tin học THCS chuẩn GDPT 2018.
Sản phẩm tham gia: "Ngày hội Nhà giáo Sáng tạo với Công nghệ số và Trí tuệ nhân tạo 2026"
Đơn vị tổ chức: Cục Nhà giáo & Cán bộ quản lý giáo dục (Bộ GD&ĐT) phối hợp cùng Đại học RMIT Việt Nam.
"""

import os
import streamlit as st
import pandas as pd
from curriculum_data import CURRICULUM_DATA
from matrix_engine import calculate_exam_blueprint
from ai_generator import generate_exam_content
from docx_exporter import generate_exam_docx

st.set_page_config(
    page_title="EduMatrix AI - Trợ lý Ma trận & Đề thi Tin học GDPT 2018",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS cho giao diện sư phạm trang nhã, hiện đại
st.markdown("""
<style>
    .main-title {
        font-size: 2.1rem;
        font-weight: 700;
        color: #1A365D;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #4A5568;
        margin-bottom: 1.2rem;
    }
    .badge {
        display: inline-block;
        padding: 0.25rem 0.6rem;
        font-size: 0.85rem;
        font-weight: 600;
        border-radius: 9999px;
        background-color: #EBF8FF;
        color: #2B6CB0;
        border: 1px solid #BEE3F8;
        margin-bottom: 0.8rem;
    }
    .metric-card {
        background: #F7FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 1rem;
        text-align: center;
    }
    .metric-val {
        font-size: 1.6rem;
        font-weight: 700;
        color: #2B6CB0;
    }
    .metric-lbl {
        font-size: 0.9rem;
        color: #4A5568;
    }
    .stButton>button {
        background-color: #2B6CB0;
        color: white;
        font-weight: 600;
        border-radius: 6px;
        padding: 0.6rem 1.5rem;
        border: none;
        transition: 0.2s;
    }
    .stButton>button:hover {
        background-color: #2C5282;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- SIDEBAR CẤU HÌNH -----------------
with st.sidebar:
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 1.2rem; padding: 0.5rem; background: #EDF2F7; border-radius: 8px;">
        <span style="font-size: 2.2rem;">🎓</span>
        <div>
            <div style="font-weight: 700; font-size: 1.15rem; color: #1A365D;">EduMatrix AI</div>
            <div style="font-size: 0.75rem; color: #4A5568;">Chuyên gia Khảo thí 2026</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("### ⚙️ Cấu hình Khảo thí")
    
    school_name = st.text_input("Đơn vị / Trường THCS:", value="Trường THCS Tiên Sơn")
    
    grade = st.selectbox(
        "Khối lớp (THCS):",
        options=[6, 7, 8, 9],
        format_func=lambda x: f"Tin học Lớp {x}"
    )
    
    period = st.selectbox(
        "Kỳ kiểm tra:",
        options=["Giữa kỳ 1", "Cuối kỳ 1", "Giữa kỳ 2", "Cuối kỳ 2"]
    )
    
    template_type = st.radio(
        "Biểu mẫu Ma trận:",
        options=["mau_1", "mau_2"],
        format_func=lambda x: "Mẫu 1 (Cấu trúc trường: TN 6.0đ + Đúng/Sai 1.0đ + Tự luận 3.0đ)" if x == "mau_1" else "Mẫu 2 (Mới - Bộ GD&ĐT: 4 dạng thức)"
    )
    
    time_minutes = st.number_input("Thời gian làm bài (phút):", min_value=15, max_value=90, value=45, step=15)
    
    st.divider()
    default_env_key = os.environ.get("GEMINI_API_KEY", "")
    if not default_env_key and hasattr(st, "secrets"):
        try:
            default_env_key = st.secrets.get("GEMINI_API_KEY", "")
        except Exception:
            pass
    gemini_key = st.text_input("Gemini API Key (Không bắt buộc):", value=default_env_key, type="password", help="Để trống nếu muốn sử dụng Ngân hàng câu hỏi chuẩn hóa tích hợp sẵn.")
    if not gemini_key:
        st.caption("ℹ️ Đang chạy chế độ **Offline Smart Engine** (Đầy đủ 100% dữ liệu GDPT 2018).")
    else:
        st.caption("✨ Đang kích hoạt **Gemini 2.5 AI Mode**.")

# ----------------- MAIN CONTENT -----------------
st.markdown('<span class="badge">Sản phẩm số dự thi Ngày hội Nhà giáo Sáng tạo 2026 (Bộ GD&ĐT & RMIT)</span>', unsafe_allow_html=True)
st.markdown('<h1 class="main-title">EduMatrix AI: Tự Động Hóa Ma Trận, Đặc Tả & Đề Thi Tin Học THCS</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Khóa cứng tỷ lệ chuẩn <b>40% Nhận biết – 30% Thông hiểu – 30% Vận dụng</b> theo Chương trình GDPT 2018. Xuất file Word (.docx) chuẩn biểu mẫu hành chính trong 3 click.</p>', unsafe_allow_html=True)

# Lấy dữ liệu khối lớp
grade_info = CURRICULUM_DATA[grade]

# Xác định danh sách bài học và chủ đề mặc định cho kỳ kiểm tra
period_lessons = grade_info.get("ky_kiem_tra", {}).get(period, [])
default_topics = []
for t_k, t_v in grade_info["chu_de"].items():
    if any(lesson in period_lessons for lesson in t_v["noi_dung"].keys()):
        default_topics.append(t_k)

all_available_topics = list(grade_info["chu_de"].keys())
valid_default_topics = [t for t in default_topics if t in all_available_topics]
if not valid_default_topics:
    valid_default_topics = all_available_topics[:2]

# Tab điều hướng
tab1, tab2, tab3 = st.tabs(["1. 🎯 Chọn Phạm vi Bài học (KNTT)", "2. 📊 Xem trước Ma trận & Đặc tả", "3. 📝 Tạo & Xuất Bản Word"])

with tab1:
    st.markdown("#### 📌 Bước 1: Chọn các Chủ đề kiến thức đưa vào đề:")
    
    selected_topics = st.multiselect(
        "Danh sách Chủ đề (Chương trình Tin học GDPT 2018):",
        options=all_available_topics,
        default=valid_default_topics,
        format_func=lambda k: f"{k}: {grade_info['chu_de'][k]['ten']}",
        key=f"sel_topics_{grade}_{period}"
    )
    
    if not selected_topics:
        st.warning("⚠️ Vui lòng chọn ít nhất 1 chủ đề kiểm tra.")
        st.stop()
        
    st.markdown("#### 📖 Bước 2: Tích chọn từng bài học đưa vào đề thi (SGK Kết nối tri thức với cuộc sống):")
    st.caption("💡 Thầy/Cô có thể linh hoạt tích hoặc bỏ chọn từng bài học theo đúng tiến độ thực tế trên lớp:")
    
    selected_lessons = []
    for t_key in selected_topics:
        t_data = grade_info["chu_de"][t_key]
        with st.expander(f"📁 {t_key}: {t_data['ten']} ({len(t_data['noi_dung'])} bài học SGK KNTT)", expanded=True):
            for unit_name, yccd_data in t_data["noi_dung"].items():
                cb_key = f"chk_{grade}_{period}_{t_key}_{unit_name}"
                is_default = (unit_name in period_lessons) if period_lessons else True
                is_checked = st.checkbox(
                    f"**{unit_name}**",
                    value=is_default,
                    key=cb_key
                )
                if is_checked:
                    selected_lessons.append(unit_name)
                    
                col_b, col_h, col_v = st.columns(3)
                with col_b:
                    st.caption(f"🔍 **Nhận biết:** {yccd_data['biet'][0]}")
                with col_h:
                    st.caption(f"💡 **Thông hiểu:** {yccd_data['hieu'][0]}")
                with col_v:
                    st.caption(f"⚡ **Vận dụng:** {yccd_data['van_dung'][0]}")
                st.markdown("<hr style='margin: 0.2rem 0; border: none; border-top: 1px dashed #E2E8F0;'/>", unsafe_allow_html=True)

    if not selected_lessons:
        st.warning("⚠️ Thầy/Cô chưa tích chọn bài học nào. Vui lòng chọn ít nhất 1 bài học để lập ma trận.")
        st.stop()

# Tính toán blueprint ma trận với danh sách bài học đã chọn
blueprint = calculate_exam_blueprint(
    grade=grade,
    exam_period=period,
    selected_topic_keys=selected_topics,
    template_type=template_type,
    selected_lessons=selected_lessons
)

with tab2:
    summary = blueprint["summary"]
    st.markdown("#### 🎯 Tỷ lệ Mức độ Nhận thức và Phân bổ Điểm số")
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-val">4.0 điểm</div>
            <div class="metric-lbl">Nhận biết (40%)</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-val">3.0 điểm</div>
            <div class="metric-lbl">Thông hiểu (30%)</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-val">3.0 điểm</div>
            <div class="metric-lbl">Vận dụng (30%)</div>
        </div>
        """, unsafe_allow_html=True)
    with c4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-val">10.0 / 100%</div>
            <div class="metric-lbl">Tổng điểm chuẩn</div>
        </div>
        """, unsafe_allow_html=True)
        
    st.divider()
    st.markdown("#### 📋 Bảng Ma trận Phân bổ Câu hỏi")
    
    # Chuẩn bị dữ liệu hiển thị dataframe
    display_rows = []
    for r in blueprint["matrix_rows"]:
        row_dict = {
            "TT": r["tt"],
            "Chủ đề": r["chu_de"].split(":")[0],
            "Nội dung kiến thức": r["don_vi"],
            "TN Biết": r["tn_biet"],
            "TN Hiểu": r["tn_hieu"],
            "Đ/S Biết": r["ds_biet"],
            "Đ/S Hiểu": r["ds_hieu"],
        }
        if template_type == "mau_2":
            row_dict["TLN Biết"] = r["tln_biet"]
            row_dict["TLN Hiểu"] = r["tln_hieu"]
            row_dict["Tự luận VD"] = r["tl_vd"]
        else:
            row_dict["TL Biết"] = r.get("tl_biet", 0)
            row_dict["TL Hiểu"] = r.get("tl_hieu", 0)
            row_dict["Tự luận VD"] = r["tl_vd"]
            
        row_dict["Tổng câu"] = r["tong_cau"]
        row_dict["Điểm"] = f"{r['diem']}đ"
        row_dict["Tỉ lệ"] = f"{r['ti_le']}%"
        display_rows.append(row_dict)
        
    df_matrix = pd.DataFrame(display_rows)
    st.dataframe(df_matrix, use_container_width=True, hide_index=True)
    
    st.info(f"💡 **Quy cách cấu trúc:** {summary['ten_mau']} bám sát công văn hướng dẫn kiểm tra đánh giá của Bộ GD&ĐT.")

with tab3:
    st.markdown("#### 🚀 Khởi tạo Đề thi và Xuất Tài liệu")
    st.write("Bấm nút bên dưới để hệ thống tự động sinh nội dung câu hỏi bám sát chuẩn kiến thức kỹ năng và đóng gói toàn bộ vào file Microsoft Word:")
    
    if "generated_exam" not in st.session_state:
        st.session_state.generated_exam = None
        st.session_state.docx_bytes = None

    col_btn, col_info = st.columns([1, 2])
    with col_btn:
        generate_clicked = st.button("🚀 BẮT ĐẦU TẠO ĐỀ & MA TRẬN", use_container_width=True)

    if generate_clicked:
        try:
            with st.spinner("⏳ Đang tính toán ma trận, sinh câu hỏi và định dạng bảng biểu Word..."):
                exam_data = generate_exam_content(blueprint, api_key=gemini_key)
                docx_buffer = generate_exam_docx(
                    blueprint=blueprint,
                    exam_content=exam_data,
                    school_name=school_name,
                    time_minutes=time_minutes
                )
                st.session_state.generated_exam = exam_data
                st.session_state.docx_bytes = docx_buffer.getvalue()
                st.success("✅ Đã hoàn tất khởi tạo trọn bộ hồ sơ khảo thí!")
        except Exception as err:
            st.error(f"❌ Đã xảy ra sự cố trong quá trình khởi tạo đề thi: {err}")
            st.info("💡 Gợi ý xử lý: Nếu gặp sự cố kết nối mạng hoặc API Key, hãy thử để trống ô Gemini API Key ở thanh bên trái để hệ thống kích hoạt Ngân hàng Sư phạm nội bộ hoàn toàn ngoại tuyến.")

    if not st.session_state.generated_exam:
        st.markdown("""
        <div style="border: 2px dashed #CBD5E0; border-radius: 8px; padding: 2.2rem; text-align: center; background: #F7FAFC; margin-top: 1rem;">
            <div style="font-size: 2.2rem; margin-bottom: 0.5rem;">📄</div>
            <div style="font-weight: 600; color: #2D3748; font-size: 1.05rem;">Chưa có tài liệu nào được khởi tạo</div>
            <div style="color: #4A5568; font-size: 0.9rem; margin-top: 0.3rem;">Bấm nút <b>"BẮT ĐẦU TẠO ĐỀ & MA TRẬN"</b> ở trên để hệ thống tự động biên soạn toàn bộ hồ sơ khảo thí.</div>
        </div>
        """, unsafe_allow_html=True)

    if st.session_state.generated_exam and st.session_state.docx_bytes:
        file_name = f"MaTran_DacTa_DeThi_{grade_info['ten_khoi'].replace(' ', '_')}_{period.replace(' ', '_')}.docx"
        
        st.download_button(
            label="📥 TẢI TOÀN BỘ FILE WORD (.DOCX) CHUẨN FORM BỘ GD&ĐT",
            data=st.session_state.docx_bytes,
            file_name=file_name,
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            use_container_width=True
        )
        
        st.divider()
        st.markdown("### 👀 Xem trước Nội dung Đề thi")
        
        exam = st.session_state.generated_exam
        
        # Phần I
        with st.expander(f"📘 PHẦN I. CÂU HỎI TRẮC NGHIỆM NHIỀU LỰA CHỌN ({summary['diem_tn']} ĐIỂM)", expanded=True):
            for item in exam.get("phan_I_trac_nghiem", []):
                st.markdown(f"**Câu {item['cau_so']}** ({item['muc_do']}): {item['cau_hoi']}")
                for opt, val in item.get("lua_chon", {}).items():
                    is_correct = " ✅" if opt == item.get("dap_an") else ""
                    st.write(f"&nbsp;&nbsp;&nbsp;&nbsp;**{opt}.** {val}{is_correct}")
                st.caption(f"💡 *Giải thích:* {item.get('giai_thich', '')}")
                st.write("")
                
        # Phần II
        with st.expander(f"📗 PHẦN II. CÂU HỎI TRẮC NGHIỆM ĐÚNG / SAI ({summary['diem_ds']} ĐIỂM)", expanded=True):
            for item in exam.get("phan_II_dung_sai", []):
                st.markdown(f"**Câu {item['cau_so']}:** {item['ngu_canh']}")
                for y in item.get("y_hoi", []):
                    badge_color = "🟢" if y['dap_an'] == "Đúng" else "🔴"
                    st.write(f"&nbsp;&nbsp;&nbsp;&nbsp;**{y['ky_hieu']})** {y['noi_dung']} — {badge_color} **{y['dap_an']}**")
                st.write("")

        # Phần III (nếu có)
        if blueprint["template_type"] == "mau_2":
            with st.expander(f"📙 PHẦN III. CÂU HỎI TRẢ LỜI NGẮN ({summary.get('diem_tln', 2.0)} ĐIỂM)", expanded=True):
                for item in exam.get("phan_III_tra_loi_ngan", []):
                    st.markdown(f"**Câu {item['cau_so']}:** {item['cau_hoi']}")
                    st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;👉 **Đáp án:** `{item['dap_an']}`")
                    st.caption(f"💡 *Giải thích:* {item.get('giai_thich', '')}")
                    st.write("")

        # Phần Tự luận
        with st.expander(f"📕 PHẦN { 'IV' if blueprint['template_type'] == 'mau_2' else 'III' }. TỰ LUẬN ({summary.get('diem_tl', 3.0)} ĐIỂM)", expanded=True):
            for item in exam.get("phan_IV_tu_luan", []):
                st.markdown(f"**Câu {item['cau_so']} ({item['diem']} điểm - {item['muc_do']}):** {item['cau_hoi']}")
                st.markdown("**Hướng dẫn chấm và thang điểm:**")
                for s in item.get("huong_dan_cham", []):
                    st.write(f"- *{s['buoc']}*: **{s['diem']} điểm**")
                st.write("")

# ----------------- FOOTER -----------------
st.divider()
st.markdown("""
<div style="text-align: center; color: #718096; font-size: 0.85rem;">
    <b>Cam kết Ứng dụng AI Có trách nhiệm (Responsible AI) & Liêm chính Sư phạm</b><br>
    Sản phẩm hỗ trợ giáo viên giảm tải 90% thời gian cơ học khi lập bảng ma trận và đặc tả. Giáo viên giữ vai trò chuyên môn cao nhất trong việc thẩm định và phê duyệt nội dung đề thi trước khi ban hành.<br>
    <i>Dự án tham dự Ngày hội Nhà giáo Sáng tạo với Công nghệ số và Trí tuệ nhân tạo năm 2026 (Bộ GD&ĐT & Đại học RMIT).</i>
</div>
""", unsafe_allow_html=True)
