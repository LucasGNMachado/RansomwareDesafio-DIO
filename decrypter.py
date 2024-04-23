import os
import pyaes

## abrir arquivo criptografado

file_name = 'Coisas_impotantes.txt.ransomwaretroll'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## chave de descriptografia

Key = b'DPiuOllUQJBO00mk'
aes = pyaes.AESModeOfOperationCTR(Key)
decrypt)data = aes.decrypt(file_data)

## Remover o arquivo criptografado

os.remove(file_name)

## criar um novo arquivo descriptografado

new_file = 'Coisas_impotantes.txt'
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypt_data)
new_file.close()

