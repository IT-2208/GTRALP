import qrcode
import os

base_url = 'https://it-2208.github.io/GTRALP/'

for i in range(1, 16):  # Loop from 1 to 15
    file_html = f'GTRALP{i:03}.html'           # e.g., GTRALP001.html
    file_png = f'GTRALP{i:03}_qr.png'          # e.g., GTRALP001_qr.png
    full_url = base_url + file_html
    img = qrcode.make(full_url)
    img.save(file_png)
    print(f'✅ QR generated for {full_url} → {file_png}')
