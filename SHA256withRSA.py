import json
import hashlib

from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256 

def sign_data(data, private_key_path): 
    serialized_data = json.dumps(data, sort_keys=True).encode('utf-8') 
    
    hash_value = hashlib.sha256(serialized_data).digest() 
    
    # with open('private_key.pem', 'wb') as f:
    #     f.write(RSA.export_key('PEM'))
    
    with open(private_key_path, 'r') as f: 
        private_key = RSA.import_key(f.read()) 
        
    
    signer = pkcs1_15.new(private_key) 
    
    signature = signer.sign(SHA256.new(hash_value)) 
    
    return signature 

json_data = {
    "Message": "Hello World"
}

private_key_path='private_key.pem' 

signature = sign_data(json_data, private_key_path) 
json_data['signature'] = signature.hex() 

print(json_data)