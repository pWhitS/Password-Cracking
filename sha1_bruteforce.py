'''
This python file opens the LinkedIn hashed password dump and brute forces
the hashes over a character set and a user defined length. 
'''
import itertools
import string
import hashlib
import sys

#get min and max password lengths for brute forcing 
if len(sys.argv) < 3:
	MINPASS = 6
	MAXPASS = 10
else:	
	MINPASS = int(sys.argv[1])
	MAXPASS = int(sys.argv[2])

#open the files
hash_file = open("hashfiles/linkedin.txt", "r")
cracked_file = open("cracked/brute_linkedin_cracked.txt", "w")

#define the character set to brute force over
charset = string.ascii_letters + string.digits

hashDict = {} #init a hash table for hashed passwords
for hash in hash_file:
	hashDict[hash.strip()] = 0

def bruteforce(_charset, _minlen, _maxlen):
    return (''.join(guess)
        for guess in itertools.chain.from_iterable(itertools.product(_charset, repeat=i)
        for i in range(_minlen, _maxlen + 1))
    )

for pwd in bruteforce(charset, MINPASS, MAXPASS): 
	sha1 = hashlib.sha1(pwd).hexdigest().strip()
	
	if hashDict.has_key(sha1): #search hash table
		cracked_file.write(sha1 + " " + pwd + "\n");

		
	
	
	