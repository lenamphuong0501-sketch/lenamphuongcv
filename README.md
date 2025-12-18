# Hướng dẫn: Trích xuất nội dung PDF vào `index.html`

Mục tiêu: trích xuất văn bản từ `pdf/Le-Nam-Phuong.pdf` và chèn vào trang chính `index.html`.

Files:
- `scripts/extract_pdf_to_html.py`: script Python để trích xuất và chèn nội dung.
- `requirements.txt`: dependencies.

Chạy:

PowerShell:
```powershell
python -m pip install -r requirements.txt
python scripts/extract_pdf_to_html.py
```

Kết quả: script sẽ tạo bản sao lưu `index.html.bak` và cập nhật phần "Về bản thân" chèn đoạn văn bản trích xuất từ PDF.
