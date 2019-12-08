import urllib.request
import subprocess

ad_server = 'https://raw.githubusercontent.com/anudeepND/blacklist/master/adservers.txt'
steven = 'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling-social/hosts'
noblock_hosts = 'https://raw.githubusercontent.com/notracking/hosts-blocklists/master/hostnames.txt'
noblock_domains = 'https://raw.githubusercontent.com/notracking/hosts-blocklists/master/domains.txt'

urls = (('steves.txt', steven), ('ad_server.txt', ad_server), ('notrack_hosts.txt', noblock_hosts), ('notrack_domains
.txt', noblock_domains))

for fname, url in urls:
    with urllib.request.urlopen(url) as resp:
        print(f'downloading files from {url}')
        with open(f'./hosts/{fname}', 'w') as f:
            hosts = resp.read()
            f.write(hosts.decode('utf-8'))

with open('./hosts/steves.txt') as rl:
    with open('./hosts/steves_edit.txt', 'w') as wl:
        wl.writelines(rl.readlines()[37:])

print('restarting dnsmasq')
subprocess.run(['sudo', 'killall', '-HUP', 'dnsmasq'])