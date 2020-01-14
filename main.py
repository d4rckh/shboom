import argparse
import Cracker

ArgParser = argparse.ArgumentParser()

#parser.add_argument("--verbosity", help="increase output verbosity")
ArgParser.add_argument("-f", help="The file to takes the hashes from, one on each line.") 
ArgParser.add_argument("-t", help="Hash type md5 is the only one supported right now.") 
ArgParser.add_argument("-w", help="The file containg the wordlist.") 

args = ArgParser.parse_args()

results = []

with open(args.f, 'r') as hashes:
    hashes = hashes.read().split('\n')
    count = hashes.__len__()
    hashtype = args.t

    print(hashes)

    print('Cracking ' + str(count) + ' hashes...')
    print('Hash type: ' + hashtype)

    for hash in hashes:
        
        if hash != '':
            with open(args.w, 'r') as words:
                words = words.read().split('\n')
                for word in words:
                    results.append(Cracker.crackword(hash, hashtype, word))

print('Cracking ended, results:')
for result in results:
    if result["cracked"]:
        print('----------------------SUCCESSFULLY CRACKED----------------------')
        print('Hash     : ' + result["hash"])
        print('Cracked  : ' + str(result["cracked"]))
        print('Result   : ' + result["word"])
        print('----------------------SUCCESSFULLY CRACKED----------------------')
