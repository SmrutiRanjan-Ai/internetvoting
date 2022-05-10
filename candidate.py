import global_file
import user
class Candidate(user.User):
    def __init__(self, region):
        super().__init__()
        self.region = region
        if region not in global_file.list_of_candidates.keys():
            global_file.list_of_candidates[region]=[self]
        else:
            global_file.list_of_candidates[region].append(self)

    def __str__(self):
        return self.alias

