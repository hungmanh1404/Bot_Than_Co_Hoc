# 🚀 Hướng Dẫn Deploy Lên Render.com

## Bước 1: Chuẩn bị GitHub Repository

### 1.1. Push code lên GitHub

Đã hoàn thành:
```bash
git init
git add .
git commit -m "init source"
```

Tiếp tục:
```bash
# Đổi branch sang main (nếu đang ở master)
git branch -M main

# Thêm remote repository (thay YOUR_USERNAME và YOUR_REPO)
git remote add origin https://github.com/YOUR_USERNAME/tuongphongthuy.git

# Push lên GitHub
git push -u origin main
```

---

## Bước 2: Tạo Web Service Trên Render.com

### 2.1. Đăng nhập Render
1. Truy cập [https://render.com](https://render.com)
2. Đăng nhập bằng GitHub account

### 2.2. Tạo Web Service Mới
1. Click nút **"New +"** ở góc trên bên phải
2. Chọn **"Web Service"**
3. Connect GitHub repository `tuongphongthuy`
4. Click **"Connect"**

### 2.3. Cấu hình Service

Điền thông tin như sau:

| Field | Value |
|-------|-------|
| **Name** | `tuongphongthuy` (hoặc tên bạn muốn) |
| **Region** | Singapore (gần VN nhất) |
| **Branch** | `main` |
| **Root Directory** | (để trống) |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `python main.py` |
| **Instance Type** | **Free** |

### 2.4. Thêm Environment Variables

Scroll xuống phần **Environment Variables**, click **"Add Environment Variable"**:

| Key | Value |
|-----|-------|
| `TELEGRAM_BOT_TOKEN` | `8246910964:AAHaIYkqy9pWwnDEXP5VBmNXU4WDhn7udRA` |
| `TELEGRAM_CHAT_ID` | `8270116773` |
| `USER_BIRTH_DAY` | `14` |
| `USER_BIRTH_MONTH` | `4` |
| `USER_BIRTH_YEAR` | `2001` |
| `USER_ELEMENT` | `Kim` |
| `USER_BRANCH` | `Tỵ` |
| `SCHEDULE_HOUR` | `20` |
| `TIMEZONE` | `Asia/Ho_Chi_Minh` |
| `PORT` | `8080` |

> **Lưu ý**: Render tự động set `PORT`, nhưng để chắc chắn thì add vào.

### 2.5. Deploy

1. Click **"Create Web Service"**
2. Đợi 3-5 phút để build và deploy
3. Xem logs để kiểm tra

---

## Bước 3: Kiểm Tra Bot Hoạt Động

### 3.1. Xem Logs

Trong Render dashboard:
- Click vào service `tuongphongthuy`
- Tab **"Logs"** → xem logs real-time

**Logs thành công sẽ hiện**:
```
✅ All services started successfully!
📅 Daily forecasts will be sent at 20:00 Asia/Ho_Chi_Minh
🤖 Bot is ready to receive commands
```

### 3.2. Lấy URL của Bot

Sau khi deploy xong, URL sẽ có dạng:
```
https://tuongphongthuy.onrender.com
```

Copy URL này để dùng cho bước tiếp theo.

### 3.3. Test Health Endpoint

Mở browser, truy cập:
```
https://tuongphongthuy.onrender.com/health
```

Sẽ thấy response:
```json
{
  "status": "healthy",
  "service": "Thiên Cơ Đại Tướng Quân",
  "version": "1.0.0"
}
```

### 3.4. Test Telegram Bot

1. Mở Telegram
2. Tìm bot của bạn
3. Gửi `/start`
4. Thử `/dubao 09/01/2026`

---

## Bước 4: ⚠️ QUAN TRỌNG - Setup Anti-Sleep

**Vấn đề**: Render free tier sẽ **tự động sleep** sau 15 phút không có request.

**Giải pháp**: Ping health endpoint mỗi 10 phút để giữ bot luôn thức.

### Cách 1: Dùng Cron-Job.org (Khuyến nghị - MIỄN PHÍ)

#### 4.1. Đăng ký Cron-Job.org
1. Truy cập [https://cron-job.org](https://cron-job.org)
2. Tạo tài khoản miễn phí
3. Verify email

#### 4.2. Tạo Cron Job
1. Click **"Create cronjob"**
2. Điền thông tin:

| Field | Value |
|-------|-------|
| **Title** | `Keep Tuongphongthuy Awake` |
| **URL** | `https://tuongphongthuy.onrender.com/health` |
| **Schedule** | `Every 10 minutes` (click vào calendar icon) |
| **Execution** | `Use standard cron job execution` |
| **Notifications** | Bỏ check (không cần) |

3. Click **"Create"**

#### 4.3. Verify

Sau 10 phút, quay lại cron-job.org:
- Tab **"History"** → sẽ thấy các lần ping thành công (status 200)

---

### Cách 2: Chạy Script Python Riêng (Nếu có VPS/máy tính luôn bật)

Đã có sẵn file `keep_awake.py`, chạy như sau:

#### 4.1. Sửa URL trong script
```bash
nano keep_awake.py
```

Đổi dòng:
```python
BOT_URL = "https://tuongphongthuy.onrender.com"  # Thay bằng URL thực của bạn
```

#### 4.2. Chạy script
```bash
# Activate venv
source venv/bin/activate

# Run keep-awake service
python keep_awake.py
```

Script sẽ ping health endpoint mỗi 10 phút.

> **Nhược điểm**: Phải giữ máy tính/VPS luôn chạy.

---

### Cách 3: Dùng UptimeRobot (Miễn phí, dễ dùng)

1. Truy cập [https://uptimerobot.com](https://uptimerobot.com)
2. Tạo tài khoản free
3. **Add New Monitor**:
   - Monitor Type: `HTTP(s)`
   - Friendly Name: `Tuongphongthuy Bot`
   - URL: `https://tuongphongthuy.onrender.com/health`
   - Monitoring Interval: `Every 5 minutes` (free tier)
4. Create Monitor

---

## Bước 5: Verify Hoạt Động 24/7

### 5.1. Kiểm tra sau 1 giờ
- Vào Render logs → xem bot còn hoạt động không
- Gửi `/start` trên Telegram → phải phản hồi ngay

### 5.2. Kiểm tra lúc 8:00 PM
- Vào ngày hôm sau, lúc 8:00 PM, kiểm tra Telegram
- Phải nhận được tin tự động dự báo cho ngày mai

### 5.3. Monitoring
- Render Dashboard → xem CPU/Memory usage
- Logs → kiểm tra có lỗi gì không

---

## Troubleshooting

### ❌ Bot không phản hồi Telegram
**Nguyên nhân**: 
- `TELEGRAM_BOT_TOKEN` sai
- Bot bị sleep

**Giải pháp**:
1. Kiểm tra token trong Render env vars
2. Ping `/health` endpoint → nếu OK thì bot vẫn sống
3. Xem logs để tìm lỗi

---

### ❌ Bot bị sleep liên tục
**Nguyên nhân**: Chưa setup anti-sleep

**Giải pháp**:
- Setup cron-job.org như Bước 4
- Verify trong History của cron-job

---

### ❌ Không nhận tin tự động lúc 8 PM
**Nguyên nhân**:
- Timezone sai
- Scheduler chưa khởi động

**Giải pháp**:
1. Kiểm tra env var `TIMEZONE=Asia/Ho_Chi_Minh`
2. Xem logs lúc 8 PM → phải thấy "Generating forecast for..."

---

### ❌ Logs hiện lỗi "Module not found"
**Nguyên nhân**: Dependencies chưa cài

**Giải pháp**:
- Kiểm tra `Build Command`: `pip install -r requirements.txt`
- Re-deploy lại: Manual Deploy → Deploy latest commit

---

## Summary Checklist

- [ ] Push code lên GitHub
- [ ] Tạo Web Service trên Render
- [ ] Add Environment Variables (10 biến)
- [ ] Deploy và xem logs thành công
- [ ] Test `/health` endpoint
- [ ] Test Telegram bot (`/start`, `/dubao`)
- [ ] Setup anti-sleep (cron-job.org)
- [ ] Verify bot không bị sleep sau 1 giờ
- [ ] Đợi đến 8 PM kiểm tra tin tự động

---

## 🎯 Kết luận

Sau khi hoàn thành các bước trên:
- ✅ Bot sẽ chạy 24/7 trên cloud
- ✅ Tự động gửi dự báo mỗi ngày lúc 8 PM
- ✅ Không bị sleep nhờ cron job
- ✅ Hoàn toàn MIỄN PHÍ

**Enjoy your mystical bot!** 🔮✨
