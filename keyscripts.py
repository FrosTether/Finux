# Create a hidden directory within your SDK
mkdir -p ~/.finux_vault/backups

# Create an automated backup script
echo "cp ~/finux/frost.key ~/.finux_vault/backups/frost.key.\$(date +%F_%T)" > backup_key.sh
chmod +x backup_key.sh

# Run the backup
./backup_key.sh
