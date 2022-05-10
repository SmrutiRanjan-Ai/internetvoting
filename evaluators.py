import json

import global_file
import user
import random
import re
class Evaluator(user.User):
    def __init__(self,region,candidates):
        super().__init__()
        self.votes= {}
        self.region=region
        self.final_votes= {}
        self.serialized_votes={}
        self.finalized_votes={}
        self.results={}
        self.candidates=candidates
        for candidate in self.candidates:
            self.results[candidate.id]=0
        global_file.list_of_evaluators[self.region] = self


    def receive_votes(self,token,vote_parts):
        if token not in self.votes.keys():
            self.votes[token]=vote_parts
        else:
            for parts in vote_parts:
                self.votes[token].append(parts)

    def construct_votes(self):

        for token in self.votes:
            max_index = 0
            for vote_parts in self.votes[token]:
                print(vote_parts)
                max_index = max( vote_parts[0],max_index)
            votes=[]
            for vote_parts in self.votes[token]:
                if vote_parts[0] == max_index:
                    votes.append(vote_parts)
            vote = ''
            for part in votes:
                vote+=part[2]
            self.serialized_votes[token]=vote
        print("vote",self.serialized_votes)


    def finalize_votes(self):
        for token in self.serialized_votes:
            #max_index = max(self.serialized_votes[token],key=self.serialized_votes[token].get)
            #final_vote = self.serialized_votes[token][max_index]
            vote_string=self.serialized_votes[token]
            pattern = '@'
            result = re.split(pattern, vote_string)
            res = json.loads(result[2])
            self.finalized_votes[token]=res
        print("final",self.finalized_votes[token])

    def mixnet(self):
        items = list(self.finalized_votes.values())
        keys = list(self.finalized_votes.keys())
        random.shuffle(keys)
        for i in range(len(keys)):
            self.finalized_votes[keys[i]] = items[i]

    def final_results(self):
        for token in self.finalized_votes:
            ballot = self.finalized_votes[token]
            candidate_id=''
            for c in ballot['data']:
                if ballot['data'][c]:
                    candidate_id = c
            if candidate_id in self.results.keys():
                self.results[candidate_id]+=1
            else:
                self.results[candidate_id]=1
        max_value = max(self.results, key=self.results.get)

        winner=None
        for candidate in self.candidates:
            if str(candidate.id) == max_value:
                winner = candidate
                break

        print("Result is ",self.results)
        print("Result is ", max_value, winner)

    def __str__(self):
        return f"{self.alias}"


