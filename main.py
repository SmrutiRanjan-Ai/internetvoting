

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
import blockchain
import agent
voters_num=5
region = 1
blockchain=blockchain.Blockchain()
issuer = agent.Agent("issuer",blockchain,"issuer")
registrar_agent = agent.Agent("registrar",blockchain,"issuer")
issuer.create_invitation('issuer')
registrar = registrars.Registrars(region,blockchain)
organizer = organizers.Organizer(region)


candidates_num = 3
counters_num = 5

for i in range(candidates_num):
	c=candidate.Candidate(region)
	print(c)
candidates = global_file.list_of_candidates[region]
evaluator = evaluators.Evaluator(region,candidates)
ballot = ballot.Ballot(region,candidates)
for i in range(counters_num):
	c=counters.Counters(region)
	print(c)

for _ in range(voters_num):
	v=voter.Voter(region,blockchain)
	issuer.send_invitation(issuer.invitation, f"{v.alias}")
	v.agent.update_data(v.alias,18)
	v.agent.send_attributes('issuer')
	issuer.check_attributes()
	issuer.send_credentials()
	v.agent.present_claim('registrar')


for i in global_file.list_of_voters[region]:
	i.send_id_registrar()

for i in global_file.list_of_voters[region]:
	print(i.id,i.alias)
	i.vote()

global_file.list_of_voters[region][0].vote()
global_file.list_of_voters[region][0].vote()
global_file.list_of_voters[region][0].vote()

for i in global_file.list_of_counters[region]:
	i.send_votes_evaluator()

global_file.list_of_evaluators[region].construct_votes()
global_file.list_of_evaluators[region].finalize_votes()
global_file.list_of_evaluators[region].mixnet()
global_file.list_of_evaluators[region].final_results()
