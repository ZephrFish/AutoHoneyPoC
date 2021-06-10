import os
import time

def compile_go(path, cve):
	try:
		# Debugging
		# print(path)
		# print(cve)
		# Line below is a fix for WSL
		os.system(f'env GOOS=windows GOARCH=amd64 go build -o {path}{cve}.exe {path}{cve}.go')
		# Line below works on linux by default (kali, ubuntu)
		# os.system(f'env GOOS=windows GOARCH=amd64 go build -o {path} {path}{cve}.go')
		os.system(f'rm {path}{cve}.go')
		print("[*] Cross Compile Success!")
	except:
		print("[*] Compilation failed :(")
		time.sleep(1)
