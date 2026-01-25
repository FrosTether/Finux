#!/data/data/com.termux/files/usr/bin/bash

# 1. Update Repositories and System
echo "--- Initializing Update ---"
pkg update -y && pkg upgrade -y

# 2. Essential Modern Tools (Rust/Go based for speed)
# eza: modern 'ls' | bat: syntax-highlighted 'cat' | zoxide: smarter 'cd'
echo "--- Installing 2026 Essentials ---"
pkg install python git gh openssh zoxide eza bat zellij micro -y

# 3. Setup Storage Access (Crucial for external file handling)
echo "--- Requesting Storage Access ---"
termux-setup-storage

# 4. Install Gemini CLI for Termux (AI-assisted coding)
# This allows you to debug scripts directly from the terminal
echo "--- Setting up Gemini CLI ---"
pkg install nodejs -y
npm install -g @mmmbuto/gemini-cli-termux

# 5. Configure Aliases for Finux/Maintenance
echo "--- Updating .bashrc ---"
cat <<EOT >> ~/.bashrc

# Productivity Aliases
alias ls='eza --icons'
alias cat='bat'
alias cd='z'
alias upd='pkg update && pkg upgrade -y'

# Finux Testing Workspace
alias test-finux='cd ~/Finux && echo "Running Finux environment test..." && ./boot_test.sh'

# Initialize Zoxide (Smart CD)
eval "\$(zoxide init bash)"
EOT

source ~/.bashrc
echo "--- Setup Complete! Run 'upd' to keep things fresh. ---"
