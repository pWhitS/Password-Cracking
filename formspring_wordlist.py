'''
This program opens the dump of Formspring hashed passwords and a selected
wordlist file. The password hashes are loaded into a hash table and the 
wordlist is loaded into an array. The array is then looped through with
all possible salts of 00-99 prepended and hashed with sha256. We then look
in the hash table for this hash. If the hash is in the table, the hash and
the plaintext password are written to a file.
'''
import hashlib
import sys

if len(sys.argv) < 2:
	print("Error: No wordlists file loaded")
filename = sys.argv[1]
 
try: #open all files
	wordlist_file = open(filename, "r")
	hash_file = open("hashfiles/formspring.txt", "r")
	cracked_file = open("cracked/formspring_cracked.txt", "w")
except IOError:
	print("One or more files could not be opened. =(")
	sys.exit(0)

hashDict = {} #init a hash table
for hash in hash_file: 
	hashDict[hash.strip()] = 1	#load hash table w/ hashed passwords

passwordList = [] 
for pwd in wordlist_file:
	passwordList.append(pwd.strip()) #load all passwords from wordlist

count = 0 
for pwd in passwordList:	
	for i in range(0, 100): #loop through all salt values
		if i < 10:
			salt = "0" + str(i)
		else:
			salt = str(i)
		
		sha256 = hashlib.sha256(salt+pwd).hexdigest().strip()
		
		if hashDict.has_key(sha256): #check hash table for password hash
			count += 1
			cracked_file.write(sha256 + " " + pwd + salt + "\n");
	
print "total cracked: ", count

