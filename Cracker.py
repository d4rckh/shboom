import hashlib

def crackword(hash, hashtype, word):
    if hashtype == 'md5':
        hashed = hashlib.md5(word.encode()).hexdigest()
        if hashed == hash:
            return {
                "cracked": True,
                "hashed": hashed,
                "type": hashtype,
                "word": word,
                "hash": hash
            }
        else:
            return {
                "cracked": False,
                "hashedword": hashed,
                "type": hashtype,
                "word": word,
                "hash": hash
            }