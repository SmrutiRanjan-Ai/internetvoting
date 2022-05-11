list_of_voters= {}
list_of_candidates={}
list_of_elections=[]
list_of_registrars= {}
list_of_regions=[]
registars_per_region={}
counters= {}
list_of_evaluators= {}
list_of_organizers= {}
list_of_ballot= {}
list_of_counters={}
n = 5  #N vote Counters
k = 3  #K confirmation

list_agents={} #list of agents

def query_diddoc(alias):
    agent=list_agents[alias]
    data = {
  "@context": [
    "https://www.w3.org/ns/did/v1",
    "https://w3id.org/security/suites/ed25519-2020/v1"
  ],
  "id": "did:key:"+agent.did,
  "publicKey": {"type": "Secp256k1VerificationKey2018", "owner":f"{agent.keypairs['pk'].to_string().hex()}" ,"publicKeyHex":f"{agent.keypairs['pk'].to_string().hex()}"},
  "authentication": [{

    "id": f"did:key:{agent.did}#keys-1",
    "type": "Ed25519VerificationKey2020",
    "controller": f"did:key:{agent.did}",
    "publicKeyMultibase": f"{agent.issuer_pk.to_string().hex()}"
  }],
      "service": [
        {"type": "Agency", "serviceEndpoint": "did:sov:fghi8377464",
        "serviceEndpoint": "https://example.com/endpoint/8377464" }]
}
    print('DIDDoc')
    print(data)

