import uuid

import global_file
import user

class Registrars(user.User):
    def __init__(self,region):
        super().__init__()
        self.region = region
        self.voter_data={}
        global_file.list_of_registrars[self.region] = self

    def receive_id(self,data):
        credential = uuid.uuid4()
        self.voter_data [data['id']] = credential
        return True, credential
    def verify_voter(self,data):
        return True
