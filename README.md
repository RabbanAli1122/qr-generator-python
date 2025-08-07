# 📦 Python QR Code Generator

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

This Python-based project allows you to generate both simple and advanced customizable QR codes using the `qrcode` and `PIL` libraries. With just a few lines of code, you can encode URLs or text into a scannable image. Customize the colors, box size, and border to suit your needs.


## ✅ Features

1. Generate QR codes from URLs or text using Python.
2. Two versions included:
   - **Simple QR Code Generator** (minimal code)
   - **Advanced Custom QR Code Generator** with full control over:
     - Pattern and background color
     - Border size
     - Box size
3. Resulting QR codes are compatible with most standard scanner apps.
4. Easy to customize with just a few code changes.


## 🧠 How It Works
## ▶️ Simple QR Code Generator
This version uses only the `qrcode` library and generates a basic black-and-white QR code with default settings.

### How It Works:
- Import the qrcode library.
- Add the data (URL or text).
- Save the image with a desired filename.

```
import qrcode as qr
image = qr.make("https://github.com/RabbanAli1122")
image.save("python.png")
```


## 🎨 Advanced QR Code Customization
This version uses both the qrcode and PIL libraries to allow for more control over QR code styling.
```
import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=6,
    box_size=10,
    border=10
)
qr.add_data("https://github.com/RabbanAli1122")
qr.make(fit=True)

img = qr.make_image(fill_color="white", back_color="black")
img.save("python_20_projects.png")
```

### 🔹 Key Customizations:

- version: QR complexity (higher means more data).
- box_size: Size of each square box.
- border: Width of border (in boxes).
- fill_color & back_color: Customize foreground/background color.

### 🧰 Requirements
Make sure you have Python installed, then install the required libraries:
```
pip install qrcode
pip install pillow
```


### 🚀 How to Run
1. Clone this repository:
```
git clone https://github.com/RabbanAli1122/Python-QR-Code-Generator.git
cd Python-QR-Code-Generator
```
2. Run the desired Python file:
- python simple_qr.py      # for basic version
- python custom_qr.py      # for advanced version

  
## 🧠 Lessons Learned
- Learned how to use the qrcode library to generate QR codes.
- Discovered how to customize QR code design using the PIL library.
- Explored parameter control to modify QR code size, color, and structure.

## 📜 License
This project is licensed under the MIT License.
See the LICENSE file for details.
