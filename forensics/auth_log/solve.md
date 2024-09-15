In the beginning of the logs, we can see that the user "securitiie" is getting bruteforced through the ssh protocol, then there is a successful login as "securitiie".
After that, we can see this line : sudo: securitiie : TTY=pts/2 ; PWD=/home/securitiie ; USER=root ; COMMAND=/usr/sbin/openvpn --dev null --script-security 2 --up '/bin/sh -c sh'
The user securitiie, is trying to elevate his privileges through a sudo misconfiguration, using the openvpn software and exploiting his sudo privileges to get a root shell.
Then, we can see that the user "professional" is being created and added to the sudo group for persistance and in order to have a second user that has an easy root access.
The MITRE Sub-technique ID for this method of persistance is : T1136.001 (Create Account: Local Account) : https://attack.mitre.org/techniques/T1136/001/

FSIIECTF{bruteforce_ssh_sudo_openvpn_T1136.001}