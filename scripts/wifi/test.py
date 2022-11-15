from subprocess import Popen, PIPE

x = Popen("./get-ssid", stdout=PIPE)
out, _ = x.communicate()

print(out.decode('utf-8'))
