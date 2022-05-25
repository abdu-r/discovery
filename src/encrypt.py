from cryptography.fernet import Fernet

# Generate key
def create_key():
    return Fernet.generate_key()

# Get key from filr
def get_key (key_file):
    with open(key_file, 'rb') as encrypt_key:
        key = encrypt_key.read()
    return key

# Save key
def save_key(key_file, key):
    with open(key_file, 'wb') as key_store:
        key_store.write(key)

# Encrypt file
def encrypt_file(key, file_name_to_encrypt, saved_file):
    f = Fernet(key)

    with open(file_name_to_encrypt, 'rb') as original_file:
        original = original_file.read()
    encrypted_file = f.encrypt(original)
  
    with open (saved_file, 'wb') as encrypted:
        encrypted.write(encrypted_file)

# Decrypt file
def decrypt_file(encryption_key, file_to_decrypt, plain_file):

    f = Fernet(encryption_key)
    with open(file_to_decrypt, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)
    with open(plain_file, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

if __name__ == "__main__":
   original_plain_file = 'data/best.csv'
   encryted_file_name = 'data/enc_best.csv'
   decryppted_file_name = 'data/best_dec.csv'
   key_file_name = 'data/enc.key'
  
   key = create_key()
   save_key(key_file_name, key)
   key = get_key(key_file_name)
   encrypt_file(key, original_plain_file, encryted_file_name)
   # decrypt_file(key, encryted_file_name, decryppted_file_name)
