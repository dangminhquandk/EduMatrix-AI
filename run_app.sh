#!/bin/bash
# Script khởi chạy ứng dụng EduMatrix AI
cd "$(dirname "$0")"

echo "=========================================================="
echo "   🎓 KHỞI CHẠY EDUMATRIX AI - TRỢ LÝ SƯ PHẠM TIN HỌC    "
echo "=========================================================="
echo "Đang mở ứng dụng trên trình duyệt web..."
echo "Địa chỉ truy cập: http://localhost:8501"
echo "Nhấn Ctrl + C để dừng ứng dụng khi hoàn tất."
echo "=========================================================="

.venv/bin/streamlit run app.py --server.port 8501
