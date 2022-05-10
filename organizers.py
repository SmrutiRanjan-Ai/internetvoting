import uuid

import global_file
import user

class Organizer(user.User):
    def __init__(self,region):
        super().__init__()
        self.region = region
        self.voter_data={}
        global_file.list_of_organizers[self.region] = self

    def receive_token_request(self, data):
        registrar = global_file.list_of_registrars[self.region]
        status = registrar.verify_voter(data)
        id = data['id']
        if status:
            if id in self.voter_data.keys():
                token = self.voter_data[id]
                token['index']+=1
                return token

            else:
                token_num = uuid.uuid4()
                index = 1
                token = {'token': token_num, 'index': index}
                self.voter_data[id]=token
                return token
    def __str__(self):
        return f"{self.alias}"

