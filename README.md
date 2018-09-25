# DNSStryker.py

DNSStryker.py is a simple Python script with a simple improvement that wraps around the host command in Unix/Linux operating systems. DNSStryker works in much of the same way as fierce, however instead of performing forward DNS brute force lookup on one domain at a time, you can feed a list of subdomains (mysite.org, example.com, etc.) and a list of hostnames (www, mail, owa, etc.) to the DNSStryker. DNSStryker will then append each of the hostnames to each of the subdomains and attempt to resolve the FQDN with the Unix/Linux host command in one go.

## Wordlists:
Hostname wordlists are included in the repository for convenience.
