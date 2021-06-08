How many visible files are there in the home directory(excluding ./ and ../)?
Ans: ls -l

What is the content of file5?
Ans: cat file5

Which file contains the string ‘password’?
Ans: grep password *

What is the IP address in a file in the home folder?
Ans: 
egrep -o "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" * 


How many users can log into the machine?
Ans:  cat /etc/passwd | grep "/bin/bash" | wc -l

What is the sha1 hash of file8?
Ans: sha1sum file8

What is mcsysadmin’s password hash?

we tried to cat /etc/shadow  got permision denied message 
then we run  following command to find a file contain shadow string
find / -name shadow* 2>/dev/null | head
/etc/shadow
after runing command we got file var/shadow.bak which the backup file of /etc/shadow 

now we run  grep mcsysadmin /var/shadow.bak this command