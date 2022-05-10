import ecdsa
import hashlib
import global_file
import address_generator as ag
import json
class Agent():
    def __init__(self,alias,blockchain,type="holder",port=None):
        self.alias=alias
        self.port=port
        self.type=type
        sk=ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        vk=sk.get_verifying_key()
        self.keypairs={'sk':sk, 'pk': vk}
        self.address={}
        self.did=ag.address_generator(sk,vk)
        self.data={"name":"","age":None}
        self.signed_data= ''
        self.issuer=None
        self.issuer_pk=None
        self.data_approved=False
        self.connections= {}
        self.invitation=None
        self.pending_signed_data=None
        self.pending_data=None
        self.pending_holder=None
        self.blockchain=blockchain
        global_file.list_agents[self.alias] = self
        if self.type=='issuer':
            blockchain.add_to_chain(self.did,self.keypairs['pk'].to_string().hex())
        print(f"{self.alias} Agent Created with did:key:{self.did}")

    def create_invitation(self,type):
        self.invitation = {"alias": self.alias, "type":type , "did": self.did}

    def send_invitation(self,invitation,alias):
        global_file.list_agents[alias].receive_invitation(invitation)


    def receive_invitation(self,invitation):
        alias=invitation["alias"]
        did=invitation["did"]
        self.connections[alias]=did
        print(f"Connection between {alias} with did:key:{did} is established with {self.alias} with did:key:{self.did}")

    def update_data(self,name="name", age=21):
        self.data["name"]=name
        self.data["age"]=age

    def send_attributes(self,issuer):
        global_file.list_agents[issuer].receive_attributes(self.alias,self.data)

    def receive_attributes(self,holder,data):
        self.pending_holder = holder
        self.pending_data = data


    def check_attributes(self):
        data = self.pending_data
        holder = self.pending_holder
        print(f"{data} of {holder} checked.")
        sig = self.sign_attributes(data, self.keypairs['sk'])
        self.pending_signed_data = sig
        print("Digital Signature = ",self.pending_signed_data.hex())
        return True

    def sign_attributes(self,data,sk):
        message = json.dumps(data, indent=4)
        message = hashlib.sha256(message.encode())
        print("message is:", message.hexdigest())
        sig = sk.sign(bytes(message.hexdigest().encode()))
        return sig

    def send_credentials(self):
        global_file.list_agents[self.pending_holder].receive_credentials(self.alias,self.pending_signed_data,self.pending_data)


    def receive_credentials(self,issuer,signed_data,data):
        self.signed_data=signed_data
        self.issuer = issuer
        self.issuer_pk = global_file.list_agents[issuer].keypairs['pk']
        self.data=data

    def present_claim(self,verifier):
        if global_file.list_agents[verifier].receive_claim(self.alias,self.signed_data,self.data,self.issuer_pk,self.did):
            print(f"Claim {self.data} by did:peer:{self.did} Verified by {verifier}")
        else:
            print(f"Claim {self.data} by did:peer:{self.did} Rejected by {verifier}")

    def present_claim_data(self, verifier,name,age):
        data={}
        data["name"]=name
        data["age"]=age
        if global_file.list_agents[verifier].receive_claim(self.alias, self.signed_data, data, self.issuer_pk,
                                                           self.did):
            print(f"Claim {self.data} by did:peer:{self.did} Verified by {verifier}")
        else:
            print(f"Claim {self.data} by did:peer:{self.did} Rejected by {verifier}")

    def receive_claim(self,holder,signed_data,data,issuer_pk,holder_did):
        if self.blockchain.confirm_pk_in_chain(issuer_pk.to_string().hex()):
            if self.verify_claim(signed_data,data, issuer_pk):
                return True
            else:
                return False
        else:
            return False

    def verify_claim(self,signed_data,data,issuer_pk):
        message = json.dumps(data, indent=4)
        message = hashlib.sha256(message.encode())
        claim = issuer_pk.verify(signed_data, bytes(message.hexdigest().encode()))
        print(claim,"Signature verified of ", issuer_pk.to_string().hex())
        return claim








