import os
from cryptography.fernet import Fernet

# Generar la clave de cifrado
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Cargar la clave de cifrado
def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

# Cifrar una carpeta
def encrypt_folder(folder_path):
    key = load_key()
    fernet = Fernet(key)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as file_data:
                data = file_data.read()
            encrypted_data = fernet.encrypt(data)
            with open(file_path, "wb") as file_data:
                file_data.write(encrypted_data)

# Descifrar una carpeta
def decrypt_folder(folder_path):
    key = load_key()
    fernet = Fernet(key)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as file_data:
                data = file_data.read()
            decrypted_data = fernet.decrypt(data)
            with open(file_path, "wb") as file_data:
                file_data.write(decrypted_data)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 script.py [generate_key|encrypt_folder <folder_path>|decrypt_folder <folder_path>]")
        sys.exit(1)
    action = sys.argv[1]
    if action == "generate_key":
        generate_key()
    elif action.startswith("encrypt_folder"):
        folder_path = sys.argv[2]
        encrypt_folder(folder_path)
    elif action.startswith("decrypt_folder"):
        folder_path = sys.argv[2]
        decrypt_folder(folder_path)
    else:
        print("Invalid action. Please choose one of the following: generate_key, encrypt_folder, decrypt_folder")
        sys.exit(1)
