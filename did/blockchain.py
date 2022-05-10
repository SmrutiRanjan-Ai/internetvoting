

import hashlib
import proof as p
import block as b

class Blockchain:
    def __init__(self):
        self.blockchain = []

    def ps_create_block(self,data):
        if self.blockchain:
            prev_block=self.blockchain[-1]
            prev_hash = prev_block.header['prev_hash']
        else:
            prev_hash="0"

        block= b.Block(prev_hash,data)
        p.proof_of_work(block)
        self.blockchain.append(block)

    def add_to_chain(self,did,pk):
        data={}
        data['did']=did
        data['pk']=pk
        self.ps_create_block(data)
        return

    def confirm_pk_in_chain(self,pk):
        for i in self.blockchain:
            if 'pk' in i.data.keys():
                if i.data['pk']==pk:
                    print('pk found ',i.data['pk'],'added by did:key:',i.data['did'])
                    print('txn:',i.data)
                    print('block data:', i.header)
                    return True
        return False

    def query_blockchain(self):
        for i in self.blockchain:
            print('block data:', i.header)
            print('txn:', i.data)

