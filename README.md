Password-Cracking
=================

Cracking passwords for well known hash dumps.

This repository has several python programs that use several different methods for cracking hashed passwords. Currently, there are cracking scripts for sha1, sha256, and md5. However, The md5 script can quickly be modified to crack passwords hashed with any hashing algorithm supported by python's hashlib. The sha256 script is written specifically to crack Formsprings hash dump, where every password was prepended with a salt. 

The md5 script accepts 2 arguments. The arguments must be text files but can be located in subdirectories. The first file is the hash dump we are cracking, and the second file is the wordlist to be loaded. 

    $ python md5_wordlist.py hashes.txt dir1/dir2/wordlist.txt
    
The sha1 and sha256 scripts accept 1 argument, the wordlist file, which can be in a subdirectory. 

    $ python sha256_wordlist.py dir1/wordlist.txt
    
Finally, the sha1 brute force script accepts 2 arguments. These are the minimum length and the maximum length of characters to brute force over. 

    $ python sha1_bruteforce.py 4 12
    

All cracking scripts output cracked passwords to a file named either name_cracked.txt or cracked_name.txt. Also, the plaintext password and corresponding hash are printed to one line in the file, for every cracked password. 
    
    --sample output file--
    7c4a8d09ca3762af61e59520943dc26494f8941b 123456
    f7c3bc1d808e04732adf679965ccc34ca7ae3441 123456789
    5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8 password
    ee8d8728f435fd550f83852aabab5234ce1da528 iloveyou
    775bb961b81da1ca49217a48e533c832c337154a princess
    20eabe5d64b0e216796e834f52d61fd0b70332fc 1234567
    f1cf651ce1a2191a760c0b2f161234f7958e26e4 rockyou
