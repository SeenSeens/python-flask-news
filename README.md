# Flask Application Template
Đây là mẫu cơ sở cho các ứng dụng web Flask. Nó cung cấp một điểm khởi đầu có cấu trúc cho các dự án mới, tuân thủ các phương pháp hay nhất trong quá trình phát triển Flask và tổ chức dự án.

## Features
- Thiết kế mô-đun sử dụng Blueprints.
- Xử lý lỗi đối với mã trạng thái HTTP 400, 403, 404 và 500.
- Kết xuất mẫu bằng Jinja2.
- Cấu hình dựa trên môi trường thông qua tệp `.env`.
- Xử lý tải lên tệp cơ bản và phân phát tệp tĩnh.
- Ghi nhật ký được cấu hình trước.

## Bắt đầu nhanh
1. Sao chép kho lưu trữ.
2. Sao chép `.env.example` sang `.env` và đặt các biến môi trường của bạn.
3. Cài đặt phụ thuộc: `pip install -r requirements.txt`.
4. Chạy ứng dụng: `flask run`.# python-flask-news

## Project Structure

- `app/`: Gói ứng dụng chứa Blueprints, static files, templates, và routes.
- `ap/admin`: Kế hoạch chi tiết cho các tuyến ứng dụng quản trị.
- `app/main/`: Kế hoạch chi tiết cho các tuyến ứng dụng người dùng.
- `app/models`: Gói ứng dụng models, có thể chứa các hàm hoặc biến dùng chung cho tất cả các models.
- `app/models/common_fields`: Các field dùng chung
- `app/static/`: Thư mục dành cho các tệp CSS, JavaScript và hình ảnh.
- `app/templates/`: Mẫu Jinja2 cho ứng dụng.
- `instance/`: Folder for instance-specific configurations (not under version control).
- `migrations`: Thư mục chứa các file liên quan đến quá trình di chuyển (migration) cơ sở dữ liệu, được tạo ra bởi Flask-Migrate và Alembic.
- `tests`: Chứa các test cho gói ứng dụng.
- `.env`: General environment variables (not to be committed).
- `.env.example`
- `.flaskenv`: File chứa các biến môi trường dành riêng cho Flask.
- `.gitignore`: 
- `application.py`: Entry point for the Flask application.
- `config.py`: Chứa các thiết lập cấu hình của ứng dụng.
- `flask-template.log`
- `README.md`: File chứa thông tin và hướng dẫn sử dụng dự án
- `requirements.txt`: Danh sách các thư viện và phiên bản cần cài đặt cho dự án.

## Cấu hình
Định cấu hình ứng dụng bằng tệp `.env`. Tham chiếu `.env.example` cho các biến bắt buộc.

## Cách sử dụng
Để tạo một dự án mới:
1. Sao chép kho lưu trữ này.
2. Đổi tên thư mục dự án.
3. Khởi tạo kho lưu trữ git mới.
4. Tùy chỉnh Bản thiết kế và mẫu nếu cần.

## Đóng góp
Đóng góp cho mẫu đều được chào đón. Vui lòng phân nhánh kho lưu trữ và gửi yêu cầu kéo.

## Giấy phép
Dự án này được cấp phép theo Giấy phép MIT - xem tệp LICENSE.md để biết chi tiết.

## Sự nhìn nhận
Đặc biệt cảm ơn tất cả những người đóng góp và duy trì Flask cũng như các tiện ích mở rộng của nó.