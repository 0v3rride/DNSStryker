#!/usr/bin/env python3

from sys import *;
from subprocess import *;
import os;

def resolver(domains, subdomains):
    # #out = Popen(std).stdout.read().decode("UTF-8");

    subfile = open(subdomains, "r");
    domainfile = open(domains, "r");

    sublist = subfile.read().splitlines();
    domainlist = domainfile.read().splitlines();

    for dom in domainlist:
        for sub in sublist:
            call(["host", "{}.{}".format(sub, dom)]);

    print("\n[!] Script has completed!");

if __name__ == '__main__':
    if (len(argv) < 3):  # up to 3
        print("Usage: ./dnsstriker.py <list of subdomains and TLD (domain.net, example.com, mydomain.org)> <list of hosts (www, mail, authns, etc.)>");
        print("The list of hosts and the list of subdomains will be joined together (authns.example.com)\nThen the host command will be used to try and resolve the FQDN to an IP address in an automated process.");
    else:
        try:
            print("""
  ___  _  _ ___ ___ _            _           
 |   \| \| / __/ __| |_ _ _ _  _| |_____ _ _ 
 | |) | .` \__ \__ \  _| '_| || | / / -_) '_|
 |___/|_|\_|___/___/\__|_|  \_, |_\_\___|_|  
                            |__/             
 [!] Script has started...
 [!] Use ctrl+c to cancel the script at anytime.
 
""");
            resolver(os.path.abspath(argv[1]), os.path.abspath(argv[2]));
        except:
            print("[!] Script has terminated unexpectedly due to an error!");