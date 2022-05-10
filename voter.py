import uuid
import json
import global_file
from user import User
class Voter(User):
    def __init__(self, region):
        super().__init__()
        self.agent = None #agent.Agent()
        self.wallet = {}
        self.ballots = [] # token:ballot
        self.voting_status = {}
        self.region = region
        self.registration_status = False
        self.voting_credential = None
        self.signed_data = None
        self.current_vote = None
        self.ballot = None
        if region not in global_file.list_of_voters.keys():
            global_file.list_of_voters[region]=[self]
        else:
            global_file.list_of_voters[region].append(self)



    def send_id_registrar(self):
        data = {"id":self.id,"region":self.region}
        status,credential = global_file.list_of_registrars[self.region].receive_id(data)
        self.registration_status = status
        self.voting_credential = credential


    def send_token_request(self):
        data = {"id": self.id, "region": self.region, "voting_credential":self.voting_credential, "signature": self.signed_data}
        token = global_file.list_of_organizers[self.region].receive_token_request(data)
        print("Token Received is ",token)
        if token:
            if self.region in self.wallet.keys():
                self.wallet[self.region].append(token)
            else:
                self.wallet[self.region]=[token]


    def vote(self):
        self.send_token_request()
        ballot = json.loads(global_file.list_of_ballot[self.region].ballot_json)
        ballot['id'] = str(uuid.uuid4())
        candidates = global_file.list_of_candidates[self.region]
        for i in range(len(candidates)):
            print(f"Option - ({i+1}) - {candidates[i].alias} - {candidates[i].id}")
        choice = int(input("Enter Choice Number from Above"))
        candidate = candidates[choice - 1]
        print(f"Option Chosen is {candidate.alias} - {candidate.id}")
        if candidate in ballot['data'].keys():
            ballot['data'][str(candidate.id)]=True
        num=0
        for i in ballot['data'].keys():
            if ballot['data'][i]:
                num+=1
            if num>1:
                print("invalid ballot. More than 1 choices")
                return
        self.ballot=ballot.copy()
        token=self.wallet[self.region][-1]
        ballot['token']=token['token']
        ballot['index']=token['index']
        self.ballots.append(ballot)
        vote={'token':token['token'],'index': token['index'],'ballot':self.ballot}
        self.current_vote =vote
        self.split_vote()

    def split_vote(self):
        vote = self.current_vote
        ballot = vote['ballot']
        ballot_str=json.dumps(ballot)
        vote_str=str(vote['token'])+'@'+str(vote['index'])+'@'+str(ballot_str)
        list_counters = global_file.list_of_counters[self.region]
        parts = self.str_split(len(list_counters),vote_str)
        for i in range(len(list_counters)):
            list_counters[i].receive_vote_parts(vote['token'],vote['index'],i+1,parts[i])

    def ballot_to_string(self,ballot):
        '''res =""
        for item in ballot['data']:
            res += str(item.id)+ ":"+str(ballot['data'][item])+":"'''
        data = {}
        for item in ballot['data']:
            data[str(item.id)]=ballot['data'][item]
        res = json.dumps(data)
        return res

    def str_split(self,n,string):
        n_parts = len(string) // n + 1
        parts = [string[i:i + n_parts] for i in range(0, len(string), n_parts)]
        return parts

    def send_vote(self):
        pass

    def ack_vote(self):
        pass

    def __str__(self):
        return f"{self.alias}"
