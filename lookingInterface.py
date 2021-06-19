import paramiko
import cmd
import sys
import time
import os

def conexion(ip):
	hostname = raw_input("Enter the hostname\n")
	que = raw_input("Please Enter Interface that you are looking for \n")
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(ip, username='test', password='test', allow_agent=False, look_for_keys=False)
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	chan = ssh.invoke_shell()
	print clock(chan, hostname)
	print lookInt(chan, hostname, que)
	print description(chan, hostname, que)
	log = raw_input("Do you want to print the logs.... y/n \n").lower()
	if log == 'y':
		print logs(chan, hostname, que)
		print u"\x1b[0m"
		print main()
	else:
		print u"\x1b[0m"
		print main()

def clock(chan, hostname):
	hostname = hostname + '#'
	chan.send('show clock')
	chan.send('\n')
	time.sleep(1)
	clock = chan.recv(9999)
	if clock != hostname:
		return clock.strip(hostname)	


def lookInt(chan, hostname, interface):
	hostname = hostname + "#"
	chan.send('sh int ' + interface)
	chan.send('\n')
	chan.send(u"\u0020")
	time.sleep(1)
	clock = chan.recv(9999)
	if clock != hostname:
		return clock.strip(hostname)

def description(chan, hostname, interface):
	hostname = hostname + "#"
	chan.send('sh int ' + interface + ' description')
	chan.send('\n')
	time.sleep(1)
	clock = chan.recv(9999)
	if clock != hostname:
		return clock.strip(hostname)

def logs(chan, hostname, interface):
	hostname = hostname + "#"
	chan.send('sh log | include ' + interface)
	chan.send('\n')
	time.sleep(1)
	clock = chan.recv(9999)
	if clock != hostname:
		return clock.strip(hostname)



print ("############################################")
print ("#            osisecurite.com               #")
print ("#                by chapo182               #")
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

