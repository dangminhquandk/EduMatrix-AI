# syntax=docker/dockerfile:1
# Multi-stage / Slim Production Image for EduMatrix AI
FROM python:3.11-slim

# Thiết lập biến môi trường chuẩn cho Python và Streamlit
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_ADDRESS=0.0.0.0 \
    STREAMLIT_SERVER_HEADLESS=true

# Thư mục làm việc trong container
WORKDIR /app

# Cài đặt curl phục vụ container healthcheck
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Áp dụng nguyên tắc Least Privilege (Bảo mật non-root)
RUN groupadd -g 1001 appgroup && \
    useradd -u 1001 -g appgroup -m -s /bin/bash appuser

# Cài đặt dependencies (tận dụng layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn và phân quyền cho non-root user
COPY --chown=appuser:appgroup . .

# Chuyển sang user non-root
USER appuser

# Mở cổng mặc định của Streamlit
EXPOSE 8501

# Healthcheck xác thực trạng thái máy chủ
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1

# Khởi chạy ứng dụng EduMatrix AI
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
