import global_file
import user
import random
class evaluator(user.user):
    def __init__(self,candidates):
        super().__init__()
        self.votes= {}
        self.region=None
        self.final_votes= {}
        self.serialized_votes={}
        self.finalized_votes={}
        self.results={}
        self.candidates=candidates
        for candidate in self.candidates:
            self.results[candidate]=0


    def receive_votes(self,token,vote_parts):
        if token not in self.votes.keys():
            self.votes[token]=vote_parts
        else:
            self.votes[token].append(vote_parts)

    def construct_votes(self):
        for token in self.votes:
            for index in self.votes[token]:
                vote_parts = self.votes[token][index]
                vote=''
                for i in range(global_file.n):
                    vote+=vote_parts[i+1]
                self.serialized_votes[token][index]=vote

    def finalize_votes(self):
        for token in self.serialized_votes:
            max_index = max(self.serialized_votes[token],key=self.serialized_votes[token].get)
            final_vote = self.serialized_votes[token][max_index]
            self.finalized_votes[token]=final_vote

    def mixnet(self):
        items = list(self.finalized_votes.values())
        keys = list(self.finalized_votes.keys())
        random.shuffle(keys)
        for i in range(len(keys)):
            self.finalized_votes[keys[i]] = items[i]

    def final_results(self):
        for token in self.finalized_votes:
            candidate = self.finalized_votes[token]
            if candidate in self.results.keys():
                self.results[candidate]+=1
        max_value = max(self.results, key=self.results.get)
        print(self.results)
        print("Result is ",max_value)



