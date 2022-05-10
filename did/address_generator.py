import hashlib,base58,binascii,ecdsa, codecs

def address_generator(ecdsaPrivateKey,ecdsaPublicKey):

    ecdsaPublicKey = '04' +  ecdsaPublicKey.to_string().hex()
    hash256FromECDSAPublicKey = hashlib.sha256(binascii.unhexlify(ecdsaPublicKey)).hexdigest()
    ridemp160FromHash256 = hashlib.new('ripemd160', binascii.unhexlify(hash256FromECDSAPublicKey))
    prependNetworkByte = '00' + ridemp160FromHash256.hexdigest()
    hash = prependNetworkByte
    for x in range(1,3):
        hash = hashlib.sha256(binascii.unhexlify(hash)).hexdigest()

    cheksum = hash[:8]
    appendChecksum = prependNetworkByte + cheksum
    bitcoinAddress = base58.b58encode(binascii.unhexlify(appendChecksum))
    return bitcoinAddress.decode('utf8')

sk=ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
vk=sk.get_verifying_key()
address_generator(sk,vk)