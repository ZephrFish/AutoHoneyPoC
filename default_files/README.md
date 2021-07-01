# $cve Exploit

$summary

### Windows Binary PoC
```
./$cve.exe will run the exploit.
./$cve.exe -t Target IP
./$cve.exe -t www.example.com
```

### Running the exploit on Linux

Change the target IP in $cve.sh then do:

```
chmod +x $cve.sh
usage:   $cve.sh -t <TargetIP>
example: $cve.sh -t 10.3.3.7
example: $cve.sh -t www.example.com
```

## Repo Info
- $cve.exe (sha256sum $sha256hash)
- $cve.sh - Linux compatible exploit for $cve
- README.md - Details the README of the repo



