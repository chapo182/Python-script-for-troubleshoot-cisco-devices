import paramiko
import cmd
import sys
import time
import os


def conexion(ip):
	hostname = raw_input("Enter the hostname\n")
	print("\n")
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(ip, username='test', password='test', allow_agent=False, look_for_keys=False)
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	chan = ssh.invoke_shell()
	print "[+] Connecting........"
	return versionUptime(chan, hostname)
	print u"\x1b[0m"
	

def versionUptime(chan, hostname):
	hostname = hostname + '#'
	chan.send('show version | i uptime')
	chan.send('\n')
	time.sleep(1)
	clock = chan.recv(9999)
	if clock != hostname:
		print clock.strip(hostname)
		print main()

print ("############################################")
print ("#            osisecurite.com               #")
print ("#                by chapo                  #")
print ("#                                          #")
print ("############################################\n")

def main():
	protocolo = raw_input("Choose Protocol ssh/telnet\n").lower()


	if protocolo == "ssh" and len(protocolo) == 3:
		ip = raw_input("Please Enter the IP Address \n")
		test = os.system('ping ' '-c 5 -W 1 '+ str(ip) + ' >  /dev/null')
		if not test:
			print u"\033[92m [+] Device Reachable" 
			conexion(ip)
		else:
			print u"\033[91m [-] Device Unreachable"
			print "[*] Re enter the information"
			print u"\x1b[0m"	
			main()

		
	elif protocolo == "telnet" and len(protocolo) == 6:
		ip = raw_input("Please Enter the IP Address \n")
		test = os.system('ping ' '-c 5 -W 1 '+ str(ip) + ' >  /dev/null')
		if not test:
			print u"\033[92m [+] Device Reachable........"
			conexion(ip)
		else:
			print "[-] Device Unreachable"
			main()

	else:
		main()

if __name__ == "__main__":
	main()
