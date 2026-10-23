# BẢN THUYẾT MINH GIẢI PHÁP SÁNG KIẾN ỨNG DỤNG AI TRONG GIÁO DỤC

TÊN SÁNG KIẾN: **EDUMATRIX AI – TRỢ LÝ SƯ PHẠM SỐ TỰ ĐỘNG HÓA THIẾT LẬP MA TRẬN, BẢN ĐẶC TẢ VÀ ĐỀ KIỂM TRA ĐỊNH KỲ MÔN TIN HỌC THCS THEO CHƯƠNG TRÌNH GDPT 2018**

* **Hạng mục tham gia:** Bảng B – Giáo viên khối Trung học Cơ sở
* **Cuộc thi:** Ngày hội Nhà giáo Sáng tạo với Công nghệ số và Trí tuệ nhân tạo năm 2026
* **Đơn vị phối hợp tổ chức:** Cục Nhà giáo và Cán bộ Quản lý Giáo dục (Bộ GD&ĐT) & Đại học RMIT Việt Nam
* **Tác giả:** Giáo viên bộ môn Tin học THCS

---

## 1. BỐI CẢNH VÀ TÍNH CẤP THIẾT CỦA SÁNG KIẾN (Trọng số 25%)

### 1.1. Thực trạng và "Nỗi đau" của nhà giáo

Triển khai Chương trình Giáo dục phổ thông (GDPT) 2018 mang lại bước chuyển mình căn bản từ tiếp cận nội dung sang phát triển toàn diện phẩm chất và năng lực người học. Kéo theo đó, công tác kiểm tra, đánh giá định kỳ đòi hỏi sự chuẩn hóa, khoa học và chặt chẽ ở mức độ rất cao thông qua hai công cụ then chốt: **Bảng ma trận đề kiểm tra** và **Bản đặc tả kỹ thuật đề kiểm tra**.

Tuy nhiên, trong thực tiễn giảng dạy tại các trường THCS hiện nay, việc xây dựng hồ sơ khảo thí định kỳ đang là một áp lực cơ học khổng lồ đối với giáo viên, đặc biệt là các thầy cô giáo lớn tuổi hoặc không chuyên sâu về kỹ thuật:

1. **Độ phức tạp toán học và ràng buộc tỷ lệ khảo thí:** Đề thi phải thỏa mãn nghiêm ngặt tỷ lệ nhận thức **40% Nhận biết – 30% Thông hiểu – 30% Vận dụng** (tỷ lệ 4:3:3). Việc tính toán số lượng câu hỏi, số ý hỏi của nhiều định dạng (Trắc nghiệm 4 lựa chọn, Trắc nghiệm Đúng/Sai, Trả lời ngắn và Tự luận) sao cho vừa khớp thang điểm 10, vừa đúng ma trận từng chủ đề bài học thường làm mất từ **8 đến 12 giờ làm việc thủ công** của mỗi giáo viên trước mỗi kỳ thi.
2. **Sự thay đổi và phân mảnh biểu mẫu:** Khung ma trận thường xuyên được cập nhật theo các đợt tập huấn chuyên môn của Vụ Giáo dục Trung học (ví dụ: chuyển đổi từ Mẫu 1 truyền thống sang Mẫu 2 với 4 dạng thức đánh giá mới). Sự không đồng nhất này khiến giáo viên bối rối trong việc kẻ bảng biểu, gộp ô và căn chỉnh tỷ lệ điểm.
3. **Hạn chế của các công cụ AI thông thường:** Một số giáo viên đã chủ động tìm đến ChatGPT hay Gemini để hỗ trợ tạo đề thi. Tuy nhiên, các mô hình ngôn ngữ lớn (LLM) thuần túy thường xuyên mắc lỗi "ảo giác" (hallucination): tính sai tổng điểm (tổng câu bị thừa hoặc thiếu so với thang 10), sinh dữ liệu lệch tỷ lệ 4:3:3 và đặc biệt là xuất định dạng bảng Markdown bị vỡ khung hoàn toàn khi sao chép sang Microsoft Word.

### 1.2. Tính cấp thiết

Xuất phát từ thực tiễn trên, việc phát triển một công cụ sư phạm chuyên biệt giúp giáo viên **tự động hóa khâu tính toán ma trận, sinh bản đặc tả và xuất ra file Word chuẩn hành chính** chỉ với 3 cú click chuột là một nhu cầu cấp bách, mang lại giá trị nhân văn và thiết thực sâu sắc cho đời sống chuyên môn của nhà giáo.

---

## 2. MỤC TIÊU VÀ Ý TƯỞNG SÁNG TẠO (Trọng số 20%)

### 2.1. Mục tiêu của sáng kiến

* **Mục tiêu chuyên môn:** Đảm bảo 100% đề thi, ma trận và bản đặc tả tuân thủ tuyệt đối khung chuẩn kiến thức kỹ năng của Chương trình GDPT 2018 môn Tin học cấp THCS (Lớp 6, 7, 8, 9).
* **Mục tiêu tối ưu hóa:** Giảm thời gian chuẩn bị hồ sơ khảo thí từ 10 tiếng xuống còn **dưới 5 phút**, triệt tiêu toàn bộ sai sót tính toán số học.
* **Mục tiêu trải nghiệm:** Thiết kế giao diện thân thiện, tinh giản tối đa (Zero-friction) để ngay cả giáo viên lớn tuổi, không rành công nghệ cũng có thể sử dụng thành thạo ngay lần đầu tiên tiếp cận.

### 2.2. Điểm mới và Tính sáng tạo đột phá: Kiến trúc Lai

Khác biệt hoàn toàn với việc chỉ dùng "prompt" văn bản đơn thuần, **EduMatrix AI** tiên phong áp dụng mô hình **Kiến trúc Lai**:

1. **Lớp Thuật toán Khóa cứng:**
   * Toàn bộ cấu trúc ma trận, số lượng câu hỏi, số điểm và tỷ lệ 4:3:3 được lập trình tính toán cứng bằng thuật toán Python.
   * Hệ thống tự động phân bổ cân đối số câu hỏi giữa các chủ đề kiến thức đã chọn, **đảm bảo độ chính xác số học 100% không bao giờ bị lệch**.
2. **Lớp Cơ sở tri thức GDPT 2018 :**
   * Số hóa toàn bộ các mạch nội dung (Chủ đề A đến F) và ma trận Yêu cầu cần đạt (YCCĐ) theo 3 mức độ (Biết - Hiểu - Vận dụng) của sách giáo khoa Tin học 6, 7, 8, 9 (Kết nối tri thức, Cánh diều).
3. **Lớp Trí tuệ nhân tạo Sinh nội dung:**
   * Ứng dụng LLM với cơ chế sinh dữ liệu có cấu trúc (JSON Schema). AI được "ràng buộc" chỉ tập trung sáng tạo nội dung câu hỏi và ngữ cảnh bám sát đúng YCCĐ của từng ô trong ma trận.
4. **Lớp Xuất bản Hành chính Sư phạm:**
   * Ứng dụng thư viện `python-docx` để tự động vẽ bảng ma trận có phân cấp (multi-level header), đổ màu nền shading xám, kẻ viền đơn chuẩn, gộp ô và định dạng phông chữ Times New Roman đúng thể thức văn bản hành chính Việt Nam.

---

## 3. CÔNG NGHỆ VÀ PHƯƠNG THỨC TRIỂN KHAI

### 3.1. Ngăn xếp công nghệ tinh gọn

* **Ngôn ngữ phát triển:** Python 3.9+ module hóa, thân thiện tài nguyên.
* **Giao diện người dùng (Frontend UI):** Streamlit – Tinh gọn, tốc độ phản hồi nhanh, trực quan hóa dữ liệu theo thời gian thực.
* **Mô hình Trí tuệ nhân tạo:** Google Gemini API (kèm cơ chế Fallback Engine chạy offline bảo đảm không phụ thuộc vào kết nối mạng khi trình diễn).
* **Xử lý tài liệu:** `python-docx` chuyên biệt cho việc tự động hóa bảng biểu khảo thí.
* **Môi trường triển khai:** Triển khai trực tuyến trên hạ tầng đám mây Streamlit Community Cloud (miễn phí, giáo viên chỉ cần bấm vào link web trên trình duyệt điện thoại hoặc máy tính).

### 3.2. Quy trình thao tác 3 bước của giáo viên

1. **Bước 1:** Chọn Khối (6-9) & Đợt kiểm tra
2. **Bước 2:** Chọn Biểu mẫu Ma trận (Mẫu 1 hoặc Mẫu 2)
3. **Bước 3:** Bấm nút "Tạo đề" & Tải file Word (.docx)

---

## 4. HIỆU QUẢ VÀ TÁC ĐỘNG THỰC TIỄN (Trọng số 25%)

### 4.1. Hiệu quả đối với Giáo viên và Nhà trường

* **Tiết kiệm thời gian vượt trội:** Thử nghiệm tại tổ chuyên môn trường THCS cho thấy thời gian xây dựng 1 bộ đề kiểm tra định kỳ (bao gồm Ma trận + Đặc tả + Đề thi + Hướng dẫn chấm) giảm từ **8–12 giờ xuống còn 3–5 phút** (giảm hơn 95% thời gian lao động cơ học).
* **Độ chính xác và tính thẩm mỹ đạt chuẩn 100%:** File Word xuất ra đồng nhất, chuẩn lề, chuẩn bảng, không bị lỗi font hay vỡ định dạng khi mở trên các phiên bản Microsoft Office khác nhau.
* **Hỗ trợ sinh đề song song có độ tương đương cao:** Giúp tổ chuyên môn dễ dàng tạo nhiều mã đề thi (Đề A, Đề B) có cùng cấu trúc ma trận và độ khó tương đương để chống gian lận trong phòng thi.

### 4.2. Hiệu quả đối với Học sinh

* Đề thi được thiết kế bám sát năng lực thực tế, minh bạch về tiêu chí chấm điểm.
* Các câu hỏi dạng Đúng/Sai và Trả lời ngắn giúp học sinh làm quen sớm với định dạng đánh giá năng lực hiện đại, kích hoạt tư duy phân tích phản biện thay vì học vẹt.

---

## 5. TÍNH BỀN VỮNG VÀ KHẢ NĂNG NHÂN RỘNG (Trọng số 15%)

* **Khả năng mở rộng liên môn:** Kiến trúc của EduMatrix AI được thiết kế theo dạng Module độc lập (Pluggable Architecture). Hiện tại hệ thống đang chạy dữ liệu môn Tin học THCS, nhưng có thể mở rộng nhanh chóng cho **Toán học, Khoa học Tự nhiên, Lịch sử & Địa lý, Tiếng Anh** chỉ bằng cách bổ sung file cấu hình dữ liệu YCCĐ tương ứng mà không cần viết lại mã nguồn ứng dụng.
* **Khả năng mở rộng đa cấp học:** Dễ dàng áp dụng cho cấp Tiểu học và cấp THPT (Lớp 10, 11, 12).
* **Chi phí vận hành 0 đồng:** Sản phẩm hoàn toàn sử dụng mã nguồn mở và nền tảng miễn phí, không phát sinh chi phí duy trì máy chủ cho nhà trường và giáo viên.

---

## 6. ỨNG DỤNG AI CÓ TRÁCH NHIỆM (RESPONSIBLE AI) VÀ LIÊM CHÍNH HỌC THUẬT (Trọng số 15%)

Sáng kiến tuân thủ chặt chẽ các nguyên tắc đạo đức trong ứng dụng Trí tuệ nhân tạo giáo dục:

1. **Nguyên tắc "Con người giữ quyền quyết định cuối cùng" (Human-in-the-loop):**
   EduMatrix AI không thay thế giáo viên, mà chỉ đóng vai trò là "Thư ký sư phạm thông minh". Giáo viên luôn là người đọc duyệt, thẩm định và hiệu chỉnh lần cuối trước khi ban hành đề thi.
2. **Liêm chính học thuật và Minh bạch tiêu chí:**
   Mọi câu hỏi sinh ra đều gắn liền với mã YCCĐ trong chương trình chính khóa của Bộ GD&ĐT. Hướng dẫn chấm được phân rã chi tiết từng bước (0,25đ – 0,5đ) đảm bảo tính công bằng, khách quan trong kiểm tra đánh giá.
3. **An toàn thông tin và Quyền riêng tư:**
   Hệ thống không thu thập bất kỳ dữ liệu cá nhân nào của học sinh hay giáo viên, hoàn toàn tuân thủ Luật An toàn thông tin mạng và đạo đức số.

---

## 7. KẾT LUẬN VÀ KIẾN NGHỊ

Sáng kiến **EduMatrix AI** đã chứng minh rằng: Khi công nghệ AI được ứng dụng đúng chỗ, giải quyết đúng "điểm nghẽn" thực tế với một tư duy kiến trúc thực dụng và tinh gọn, nó sẽ trở thành đòn bẩy đắc lực giải phóng sức lao động cho người thầy, góp phần thực hiện thắng lợi công cuộc chuyển đổi số toàn diện của ngành giáo dục Việt Nam.
