import ecdsa
import hashlib
sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
vk = sk.get_verifying_key()
public_key=vk.to_string().hex()
message='hello'
message=hashlib.sha256(message.encode())
print(message.hexdigest())
sig = sk.sign(bytes(message.hexdigest().encode()))
print(vk.verify(sig, bytes(message.hexdigest().encode())))



#print(bytes.fromhex(ok))
