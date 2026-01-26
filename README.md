# Finux
Frost Sub-Zero Vault Launch app 
# Initialize the local repo
git init

# Add the Genesis block, Kernel headers, and DARPA FOIA scripts
git add .

# Create the first public commit
git commit -m "Frost Protocol Genesis: Initial Open Source Release - Jan 24, 2026"

# Link to your public GitHub/GitLab
git remote add origin https://github.com/Frost-OS/Finux-Project.git

# Push the code to the world
git push -u origin main
# Frostoise Protocol
Deployment of the 1655 West Main Node via Termux/F-Droid.

## Installation
1. Install dependencies:
   `pkg install x11-repo tur-repo`
   `pkg install python-kivy mesa-dev libglvnd-dev msmtp bsd-mailx ffmpeg`
2. Configure `~/.msmtprc` with your Google App Password.
3. Run the engine:
   `python frostit.py`
