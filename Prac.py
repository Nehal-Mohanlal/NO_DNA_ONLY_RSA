from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256  

#public_key, private_key = RSA.newkeys(1024) 
# key = RSA.generate(2048) 
# with open("public.pem", "wb") as f: 
#     f.write(public_key.save_pkcs1("PEM")) 
    
# with open("private.pem", "wb") as f: 
# #     f.write(private_key.save_pkcs1("PEM")) 

# with open('private_key.pem', 'wb') as f:
#     f.write(key.export_key('PEM'))
# with open("public.pem", "rb") as f: 
#     public_key = RSA.PublicKey.load_pkcs1(f.read()) 
    

# with open("private.pem", "rb") as f: 
#     private_key = RSA.PrivateKey.load_pkcs1(f.read()) 


# message = "Hello World"
# en_message = rsa.encrypt(message.encode(), public_key) 

# print(en_message)
# print("------------------------------------------------")
# dec_message = rsa.decrypt(en_message, private_key) 

# print(dec_message.decode())
    


# with open("public_key.pem", "wb") as f: 
#     f.write(public_key.save_pkcs1("PEM")) 
    
# with open("private_key.pem", "wb") as f: 
#     f.write(public_key.save_pkcs1("PEM")) 

key = RSA.generate(2048)
private_key = key.export_key()
with open("private_key.pem", "wb") as private_key_file:
    private_key_file.write(private_key)

# Export public key
public_key = key.publickey().export_key()
with open("public_key.pem", "wb") as public_key_file:
    public_key_file.write(public_key)