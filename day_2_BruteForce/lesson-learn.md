Brute force attacks used to crack password,enumarate username and also for discover hidden page and content.


Go Buster:
gobuster dir -u Url -w /wordlists/ -e -t64


WFuzz:
wfuzz -c -W /usr/share/wfuzz/wordlist/dir/common.txt --hc 400,404,403 http://192.168.1.1/dvwa/FUZZ


Dirb:
dirb http://192.168.1.1/dvwa 



DirSearch:
dirsearch.py -u https://www.tryhackme.com/ -w ./DirBuster-Lists/directory-list-2.3-big.txt -e html

Syntax:
-u is the hostname of the website
-w is the wordlist
-e / -x is the extension or expanded mode
Different web pages use different technologies(you can usually identify this by the file it loads in the browser e.g. if it’s a .js, .aspx page)
-f is the flag used to force extensions applied to the pages in the word list:
Mostly used when you’re quite sure about what kind of technology a server is running
If you don’t know what extension to brute force, you don’t need to specify this flag
-t number of threads
-o output 