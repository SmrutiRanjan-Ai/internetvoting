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
