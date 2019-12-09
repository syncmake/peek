import subprocess
import urllib.request

ad_server = "https://raw.githubusercontent.com/anudeepND/blacklist/master/adservers.txt"
noblock_hosts = (
    "https://raw.githubusercontent.com/notracking/hosts-blocklists/master/hostnames.txt"
)
noblock_domains = (
    "https://raw.githubusercontent.com/notracking/hosts-blocklists/master/domains.txt"
)

# pi hole domains
just_domains = "https://mirror1.malwaredomains.com/files/justdomains"
cameleon = "http://sysctl.org/cameleon/hosts"
discon_track = "https://s3.amazonaws.com/lists.disconnect.me/simple_tracking.txt"
discon_ads = "https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt"
hosts_file = "https://hosts-file.net/ad_servers.txt"
steven = "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"

# download all the files
urls = (
    ("ad_server.txt", ad_server),
    ("notrack_hosts.txt", noblock_hosts),
    ("notrack_domains.txt", noblock_domains),
    ("just_domains.txt", just_domains),
    ("cameleon.txt", cameleon),
    ("discon_track.txt", discon_track),
    ("discon_ads.txt", discon_ads),
    ("hosts_files.txt", hosts_file),
    ("steves.txt", steven),
)


def download_to_file(urls: tuple):
    """Download files into ./hosts folder
    
    Parameters
    ----------
    url : tuple
        Takes a tuple of name of file to save and url
    """
    for fname, url in urls:
        with urllib.request.urlopen(url) as resp:
            print(f"downloading files from {url}")
            with open(f"./hosts/{fname}", "w") as f:
                hosts = resp.read()
                f.write(hosts.decode("utf-8"))


download_to_file(url=urls)

# post processing of the host files now
# each host file is slightly different and rather then using the generic method provided by
# gravity.sh i am going to explicitly change each of the file formats. 

# ignore top block of steves
with open("./hosts/steves.txt") as rl:
    with open("./hosts/steves_edit.txt", "w") as wl:
        # skipping first couple lines
        wl.writelines(rl.readlines()[37:])

print("restarting dnsmasq")
subprocess.run(["sudo", "killall", "-HUP", "dnsmasq"])

