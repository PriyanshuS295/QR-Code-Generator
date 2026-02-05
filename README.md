# QR-Code-Generator
📌 QR Code Generator

A simple Python-based QR Code Generator that creates a QR code image from any user-provided link or text. The generated QR code is saved locally as a .png file with a custom name.

This project is beginner-friendly and demonstrates basic usage of external Python libraries, user input handling, and file generation.

🚀 Features

Generate QR codes for any link or text

Save QR code as a PNG image

Custom filename support

Simple and lightweight

Runs directly from the terminal

🛠️ Technologies Used

Python

qrcode library

Pillow (PIL) (dependency used internally by qrcode)

🔧 Installation & Setup

Clone the repository

git clone https://github.com/your-username/QR-Code-Generator.git


Navigate to the project directory

cd QR-Code-Generator


Install required library

pip install qrcode[pil]

▶️ How to Run the Project

Run the Python file:

python qr_generator.py


Enter the link or text when prompted:

Please provide the link:


Enter the name for the QR code image:

Write the name by which you want to save:


The QR code will be saved as:

your_filename.png

📸 Output Example

Input: https://www.google.com

Output: google_qr.png
