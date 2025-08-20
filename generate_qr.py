import qrcode
import os

# GitHub Pages base URL
base_url = 'https://it-2208.github.io/GTRALP/'

# Generate QR for files GTRALP001.html to GTRALP015.html
for i in range(1, 16):
    filename = f'GTRALP{i:03}.html'
    output_image = f'GTRALP{i:03}_qr.png'
    url = base_url + filename
    img = qrcode.make(url)
    img.save(output_image)
    print(f"✅ QR generated for {url} → {output_image}")
 
