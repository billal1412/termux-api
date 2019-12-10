import json,os
print ("[*] Getting Contact ...")
os.system("termux-contact-list > /dev/null > list.json")
op = open("list.json","r").read()
j = json.loads(str(op))
print ("Contact List With CLI")
print ("copyright 2019 BILLAL")
for contact in j:
	print ("[+] Name: "+contact["name"])
	print ("[+] Number: "+contact["number"])
