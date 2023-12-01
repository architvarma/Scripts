# SSH Script to Start Jenkins Agent #
This Bash script is designed to remotely start the Jenkins agent service on a specified server using SSH. The script utilizes the ssh command to connect to the server and execute the necessary commands.

## Script Explanation: ##
#!/bin/bash: Specifies the script should be executed using the Bash shell.

set -x: Enables debugging mode, printing each command and its arguments to the standard error output before executing it. Helpful for troubleshooting.

ssh -tt username@ip-address << ENDSSH: Initiates an SSH connection to the specified server {xxx.xxx.xxx.xxx}[ip-adddress] as the user deployer. The -tt option ensures that the remote commands are executed properly.

Commands within the << ENDSSH and ENDSSH block are sent to the remote server for execution.

sudo -u root systemctl start jenkins-agent: Initiates the Jenkins agent service on the remote server with superuser privileges.

exit: Exits the SSH session.

## Prerequisites: ##
Ensure that the SSH key-based authentication is set up for the user **username** to connect to the remote server without a password prompt.

Make sure the user deployer has the necessary permissions to execute the systemctl command with sudo without entering a password.

**Note:** Before running the script, review and modify it according to your specific server setup and security considerations.

### Disclaimer:###
This script assumes a certain environment and configuration. Make sure to adapt it to your specific needs and test it in a safe environment before deploying it in a production setting. Use at your own risk.






