#################################################
#######Python Network Automation Framework#######
#########Created by Decki Okmal Pratama##########
#################################################

System Requirement:
-Python 3.10 or latest
-PyYaml
-Jinja2
-Paramiko
-Json

Step to use the Framework:
1. Install system requirement on your local pc
2. add ip address, username and password on devices.json
3. edit the yaml file according to the allocation of each location to be configured
4. run mainoop.py
5. done, you will see the result
6. configuration verification : 
	- get ipsec tunnel list
	- get router info bgp summary
	- diagnose sys sdwan service or diagnose sys virtual-wan-link service
