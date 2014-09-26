'''
This file opens the dump file of LinkedIn hashed passwords and a selected
wordlist file. The hashed passwords are loaded into a hash table, and the 
wordlist is loaded into an array. The password array is then looped through,
each password hashed with sha1, and then looked up in the hash table. If the
hash is found, then the hash and plaintext password are written out to a file.
'''
import hashlib
import sys

if len(sys.argv) < 2:
	print("Error: No wordlists file loaded")
filename = sys.argv[1]

try: #open all files
	wordlist_file = open(filename, "r")
	hash_file = open("hashfiles/Linkedin.txt", "r")
	cracked_file = open("cracked/linkedin_cracked.txt", "w")
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
	sha1 = hashlib.sha1(pwd).hexdigest().strip()
		
	if hashDict.has_key(sha1) or hashDict.has_key('00000'+sha1[5:]):
		count += 1
		cracked_file.write(sha1 + " " + pwd + "\n");

print("total cracked: " + str(count))

