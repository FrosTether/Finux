# 6. Git Push (Verified Builds Only)
echo "[*] Cold boot passed. Preparing to push to remote..."

# Navigate to your local repo root
cd $PROJECT_DIR

# Stage changes (including new binaries if tracked)
git add .

# Commit with the nightly timestamp
COMMIT_MSG="Nightly Verified Build: $(date +'%Y-%m-%d %H:%M') [Android 17 PC]"
git commit -m "$COMMIT_MSG"

# Push to your private main branch
echo "[*] Pushing to GitHub/GitLab..."
git push origin main --force # Using force here if you use a rolling nightly branch

if [ $? -eq 0 ]; then
    echo "--- [$(date)] Full Cycle Success: Build, Test, and Pushed ---"
else
    echo "[!] ERROR: Git push failed. Check your SSH keys or network."
    exit 1
fi
