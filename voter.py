import global_file
from user import user
class Voter(user):
    def __init__(self, region):
        super().__init__()
        self.agent = None #agent.Agent()
        self.wallet = {}
        self.ballots = {} # token:ballot
        self.voting_status = {}
        self.region = region
        self.registration_status = False
        self.voting_credential = None
        self.signed_data = None
        self.current_vote = None
        self.ballot = None

    def send_id_registrar(self):
        data = {"id":self.id,"region":self.region}
        status,credential = global_file.list_of_registrars[self.region].receive_id(data)
        self.registration_status = status
        self.voting_credential = credential


    def send_token_request(self):
        data = {"id": self.id, "region": self.region, "voting_credential":self.voting_credential, "signature": self.signed_data}
        token = global_file.list_of_organizers[self.region].receive_token_request(data)

        if token:
            if self.region in self.wallet.keys():
                self.wallet[self.region].append(token)
            else:
                self.wallet[self.region]=[]
                self.wallet[self.region].append(token)


    def vote(self,candidate):
        if candidate in self.ballot.keys():
            self.compile_vote(candidate)


    def compile_vote(self,candidate):
        ballot = global_file.list_of_ballot[self.region]
        ballot = ballot.copy()
        ballot[candidate]=True
        num=0
        for i in ballot.keys():
            if ballot[i]:
                num+=1
            if num>1:
                print("invalid ballot. More than 1 choices")
                return
        token=self.wallet[self.region][-1]
        self.ballots[token]=ballot
        vote={'token':token,'index': token['index'],'ballot':ballot}
        self.current_vote =vote

    def split_vote(self):
        vote = self.current_vote
        ballot = vote['ballot']
        ballot_str=self.ballot_to_string(ballot)
        vote_str='token:'+str(vote['token'])+'index:'+str(vote['index'])+'ballot:'+str(ballot_str)
        list_counters = global_file.list_of_counters[self.region]
        parts = self.str_split(len(list_counters),vote_str)
        for i in range(len(list_counters)):
            list_counters[i].receive_vote_parts(vote['token'],i,parts[i])


    def ballot_to_string(self,ballot):
        res =""
        for item in ballot:
            res += item + str(ballot[item])
        return str(res)

    def str_split(self,n,string):
        n_parts = len(string) // n + 1
        parts = [string[i:i + n_parts] for i in range(0, len(string), n_parts)]
        return parts

    def send_vote(self):
        pass

    def ack_vote(self):
        pass
