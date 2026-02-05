#!/bin/bash
# FINUX INFINITY OPTIMIZER

DOMAIN="finux222.surge.sh"

echo ">> OPTIMIZING FOR DEPLOYMENT..."

# 1. GitHub Sync
echo ">> SYNCING GITHUB REPOS..."
git add .
git commit -m "Finux 2.2.2: FAI 🪵🪓 Optimization & FIP Compression"
git push origin main

# 2. Local Cleanup
echo ">> PURGING LOCAL CACHE..."
find . -name ".DS_Store" -delete

# 3. Surge Deployment
echo ">> PUSHING TO $DOMAIN..."
surge www $DOMAIN

echo ">> ✅ SYSTEM LIVE AT https://$DOMAIN"
