# Image Security using Encryption


## Overview
This Flask-based web application enables secure image uploading, encryption, and decryption using AES (Advanced Encryption Standard) cryptography. Users can upload images, encrypt them with a user-provided key, and later decrypt them for download.


## Features
- **Image Upload**: Upload image files securely to the server.
- **AES Encryption**: Encrypt uploaded images using AES with a user-provided key.
- **AES Decryption**: Decrypt previously encrypted images with the corresponding key.
- **User Interface**: Intuitive web interface for easy interaction.


## Technologies Used
- **Framework**: Flask
- **Encryption**: PyCryptodome (Python Cryptographic Toolkit)
- **Forms Handling**: Flask-WTF
- **File Uploads**: Flask-Dropzone
- **Frontend**: HTML/CSS, JavaScript, Bootstrap 4


## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/kajalrawat3603/Image-Security-using-Encryption.git
   cd Image-Security-using-Encryption
   ```

2. **Create and Activate a Virtual Environment:**
     #### On Windows:
     ```bash
     python -m venv imgenv
     .\imgenv\Scripts\activate
     ```
  
     #### On macOS/Linux:
     ```bash
     python -m venv imgenv
     source imgenv/bin/activate
     ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python run.py
   ```

5. **Open your web browser and go to [http://localhost:5000](http://localhost:5000) to view the application.**

   
## Usage
   ### Upload Image
   1. Navigate to the upload page and select an image file.
   2. Click on the "Upload Image" button.
   
   ### Encrypt Image
   1. After uploading an image, navigate to the encryption page.
   2. Enter an encryption key (must be at least 16 characters long).
   3. Click on the "Encrypt Image" button to encrypt and download the image.
   
   ### Decrypt Image
   1. Upload an encrypted image.
   2. Go to the decryption page.
   3. Enter the decryption key used to encrypt the image.
   4. Click on the "Decrypt Image" button to decrypt and download the image.

