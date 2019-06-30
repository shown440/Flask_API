from Crypto.Cipher import AES

#msg = '{"HARCOD": "AAA", "SOFCOD": "997", "CODDES": "Deposite Instalment Due Change Cumalitiv", "CORCOD": "N", "AMOUNT": "", "MANHRS": "100", "RTDNON": "1", "OPRSTAMP": "SYSTEM", "TIMSTAMP": "29-09-2016", "SECCOD": "Y", "ACTFLG": "Y", "SEQNUM": "100", "INTRT_CHGFLG": "", "REQUIRE_FLG": "", "ODRSRL": "100", "EFFDAT": "29-09-2016"}'
msg = '{"HARCOD": "AAA","SOFCOD": "997"}' #For GET Method
#msg = '{"HARCOD": "PEN","SOFCOD": "002"}' #For DELETE Method


msg_text = msg.rjust(512)
#print(msg_text)
secret_key = 'shifullah1234567'   #'1234567890123456' # create new & store somewhere safe

cipher1 = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
encoded = cipher1.encrypt(msg_text)
# print("Encoded byte code: ",encoded)
# print(len(encoded))
print("********************************************************\n")

encoded2 = encoded.hex()
print("converted hex code: ", encoded2)
#print(len(encoded2))
#print("##################################################################################")
#print("Encoded String: ",encoded.decode("utf-8")) #'utf-8'
#print(type(encoded))
#encoded_text = str(encoded)
#print(type(encoded))
print("********************************************************\n")