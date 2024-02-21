import requests, sys

def request(url):
    try:
        result = requests.get("https://" + url)
        if(result):
            print("[+] Subdomain discovered ----> " + url)
    except:
        pass


def main():
    target_url = sys.argv[1]
    #open subd list
    with open("subdmainwordlist.txt", "r") as wordlist:
        for line in wordlist:
            #To remove space in terminal
            word = line.strip()
            test_url = word + "." + target_url
            request(test_url)
 
main()
