# from Crypto.Cipher import AES
# import base64

# msg_text = 'shifullah'
# secret_key = '1234567890123456' # create new & store somewhere safe

# #msg_text = msg_text.encode('base64','strict')
# enc_msg = base64.b64encode(bytes(msg_text, 'utf-8'))

# print("Encoded txt: ",enc_msg)
# print(type(enc_msg))

# print("Decoded String: " + base64.b64decode(enc_msg.decode('utf-8')))
# print(type(enc_msg.decode('utf-8')))
# encoded_text = str(encoded)
# print(type(encoded))

# decoded = cipher.decrypt(base64.b64decode(encoded))
# print("Decoded text is: ",decoded.strip())
#print(decoded)

##################################################################################################################

# from Crypto.Cipher import AES
# import base64

# msg = '{"name": "SHIFULLAH","designation": "VP","manager_id": "7839","date_of_birth": "16-03-1988","salary": "5000","commission": "2000","department_no": "10"}'

# msg_text = msg.rjust(1600)
# secret_key = '1234567890123456' # create new & store somewhere safe

# cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
# encoded = base64.b64encode(cipher.encrypt(msg_text))
# print("Encoded txt: ",encoded)
# print(type(encoded))
# encoded_text = str(encoded)
# print(type(encoded))

# decoded = cipher.decrypt(base64.b64decode(encoded))
# print("Decoded text is: ",decoded.strip().decode('utf-8'))
# print(decoded)

#################################################################################################

from Crypto.Cipher import AES
#import base64

msg = '{"name": "SHIFULLAH","designation": "VP","manager_id": "7839","date_of_birth": "16-03-1988","salary": "5000","commission": "2000","department_no": "10"}'

msg_text = msg.rjust(512)
#print(msg_text)
secret_key = 'shifullah1234567'   #'1234567890123456' # create new & store somewhere safe

cipher1 = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
encoded = cipher1.encrypt(msg_text)
print("Encoded txt: ",encoded)
print(len(encoded))
print("********************************************************\n")

encoded2 = encoded.hex()
print("encoded2 : ", encoded2)
print(len(encoded2))
#print("##################################################################################")
#print("Encoded String: ",encoded.decode("utf-8")) #'utf-8'
#print(type(encoded))
#encoded_text = str(encoded)
#print(type(encoded))
print("********************************************************\n")

new_rnd_bytes = bytes.fromhex(encoded2)
print("new_rnd_bytes : ", new_rnd_bytes)
print(len(new_rnd_bytes))
# encoded_string = str(encoded)    #unicode(str, errors='replace')
# print(encoded_string)
# print(len(encoded_string))
print("********************************************************\n")

decoded = cipher1.decrypt(new_rnd_bytes)    #encoded
print("Decoded text is: ",decoded.strip().decode('utf-8'))
#print(decoded)