#!/bin/bash
set -x

ssh -tt username@ip-address << ENDSSH
sudo -u root systemctl start jenkins-agent
exit
ENDSSH
