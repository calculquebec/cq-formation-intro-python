#!/usr/bin/env python3
import subprocess
import socket
import sys
import getpass

hostname = socket.gethostname()
if hostname.startswith("lg"):
    print("You are still on the login node.")
    print("Please start an interactive qsub session using qsub interactive.pbs.")
    sys.exit(1)
proc = subprocess.Popen(['ipython','notebook','--no-browser'],stderr=subprocess.PIPE,universal_newlines=True)
for line in proc.stderr:
    sys.stderr.write(line)
    if 'localhost:' in line:
        portidx = line.find('localhost:')+10
        port = int(line[portidx:portidx+4])
        user = getpass.getuser()
        print("\nPlease open a new terminal window and enter the following ssh commands:\n")
        print("ssh -N -f -L1234:%s:22 %s@guillimin.hpc.mcgill.ca"%(hostname,user))
        print("ssh -N -f -L8888:localhost:%d -p 1234 %s@localhost\n"%(port,user))
        print("Then use http://localhost:8888 in a web browser\n")
