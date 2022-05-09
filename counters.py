import user
import global_file
class Counters(user.user):
    def __init__(self,region):
        super().__init__()
        self.votes={}
        self.region=None
        if self.region in global_file.counters.keys():
            global_file.counters[self.region].append(self)
        else:
            global_file.counters[self.region]=[]
            global_file.counters[self.region].append(self)

    def receive_vote_parts(self,token, index, serial, vote_parts):
        if token in self.votes.keys():
            if index in self.votes[token].keys():
                self.votes[token][index][serial]=vote_parts
            else:
                self.votes[token][index]={}
                self.votes[token][index]={serial:vote_parts}
        else:
            self.votes[token]={}
            self.votes[token][index]={serial:vote_parts}



    def send_votes_evaluator(self):
        evaluator=global_file.list_of_evaluators[self.region]
        for token in self.votes:
            evaluator.receive_votes(token, self.votes[token])


