# Sử dụng bản python nhẹ
FROM python:3.9-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Copy các file vào container
COPY . .

# Cài đặt thư viện
RUN pip install --no-cache-dir -r requirements.txt

# Chạy ứng dụng bằng gunicorn (tốt hơn cho production)
CMD ["gunicorn", "-b", "0.0.0.0:10000", "app:app"]