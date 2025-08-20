import qrcode

url = 'https://it-2208.github.io/GTRALP/GTRALP002.html'
img = qrcode.make(url)
img.save('GTRALP/GTRALP002_qr.png')
