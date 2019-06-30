from Crypto.Cipher import AES


secret_key = 'shifullah1234567'   #'1234567890123456' # create new & store somewhere safe

cipher1 = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously

hex_code = "0e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f8de4434b2d0961f2dbc84b5380b0ccb809b6f22ca733d1dee5b0df19389f66bf06f441d737896a9c4bedf7eaa4c13ddd1"
new_rnd_bytes = bytes.fromhex(hex_code)
# print("hex to byte code: ", new_rnd_bytes)
# print(len(new_rnd_bytes))
# encoded_string = str(encoded)    #unicode(str, errors='replace')
# print(encoded_string)
# print(len(encoded_string))
print("********************************************************\n")

decoded = cipher1.decrypt(new_rnd_bytes)    #encoded
print("Decoded text is: ",decoded.strip().decode('utf-8'))
#print(decoded)