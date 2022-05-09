import uuid
import names
import ecdsa

class user():
    def __init__(self):
        self.id = uuid.uuid4()
        self.alias = names.get_full_name()
        self.privatekey = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        self.publickey = self.privatekey.get_verifying_key()
