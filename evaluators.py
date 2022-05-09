import user
class evaluator(user.user):
    def __init__(self):
        super().__init__()
        self.votes= {}
        self.region=None
        self.final_votes=[]


    def receive_votes(self,token,vote_parts):
        if token not in self.votes.keys():
            self.votes[token]=vote_parts
        else:
            self.votes[token].append(vote_parts)

    def arrange_votes(self):