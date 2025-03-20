from cryptography.fernet import Fernet

# Gerar e salvar a chave
key_file = "key.key"
try:
    with open(key_file, "rb") as keyfile:
        key = keyfile.read()
except FileNotFoundError:
    key = Fernet.generate_key()
    with open(key_file, "wb") as keyfile:
        keyfile.write(key)

# Criar objeto de criptografia
cipher = Fernet(key)

# Nome do arquivo a ser criptografado
file_name = "teste.txt"
encrypted_file = file_name + ".enc"

# Ler o conteúdo do arquivo original
with open(file_name, "rb") as file:
    file_data = file.read()

# Criptografar os dados
encrypted_data = cipher.encrypt(file_data)

# Escrever o conteúdo criptografado no novo arquivo
with open(encrypted_file, "wb") as file:
    file.write(encrypted_data)

# Remover o arquivo original (opcional)
import os
os.remove(file_name)

print(f"Arquivo criptografado salvo como: {encrypted_file}")
