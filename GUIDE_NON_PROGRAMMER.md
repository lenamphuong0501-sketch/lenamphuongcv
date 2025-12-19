# Hướng dẫn chi tiết (Dành cho người không lập trình) — Web CV "Lê Nam Phương"

Mục tiêu: hướng dẫn từng bước để người không biết lập trình có thể tải, chỉnh sửa, chạy và xuất bản website CV này.

Tệp liên quan nhanh:
- `index.html` (file chính)
- `assets/img/mee.png` (ảnh đại diện)
- `pdf/Le-Nam-Phuong.pdf` (CV PDF)
- `assets/css/style-light.css`, `assets/css/style-dark.css` (style)
- `scripts/extract_pdf_to_html.py` (script trích pdf -> chèn vào HTML, tùy chọn)

1) Mở trang trên máy (không cần cài gì)

- Tải project (Download ZIP từ GitHub hoặc copy folder). Giữ nguyên cấu trúc thư mục.
- Mở thư mục project, bấm đúp `index.html` → trang sẽ mở trong trình duyệt.

Ghi chú: để trang hiển thị đúng, giữ nguyên cấu trúc thư mục (thư mục `assets`, `pdf`, `js`... phải nằm cạnh `index.html`).

2) Chỉnh nội dung cơ bản (tên, email, điện thoại, mô tả)

- Mở `index.html` bằng Notepad (Windows) hoặc Notepad++/VSCode nếu có.
- Sửa trực tiếp chữ trong các thẻ: `h1` (tên), block `profile_info` (số điện thoại, email), phần `section id="about"` (giới thiệu).
- Lưu file và refresh trình duyệt.

3) Thay ảnh cá nhân

- Ghi đè file `assets/img/mee.png` bằng ảnh mới có cùng tên, hoặc: sửa đường dẫn trong `index.html`.

4) Thay file CV (PDF)

- Ghi đè file `pdf/Le-Nam-Phuong.pdf` bằng CV của bạn. Link download trên trang sẽ vẫn hoạt động.

5) (Tùy chọn) Tự chèn nội dung PDF vào HTML

Nếu bạn muốn phần "Về bản thân" tự chèn đoạn tóm tắt từ file PDF, dùng script Python có sẵn.

Yêu cầu: cài Python 3.x

Các bước (Windows PowerShell):
```powershell
cd <đường dẫn tới thư mục project>
# cài dependencies 1 lần
python -m pip install -r requirements.txt
# chạy script để chèn nội dung PDF vào index.html
python scripts\extract_pdf_to_html.py
```

Script tạo bản sao lưu `index.html.bak` trước khi ghi đè.

6) Tải (đưa) project lên GitHub

6A) Upload bằng giao diện web (dễ, không cần Git):

- Tạo repository mới trên GitHub (đăng nhập → New repository).
- Vào repo → Add file → Upload files, kéo và thả toàn bộ thư mục con và file (hoặc nén thành ZIP rồi tải lên). Commit.

6B) Dùng Git (tự động hơn, 1 lần cài Git)

- Cài Git cho Windows: https://git-scm.com/downloads
- Mở PowerShell, điều hướng vào thư mục project rồi chạy:
```powershell
git init
git add .
git commit -m "Initial commit"
# Tạo repo trên GitHub (qua web) rồi copy URL HTTPS
git remote add origin https://github.com/USERNAME/REPO.git
git branch -M main
git push -u origin main
```

- Lưu ý: khi push HTTPS, Git sẽ yêu cầu Username và Password — Password ở đây là Personal Access Token (PAT) do GitHub cấp (tạo ở https://github.com/settings/tokens).

7) Triển khai (Deploy) — 2 cách phổ biến

7A) Vercel (dễ, tự động):

- Tạo tài khoản trên https://vercel.com, chọn "Import Git Repository", kết nối GitHub, chọn repo, bấm Deploy. Vercel sẽ build và cung cấp URL.

7B) GitHub Pages (đơn giản):

- Trong repo trên GitHub → Settings → Pages → Source: chọn branch `main` và folder `/ (root)` hoặc `/docs` nếu bạn đặt vào đó → Save. Sau vài phút site sẽ xuất hiện ở `https://<username>.github.io/<repo>`.

8) Thay đổi giao diện (ví dụ: căn giữa ảnh trên mobile)

- CSS chính nằm ở `assets/css/style-light.css` và `assets/css/style-dark.css`.
- Mở file style, tìm `@media (max-width: 480px)` và chỉnh `max-width` cho ảnh (`.about_me img.img-fluid`).

9) Một số lỗi & cách khắc phục nhanh

- Trang không hiển thị: chắc chắn bạn đang mở `index.html` từ thư mục gốc và giữ nguyên các thư mục `assets`, `pdf`, `scripts`.
- Ảnh bị lệch: mở DevTools (F12) → Elements → tìm `<img>` và kiểm tra xem có `position:absolute` hay `transform` nào đang ghi đè; nếu có, sửa trong `assets/css/style-light.css` (đã có phần override cho mobile).
- Muốn quay lại trước khi chạy script PDF: dùng `index.html.bak` (bản sao lưu được tạo khi chạy script).

10) Muốn trợ giúp trực tiếp?

- Gửi thông tin bạn muốn thay đổi (tên, email, ảnh, file PDF) và tôi sẽ hướng dẫn cụ thể từng bước hoặc giúp chỉnh và push thay bạn.

-- Hết --

File liên quan nhanh: `index.html`, `assets/img/mee.png`, `pdf/Le-Nam-Phuong.pdf`, `scripts/extract_pdf_to_html.py`, `requirements.txt`.

Nếu bạn muốn, tôi sẽ commit và push file hướng dẫn này lên repo.

End of guide.
