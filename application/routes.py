from flask import render_template, request, redirect, url_for, send_file, session
from werkzeug.utils import secure_filename
import os
from .form import EncryptionForm,UploadImagePath,DecryptionForm
from application import app
import secrets
from flask import session
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from flask import send_file

upload_image_path = UploadImagePath()
secret_key = secrets.token_hex(16)
print("Generated Secret Key:", secret_key)
app.secret_key = secret_key

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        if "file" not in request.files:
            print("No file part")
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            print("No selected file")
            return redirect(request.url)
        
        try:
            f = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOADED_PATH"], f)
            file.save(filepath)
            upload_image_path.path = filepath
            session['filename'] = f
            print("File saved successfully:", filepath)
        except Exception as e:
            print("Error saving file:", e)
            return redirect(request.url)
        return redirect(url_for("upload"))
    
    return render_template("upload.html")


@app.route("/encryption", methods=["GET", "POST"])
def encryption():
    form = EncryptionForm()
    error_key = False
    error_message = None 
    if request.method == "POST":
        key = form.encryption_key.data.encode("utf-8")
        filename = session.get("filename")
        if not filename:
            error_no_file = True
            return render_template("encryption.html", form=form, error_no_file=error_no_file)
        filepath = os.path.join(app.config["UPLOADED_PATH"], filename)
        
        try:
            with open(filepath, 'rb') as f:
                img_data = f.read()
                if len(img_data) == 0:
                    raise ValueError("Image file is empty")

                iv = os.urandom(16)
                pad_img = pad(img_data, AES.block_size)
                cipher_obj = AES.new(key, AES.MODE_CBC, iv)
                encrypt_img = cipher_obj.encrypt(pad_img)
            with open(filepath, 'wb') as f:
                f.write(iv + encrypt_img)
            print("Done", "Successfully Encrypted Image...")

            return send_file(filepath, as_attachment=True)
        except ValueError as e:
            error_key = True
            error_message = str(e) 
            return render_template("encryption.html", form=form, error_key=error_key, error_message=error_message)
    return render_template("encryption.html", form=form)


# Route for decryption page
@app.route("/decryption", methods=["GET", "POST"])
def decryption():
    form = DecryptionForm()
    if request.method == "POST":
        key = form.decryption_key.data.encode('utf-8')
        filename = session.get("filename")
        if not filename:
            print("Invalid file")
            return redirect(url_for("upload"))

        filepath = os.path.join(app.config["UPLOADED_PATH"], filename)

        try:
            with open(filepath, 'rb') as f:
                encrypted_data = f.read()
                if len(encrypted_data) == 0:
                    raise ValueError("Encrypted file is empty")

                iv = encrypted_data[:AES.block_size]
                cipher_obj = AES.new(key, AES.MODE_CBC, iv)
                pad_img = cipher_obj.decrypt(encrypted_data[AES.block_size:])
                img_data = unpad(pad_img, AES.block_size)
            with open(filepath, 'wb') as f:
                f.write(img_data)
            print("Done", "Successfully Decrypted Image...")
            return send_file(filepath, as_attachment=True)
        except Exception as e:
            print(f"Decryption error: {str(e)}")
            return redirect(url_for("decryption"))
    return render_template("decryption.html", form=form)


