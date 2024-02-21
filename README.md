Subdomain Discovery Tool

This Python script is a simple subdomain discovery tool designed to identify subdomains associated with a given target domain. It utilizes a wordlist of potential subdomains and attempts to access each subdomain by making HTTP requests. If a subdomain is found to be valid and accessible, it is printed to the console.
<hr>
Features:

    - Subdomain Discovery: The script generates potential subdomains by combining entries from a wordlist with the target domain.
    - HTTP Requests: It sends HTTP requests to each generated subdomain to check for accessibility.
    - Output: Valid subdomains are printed to the console for further analysis.
<hr>
How to Use:

    1) Clone Repository: Clone this repository to your local machine.
    2) Install Requirements: Ensure you have Python installed, along with the requests library. You can install it using pip install requests.
    3) Execute Script: Run the script via command line, providing the target domain as an argument.
    4) Review Results: Valid subdomains discovered during the process will be displayed in the console output.
<hr>
Libraries:
    - requests (pip3 install requests)
<hr>
Wordlist:

    The script utilizes a wordlist (subdmainwordlist.txt) containing potential subdomains. You can customize this wordlist to include specific subdomains relevant to your target.
<hr>
Disclaimer:

    This tool is intended for educational and ethical use only. Ensure you have proper authorization before using it against any target domain. The developer is not responsible for any misuse of this tool.


<p align="left">
</p>
<hr>
<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

