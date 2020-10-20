# ServerBitzInsights
The server module for the ServerBitzInsights mobile application


# Files
The Installer will create a service and several files. 

serverbitzinsight.service file and enable it as a service
/etc/serverbitzinsight.config
The installer will create a directory location where you want to host the file, this file will be zip password protected and the directory will be random making it difficult for web scanners to identify. 

The zip file will contain a json file of simple information example included in the project.

# JSON file cb-serverbitz.json 
This file will contain the data from the collectors, there is two types of data:

Name:Value or Name:Array

Example will be:
Errors:33
Top IPs: 10.10.10.10,10.10.10.20,10.10.10.10,10.10.10.30,...

