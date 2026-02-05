#!/bin/bash

# RC241 // THE_CLEAN_SWEEP
# OWNER: Jacob Thomas Frost (voluntaryistj@gmail.com)
# TARGET: Wipe all except fpu4eva.surge.sh

echo "♊ INITIATING CLEAN SWEEP UNDER voluntaryistj@gmail.com..."

# 1. Login Authority
surge login --email voluntaryistj@gmail.com

# 2. Domain Dissolution
# Add any other domains you've used to this list
echo ">> Tearing down frostaie.surge.sh..."
surge teardown frostaie.surge.sh

echo ">> Tearing down frost-os.surge.sh..."
surge teardown frost-os.surge.sh

# 3. Local Purge
echo ">> Purging local build fragments..."
rm -rf games apps scripts assets index.html icecrush.html icechain.html wallet.html compileme.sh

echo "✅ SWEEP COMPLETE. Only fpu4eva.surge.sh remains in the lattice."
