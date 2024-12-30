import os
import pyaes

#abrir o arquivo criptografado

file_name = "texto-teste.txt.ransomwaretroll"
file = open(file_name, "rb")
file_data = file.read()
file.close()

#chave de descriptografia

key = b"testeransomware"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

#remover o arquivo criptografado
os.remove(file.name)

#criar um novo arquivo descriptografado

new_file = "texto-teste.txt"
new_file = open(f"{new_file}", "mb")
new_file.write(decrypt_data)
new_file.close()