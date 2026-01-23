nano ~/.bashrc
# Auto-boot Finux if we are in a GUI environment
if [ -n "$DISPLAY" ]; then
    sh /home/jacob/finux/bootloader.sh
fi
