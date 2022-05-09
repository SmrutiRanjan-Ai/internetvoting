import uuid


class ballot():
    def __init__(self,candidates):
        self.id = uuid.uuid4()
        self.candidates = candidates #  expected list
        self.ballot_json = self.ballot_json_creator(self.candidates)

    def ballot_json_creator(self,candidates):
        json_data={}
        for i in candidates:
            json_data[i]=None
        return json_data

