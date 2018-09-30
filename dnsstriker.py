#!/usr/bin/env python3

####################
## DNSStryker.py ###
####################
#  0v3rride - 2018 #
####################

from sys import *;
from subprocess import *;
import os;
from argparse import *;

def parseArgs(argl):
    opts = [];

    # Parse other args
    if argl.address and argl.mx:
        print("Cannot grep for resolved addresses and mail exchange addresses at the same time. Please pick one or the other, but not both.");
        exit(0);

    if argl.address:
        opts.append("| grep -i \"has address\" ");

    if argl.mx:
        opts.append("| grep -i \"mail is handled\" ");

    if argl.alias:
        opts.append("| grep -i \"alias for\" ");

    if argl.ips and argl.address:
        opts.append("| cut -d\" \" -f4 ");

    if argl.ips and argl.mx:
        opts.append("| cut -d\" \" -f7 ");

    if argl.ips and argl.alias:
        opts.append("| cut -d\" \" -f1,6 --output-delimiter=\" --> \" ");

    if argl.resovled:
        opts.append("| grep -vi \"3(NXDOMAIN)\" ");

    #Filter out these IPs as they are not valid
    opts.append("| grep -vi \"198.105.254.63\\|198.105.244.63\"");

    return opts;


def resolver(cargs):
    hostlist = None;
    domainlist = None

    try:
        #Check for valid files and read them out and store them in lists by using the newline character as a delimiter
        if os.path.isfile(cargs.Domains) and os.path.isfile(cargs.Hosts):
            hostlist = open(os.path.abspath(cargs.Hosts), "r").read().splitlines();
            domainlist = open(os.path.abspath(cargs.Domains), "r").read().splitlines();
    except FileExistsError:
        print("[!] File path provided is not valid!");
    except FileNotFoundError:
        print("[!] File path provided is not valid! 2");


    #Parse optional arguments
    opts = parseArgs(cargs);
    #print(opts);

    #Resolve all FQDNs to IPs
    for dom in domainlist:
        for host in hostlist:
            output = Popen("host {}.{} {}".format(host, dom, "".join(opts)), stdout=PIPE, shell=True).stdout.read().decode("utf-8"); #Send command to shell and retireve the output
            print(output, end="\r"); #Print the output every iteration


def main():
    # Argument parser
    parser = ArgumentParser(description="A simple forward DNS brute forcer that appends hostnames from one file with domains in the other and attempts to resolve the FQDN into a valid IP address.");
    parser.add_argument("-H", "--Hosts", required=True, type=str, help="Absolute path to file with the list of hostnames (www, mail, myhost, etc.)");
    parser.add_argument("-D", "--Domains", required=True, type=str, help="Absolute path to file with the list of domains (mydomain.org, somedomain.com, college.edu, etc.");
    parser.add_argument("-a", "--address", required=False, action="store_true", help="Filter for addresses only (will not include addresses for mail exchange servers");
    parser.add_argument("-m", "--mx", required=False, action="store_true", help="Filter for addresses only pertaining to mail exchange servers");
    parser.add_argument("-i", "--ips", required=False, action="store_true", help="Only return the IP addresses or FQDNs that are valid");
    parser.add_argument("-r", "--resovled", required=False, action="store_true", help="Filter for output for addresses and FQDNs that have been successfully resolved only");
    parser.add_argument("--alias", required=False, action="store_true", help="Filter for aliases");

    # Parse arguments
    args = parser.parse_args();

    # Check number for number arguments
    if (len(argv) < 3):  # up to 3
        parser.print_help();
    else:
        try:
            print("""
      ___  _  _ ___ ___ _            _           
     |   \| \| / __/ __| |_ _ _ _  _| |_____ _ _ 
     | |) | .` \__ \__ \  _| '_| || | / / -_) '_|
     |___/|_|\_|___/___/\__|_|  \_, |_\_\___|_|  
                                |__/             
     
     [!] https://github.com/0v3rride
     [!] Script has started...
     [!] Use CTRL+C to cancel the script at anytime.

    """);
            resolver(args);  # start parser here
            print("\n[!] Script has completed!");
        except KeyboardInterrupt as ki:
            print("\n");
        except Exception as e:
            print("[!] An error has occured! The script has been terminated!");


if __name__ == '__main__':
    main();