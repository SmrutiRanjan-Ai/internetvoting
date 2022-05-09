import uuid


class election():
    def __init__(self,organizers,counters,evaluators):
        self.id = uuid.uuid4()
        self.candidate_list=[]
        self.organizers = organizers
        self.counters = counters
        self.evaluators = evaluators
        self.result = None
        self.votes = []

    def receive_votes(self,votes):
        self.votes=votes