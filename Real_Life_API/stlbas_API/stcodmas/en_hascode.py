import hashlib

def encrypt_string(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

hash_string = 'shifullah'

sha_signature = encrypt_string(hash_string)
#sha_signature = encrypt_string(hash_string, 'key')

print(sha_signature)



### C2C4A775CCACF3DF77B056D6F243E9EAA678D186A92C84D6A9D8FD085845114D
encrypt_text = "C2C4A775CCACF3DF77B056D6F243E9EAA678D186A92C84D6A9D8FD085845114D"
dycript = hashlib.sha256(encrypt_text.decode()).hexdigest()

print(dycript)