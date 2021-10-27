
'''

Lets count the number of public IPs that new zealand ISPs own!


This IP data is obtained from the internet, here:
https://www.nirsoft.net/countryip/nz.html

And the CSV has been downloaded.

NOTE THAT THIS DATA MAY BE OUTDATED!!!

'''


# Format:  
# IP1, IP2, NUM ips, date

sm = 0

with open("nz.csv", "r") as f:
    spl = f.read().splitlines()
    for line in spl:
        spltted = line.split(",")
        if len(spltted) >= 3:
            n = int(spltted[2])
            sm += n


print(f"New Zealand has {sm} public addresses allocated.")



