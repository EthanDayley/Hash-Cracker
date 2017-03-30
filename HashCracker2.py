import hashlib
import time

def loadWords(wordlist):
    f=open(wordlist)#name of wordlist for dictionary attack
    words = f.read()
    words.replace('\n',' ')
    words=words.split()
    return words
def TestMD5(yourhash, words):
    match = False
    for i in words:
        if hashlib.md5(i.encode()).hexdigest() == yourhash:
            match = True
            word = i
            break
        try:
            wordCap = i[0].upper()+i[1:-1]+i[-1]
            if hashlib.md5(wordCap.encode()).hexdigest() == yourhash:
                match = True
                word = wordCap
                break
        except: pass
    if match:
        return word
    else:
        return 'Not Found'    
def TestSha1(yourhash, words):
    match = False
    for i in words:
        if hashlib.sha1(i.encode()).hexdigest() == yourhash:
            match = True
            word = i
            break
        try:
            wordCap = i[0].upper()+i[1:-1]+i[-1]
            if hashlib.sha1(wordCap.encode()).hexdigest() == yourhash:
                match = True
                word = wordCap
                break
        except: pass
    if match:
        return word
    else:
        return 'Not Found'
def TestSha224(yourhash, words):
    match = False
    for i in words:
        if hashlib.sha224(i.encode()).hexdigest() == yourhash:
            match = True
            word = i
            break
        try:
            wordCap = i[0].upper()+i[1:-1]+i[-1]
            if hashlib.sha224(wordCap.encode()).hexdigest() == yourhash:
                match = True
                word = wordCap
                break
        except: pass
    if match:
        return word
    else:
        return 'Not Found'

def TestSha256(yourhash, words):
    match = False
    for i in words:
        if hashlib.sha256(i.encode()).hexdigest() == yourhash:
            match = True
            word = i
            break
        try:
            wordCap = i[0].upper()+i[1:-1]+i[-1]
            if hashlib.sha256(wordCap.encode()).hexdigest() == yourhash:
                match = True
                word = wordCap
                break
        except: pass
    if match:
        return word
    else:
        return 'Not Found'
def TestSha384(yourhash, words):
    match = False
    for i in words:
        if hashlib.sha384(i.encode()).hexdigest() == yourhash:
            match = True
            word = i
            break
        try:
            wordCap = i[0].upper()+i[1:-1]+i[-1]
            if hashlib.sha384(wordCap.encode()).hexdigest() == yourhash:
                match = True
                word = wordCap
                break
        except: pass
    if match:
        return word
    else:
        return 'Not Found'

def TestSha512(yourhash, words):
    match = False
    for i in words:
        if hashlib.sha512(i.encode()).hexdigest() == yourhash:
            match = True
            word = i
            break
        try:
            wordCap = i[0].upper()+i[1:-1]+i[-1]
            if hashlib.sha512(wordCap.encode()).hexdigest() == yourhash:
                match = True
                word = wordCap
                break
        except: pass
    if match:
        return word
    else:
        return 'Not Found'

def Crack(yourhash, wordlist):
    """Crack a hash (yourhash) based on a file containing a wordlist
       each word in the wordlist should be on a new line"""
    Time1 = time.time()
    match = False
    hashtype = ''
    words = loadWords(wordlist)
    word = ''
    MD5 = TestMD5(yourhash,  words)
    if MD5 != 'Not Found':
        hashtype = 'MD5'
        match = True
        word = MD5
    SHA1 = TestSha1(yourhash,  words)
    if SHA1 != 'Not Found' and not match:
        hashtype = 'SHA1'
        match = True
        word = SHA1
    SHA224 = TestSha224(yourhash,  words)
    if SHA224 != 'Not Found' and not match:
        hashtype = 'SHA224'
        match = True
        word = SHA224
    SHA256 = TestSha256(yourhash,  words)
    if SHA256 != 'Not Found'  and not match:
        hashtype = 'SHA256'
        match = True
        word = SHA256
    SHA384 = TestSha384(yourhash,  words)
    if SHA384 != 'Not Found'  and not match:
        hashtype = 'SHA384'
        match = True
        word = SHA384
    SHA512 = TestSha512(yourhash,  words)
    if SHA512 != 'Not Found'  and not match:
        hashtype = 'SHA512'
        match = True
        word = SHA512
    rlist = {'hashtype':hashtype, 'word':word, 'time':time.time()-Time1}
    if match:
        return rlist
    else:
        return rlist

    
