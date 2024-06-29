import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encryption(filepath, key):
    try:
        with open(filepath, 'rb') as f:
            img_data = f.read()
        iv = os.urandom(16)
        pad_img = pad(img_data, AES.block_size)
        cipher_obj = AES.new(key.encode(), AES.MODE_CBC, iv)
        encrypt_img = cipher_obj.encrypt(pad_img)
        with open("encrypted_" + filepath, 'wb') as f:
            f.write(iv + encrypt_img)
        return True
    except Exception as e:
        print(f"Encryption error: {e}")
        return False

def decryption(filepath, key):
    try:
        with open(filepath, 'rb') as f:
            encrypted_data = f.read()
        
        iv = encrypted_data[:AES.block_size]
        cipher_obj = AES.new(key.encode(), AES.MODE_CBC, iv)
        pad_img = cipher_obj.decrypt(encrypted_data[AES.block_size:])
        img_data = unpad(pad_img, AES.block_size)
        
        with open("decrypted_" + filepath, 'wb') as f:
            f.write(img_data)
        
        return True
    except Exception as e:
        print(f"Decryption error: {e}")
        return False
