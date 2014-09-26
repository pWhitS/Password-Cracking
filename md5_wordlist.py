'''
This program opens a dump of md5 hashed passwords, without salts, and a selected
wordlist file. Hashed passwords are loaded into a hash table, and the wordlist is 
loaded into an array. Each password is hashed with md5 then looked up in the
hash table. Cracked passwords are output to a file.
'''
import hashlib
import sys

if len(sys.argv) < 3:
	print("Error: No hash or wordlist file loaded")
	print("Ex: Python md5.py arghash.txt argwords.txt")
	
hash_filename = sys.argv[1]
word_filename = sys.argv[2]

try: #open all files
	wordlist_file = open(word_filename, "r")
	hash_file = open(hash_filename, "r")
	cracked_file = open("cracked/cracked_" + hash_filename, "w")
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
	md5 = hashlib.md5(pwd).hexdigest().strip()
		
	if hashDict.has_key(md5):
		count += 1
		cracked_file.write(md5 + " " + pwd + "\n");

print("total cracked: " + str(count))

