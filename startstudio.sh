#!/bin/bash

#!/bin/bash

# Activate the environment
sleep 1
./etc/EDCET-STUDIO/
echo "Starting script at $(date)"
sleep 1

exec >> /var/www/html/startpyenv.log 2>&1
/etc/EDCET-STUDIO/miniconda3/bin/python --version
export PATH="/etc/EDCET-STUDIO/miniconda3/bin:$PATH"
cd /etc/EDCET-STUDIO/
# Run the Django development server
yarn run runserver


