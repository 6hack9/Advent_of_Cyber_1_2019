SSH port is not running on standard port, so we run the following nmap command to get the port where ssh is running 

# sudo nmap -sS -sV -A -p- 10.10.143.204

We can scan the whole file system to find all files with the SUID bit set, with the following code:

# find / -user root -perm -4000 -exec ls -ldb {} \; 2>/dev/null

# find / -user igor -perm -4000 -exec ls -ldb {} \; 2>/dev/null