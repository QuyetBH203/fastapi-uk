# FastAPI UK Project

## Cấu hình môi trường

Dự án sử dụng Pydantic BaseSettings để quản lý cấu hình từ biến môi trường. Bạn có thể cấu hình ứng dụng bằng cách:

1. Tạo file `.env` ở thư mục gốc của dự án
2. Thiết lập các biến môi trường trong hệ thống

### File .env mẫu

```
# Application Environment
ENV=local

# Application Settings
DEBUG=true
APP_HOST=0.0.0.0
APP_PORT=8000

# Database Settings
WRITER_DB_URL=mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi
READER_DB_URL=mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi

# Authentication
JWT_SECRET_KEY=your_secure_jwt_key_here
JWT_ALGORITHM=HS256

# Services
SENTRY_SDN=
CELERY_BROKER_URL=amqp://user:bitnami@localhost:5672/
CELERY_BACKEND_URL=redis://:password123@localhost:6379/0
REDIS_HOST=localhost
REDIS_PORT=6379

# Test Environment Specific
TEST_WRITER_DB_URL=mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi_test
TEST_READER_DB_URL=mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi_test

# Production Environment Specific
PROD_DEBUG=false
```

### Cách hoạt động

1. Biến môi trường `ENV` xác định môi trường đang chạy (`local`, `test`, hoặc `prod`)
2. Mỗi môi trường có thể có tiền tố riêng cho biến môi trường:
   - Môi trường test: `TEST_`
   - Môi trường local: `LOCAL_`
   - Môi trường production: `PROD_`

3. Ví dụ:
   - Nếu `ENV=test`, biến `TEST_WRITER_DB_URL` sẽ ghi đè lên giá trị mặc định của `WRITER_DB_URL`
   - Nếu `ENV=prod`, biến `PROD_DEBUG` sẽ ghi đè lên giá trị mặc định của `DEBUG`

### Sử dụng trong code

```python
from core.config import config

# Sử dụng cấu hình
debug_mode = config.DEBUG
database_url = config.WRITER_DB_URL
```
