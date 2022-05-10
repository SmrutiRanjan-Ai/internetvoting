import user
import global_file
class Counters(user.User):
    def __init__(self,region):
        super().__init__()
        self.votes={}
        self.region=region
        if self.region in global_file.list_of_counters.keys():
            global_file.list_of_counters[self.region].append(self)
        else:
            global_file.list_of_counters[self.region]=[self]


    def receive_vote_parts(self,token, index, serial, vote_parts):
        if token not in self.votes.keys():
            self.votes[token] = [(index, serial, vote_parts)]
        else:
            self.votes[token].append((index, serial, vote_parts))




    def send_votes_evaluator(self):
        evaluator=global_file.list_of_evaluators[self.region]
        for token in self.votes:
            evaluator.receive_votes(token, self.votes[token])

    def __str__(self):
        return f"{self.alias}"
