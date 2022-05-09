import votes,voter,user,counters,candidate,ballot,registrars,global_file,evaluators,election

voters_num=1
region = 1
for i in range(voters_num):
	v=voter.Voter(1)
	global_file.list_of_voters.append(v)

for i in global_file.list_of_voters:
	i.send_id_registrar()