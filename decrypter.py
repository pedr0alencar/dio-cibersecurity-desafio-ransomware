from cryptography.fernet import Fernet
import os

# Ler a chave salva
key_file = "key.key"
with open(key_file, "rb") as keyfile:
    key = keyfile.read()

# Criar objeto de criptografia
cipher = Fernet(key)

# Nome do arquivo criptografado
encrypted_file = "teste.txt.enc"
decrypted_file = "teste.txt"

# Ler o conteúdo criptografado
with open(encrypted_file, "rb") as file:
    encrypted_data = file.read()

# Descriptografar os dados
decrypted_data = cipher.decrypt(encrypted_data)

# Escrever o conteúdo descriptografado no novo arquivo
with open(decrypted_file, "wb") as file:
    file.write(decrypted_data)

# Remover o arquivo criptografado (opcional)
os.remove(encrypted_file)

print(f"Arquivo descriptografado salvo como: {decrypted_file}")
