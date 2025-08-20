import qrcode
import os

os.makedirs('GTRALP', exist_ok=True)

base_url = 'https://it-2208.github.io/'

for i in range(1, 16):  # 1 to 15 inclusive
    file_html = f'GTRALP/GTRALP{i:03}.html'      # GTRALP001.html etc.
    file_png = f'GTRALP/GTRALP{i:03}_qr.png'     # GTRALP001_qr.png etc.
    full_url = base_url + file_html
    img = qrcode.make(full_url)
    img.save(file_png)
    print(f'Generated QR for {full_url} -> {file_png}')
