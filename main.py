import counters
import organizers
import user
import voter
import votes
import registrars
import candidate
import global_file
import evaluators
import election
import ballot

voters_num=3
region = 1

registrar = registrars.Registrars(region)
organizer = organizers.Organizer(region)


candidates_num = 3
counters_num = 5

for i in range(candidates_num):
	c=candidate.Candidate(region)
candidates = global_file.list_of_candidates[region]
evaluator = evaluators.Evaluator(region,candidates)
ballot = ballot.Ballot(region,candidates)
for i in range(counters_num):
	c=counters.Counters(region)

for _ in range(voters_num):
	v=voter.Voter(region)


for i in global_file.list_of_voters[region]:
	i.send_id_registrar()

for i in global_file.list_of_voters[region]:
	print(i.id,i.alias)
	i.vote()

global_file.list_of_voters[region][1].vote()

for i in global_file.list_of_counters[region]:
	i.send_votes_evaluator()

global_file.list_of_evaluators[region].construct_votes()
global_file.list_of_evaluators[region].finalize_votes()
global_file.list_of_evaluators[region].mixnet()
global_file.list_of_evaluators[region].final_results()
