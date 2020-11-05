import re
import json

from os import system, name

if __name__ == '__main__':
    accesslog = 'D:\\Cases\\SSEENrollment\\W3SVC2\\u_ex170929_x.log'
    fail2banlog = 'D:\\Downloads\\fail2ban.log'

    patternSourceIps = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")
    
    openFile = open(accesslog, "r")

    readLines = openFile.read()
    uniqueIPs = []
    IPs = re.findall(patternSourceIps, readLines)
    for ip in IPs:
        if ip not in uniqueIPs:
            uniqueIPs.append(ip)

 
    ips = json.dumps(uniqueIPs)
    formatips = ['uniqueIPs: ', ips]
    uniqueips = json.dumps(formatips)
   

    # FAIL2BAN
    patternSourceIps = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")
    uniqueBanIPs = []
    with open(fail2banlog, 'r') as n:
        for line in n:
            if "Ban" in line:
                uniqueBanIPs += re.findall(patternSourceIps, line)
     
    banips = json.dumps(uniqueBanIPs)
    formatbanips = ['Fail2BanIPs: ', banips]
    fail2BanIPs = json.dumps(formatbanips)


    print('[' + uniqueips + ', ' + fail2BanIPs + ']')
