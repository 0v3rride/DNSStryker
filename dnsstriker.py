#!/usr/bin/env python3

####################
## DNSStryker.py ###
####################
#  0v3rride - 2018 #
####################

from sys import *;
from argparse import *;
from socket import *;
import os;
from re import *;
#from dnspython import

def forwardLookup(cargs): # FQDN --> IP
    hostlist = None;
    domainlist = None
   #badIpList = ["198.105.254.10", "198.105.244.10"];

    try:
        # Check for valid files and read them out and store them in lists by using the newline character as a delimiter
        if os.path.isfile(cargs.domainList) and os.path.isfile(cargs.hostList):
            hostlist = open(os.path.abspath(cargs.hostList), "r").read().splitlines();
            domainlist = open(os.path.abspath(cargs.domainList), "r").read().splitlines();

            # Resolve all FQDNs to IPs
            for dom in domainlist:
                for host in hostlist:
                    try:
                        if cargs.badIPList is None:
                            print("{}.{} --> {}".format(host, dom, gethostbyname("{}.{}".format(host, dom))));
                        elif cargs.badIPList is not None:
                            ip = gethostbyname("{}.{}".format(host, dom));
                            if ip not in cargs.badIPList:
                                print("{}.{} --> {}".format(host, dom, gethostbyname("{}.{}".format(host, dom))));
                    except:
                        print(end="\r");
        else:
            print("One of the paths to the provided files does not exist. Please check your syntax!");
    except FileExistsError:
        print("[!] File path provided is not valid! Error Num 1");
    except FileNotFoundError:
        print("[!] File path provided is not valid! Error Num 2");

def reverseLookup(cargs): # IP --> FQDN
    try:
        if(os.path.isfile(cargs.ipList)):
            iplist = open(os.path.abspath(cargs.ipList), "r").read().splitlines();

            for addr in iplist:
                try:
                    print("{} --> {}".format(addr, getfqdn(addr)));
                except:
                    print(end="\r");
    except FileExistsError:
        print("[!] File path provided is not valid! Error Num 1");
    except FileNotFoundError:
        print("[!] File path provided is not valid! Error Num 2");


def resolver(cargs):
    if cargs.hostList is not None and cargs.domainList is not None and cargs.ipList is None:
        forwardLookup(cargs);
    elif cargs.ipList is not None and cargs.hostList is None and cargs.domainList is None:
        reverseLookup(cargs)
    else:
        print("[!] You may only do a forward or reverse lookup at any single given time, not both. Please use -hL and -dL for forward lookups and -iL for reverse lookups.");
        exit(0);

    # if cargs.hostList is not None and cargs.domainList is not None:
    #     forwardLookup(cargs);
    # elif cargs.ipList is not None:
    #     reverseLookup(cargs)
    # elif((cargs.hostList is not None and cargs.domainList is not None and cargs.ipList is not None) or (cargs.hostList is not None and cargs.ipList is not None) or (cargs.domainList is not None and cargs.ipList is not None)):
    #     print("[!] You may only do a forward or reverse lookup at an single given time, not both. Please use -hL and -dL for forward lookups and -iL for reverse lookups.");
    #     exit(0);


def main():
    # Argument parser
    parser = ArgumentParser(description="A simple forward and reverse DNS brute forcer. Requires at least one argument: List of IPs (-iL) for reverse lookup for both a list of hosts and domains (-hL & -dL) for forward lookups!");
    parser.add_argument("-hL", "--hostList", required=False, type=str, help="Absolute path to file with the list of hostnames (www, mail, myhost, etc.)");
    parser.add_argument("-dL", "--domainList", required=False, type=str, help="Absolute path to file with the list of domains (mydomain.org, somedomain.com, college.edu, etc.");
    parser.add_argument("-iL,", "--ipList", required=False, type=str, help="Absolute path to file with the list of IPs for reverse DNS lookup.");
    parser.add_argument("-bL", "--badIPList", required=False, nargs='+', help="Give list of IPs to ignore separated by spaces");
    # parser.add_argument("-a", "--address", required=False, action="store_true", help="Filter for addresses only (will not include addresses for mail exchange servers");
    # parser.add_argument("-m", "--mx", required=False, action="store_true", help="Filter for addresses only pertaining to mail exchange servers");
    # parser.add_argument("-i", "--ips", required=False, action="store_true", help="Only return the IP addresses or FQDNs that are valid");
    # parser.add_argument("-r", "--resovled", required=False, action="store_true", help="Filter for output for addresses and FQDNs that have been successfully resolved only");
    # parser.add_argument("--alias", required=False, action="store_true", help="Filter for aliases");

    # Parse arguments
    args = parser.parse_args();

    # Check number for number arguments
    if (len(argv) < 2):  # up to 2
        parser.print_help();
    else:
        try:
            print("""
      ___  _  _ ___ ___ _            _           
     |   \| \| / __/ __| |_ _ _ _  _| |_____ _ _ 
     | |) | .` \__ \__ \  _| '_| || | / / -_) '_|
     |___/|_|\_|___/___/\__|_|  \_, |_\_\___|_|    v1.1
                                |__/                 
     
     [*] https://github.com/0v3rride
     [*] Script has started...
     [*] Use CTRL+C to cancel the script at anytime.

    """);
            resolver(args);  # start parser here
            print("\n[!] Script has completed!");
        except KeyboardInterrupt as ki:
            print("\n");
        except Exception as e:
            # print("[!] An error has occured! The script has been terminated!");
            print(e);


if __name__ == '__main__':
    main();