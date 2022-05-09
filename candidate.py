import user
class candidate(user.user):
    def __init__(self, election_id):
        super().__init__()
        self.election_id = election_id