import json
import uuid

import global_file


class Ballot():
    def __init__(self,region,candidates):
        self.id = uuid.uuid4()
        self.region = region
        self.candidates = candidates #  expected list
        self.ballot_json = json.dumps(self.ballot_json_creator(self.candidates))
        global_file.list_of_ballot[self.region]=self
        print(self.ballot_json)

    def ballot_json_creator(self,candidates):
        json_data={}
        for i in candidates:
            json_data[str(i.id)]=None
        return {'id':None, 'data': json_data}

