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

#msg = '{"HARCOD": "PEN", "SOFCOD": "002", "CODDES": "Deposite Instalment Due Change Cumalitiv", "CORCOD": "N", "AMOUNT": "100", "MANHRS": "100", "RTDNON": "1", "OPRSTAMP": "SYSTEM", "TIMSTAMP": "29-09-2016", "SECCOD": "Y", "ACTFLG": "Y", "SEQNUM": "100", "INTRT_CHGFLG": "", "REQUIRE_FLG": "", "ODRSRL": "100", "EFFDAT": "29-09-2016"}'
msg = '{"HARCOD": "ABC","SOFCOD": "999"}' #For GET Method
#msg = '{"HARCOD": "PEN","SOFCOD": "002"}' #For DELETE Method


msg_text = msg.rjust(512)
#print(msg_text)
secret_key = 'shifullah1234567'   #'1234567890123456' # create new & store somewhere safe

cipher1 = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
encoded = cipher1.encrypt(msg_text)
print("Encoded byte code: ",encoded)
print(len(encoded))
print("********************************************************\n")

encoded2 = encoded.hex()
print("converted hex code: ", encoded2)
print(len(encoded2))
#print("##################################################################################")
#print("Encoded String: ",encoded.decode("utf-8")) #'utf-8'
#print(type(encoded))
#encoded_text = str(encoded)
#print(type(encoded))
print("********************************************************\n")

    # my_hex_code = "0e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f80e50c33b9dc3cb909a33a0f86b74f7f81e5c83fc1efc32308b48483190ac5aa2a8e3fe6a021127219a0800f93d4897e9590423373c16728d6ccc23130f6747c5913c7e8bce5a279661fdc6c2d7cfb18b42af13f224dc43e6f1b523707f42e75944f257f0e91e663c6cc1210debfb15639c5940128688dc751cce2fae5e9de43397a6f5a190f7b09c9e310ab305311f5cda8f4974654adfacec3f87321d612f975cb7dd426fbb38178a4a2d85c9deede6e79ac4b0b53fbd678602707f9e7f1c0168609f0655367bd749d81d5c562b6527a572295e16fd77dfd9d45482e6946cadf795d053fdba7d4046a3ba10b2dcb591249abbe5925151f254cb65bf6a05b55229e7f0e79d789ea531d21b5810a29bb247948a35068c13c7e579583e5ded45f8ef80bf0163d2e14a7f45c598340cad19ea5410bec97fa329b5a9b44b8881948f14fb900ea0639a52f4522584230f48cc81d28ed97e875b7675b1ef449a5b71a4"
    # print(my_hex_code)
new_rnd_bytes = bytes.fromhex(encoded2)
print("hex to byte code: ", new_rnd_bytes)
print(len(new_rnd_bytes))
# encoded_string = str(encoded)    #unicode(str, errors='replace')
# print(encoded_string)
# print(len(encoded_string))
print("********************************************************\n")

decoded = cipher1.decrypt(new_rnd_bytes)    #encoded
print("Decoded text is: ",decoded.strip().decode('utf-8'))
#print(decoded)