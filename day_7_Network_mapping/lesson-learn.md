 How many TCP ports under 1000 are open?

 nmap -sS -sV -A -p- 10.10.219.159

Meaning of command:

# sS TCP SYN scan

# sT TCP connect scan

# sU UDP scans

# sY SCTP INIT scan

# sN TCP NULL

# -sV Version detection

# -A Aggressive detection

# -oN output.txt

# -O  OS detection (require root privilege)