#!/bin/bash
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6

exec >> /var/www/html/start.log 2>&1

cd /etc/EDCET-STUDIO/

echo "Starting script at $(date)"
# Start the docker containers for minio, redis, and postgres
sudo make run-services &

/etc/EDCET-STUDIO/startstudio.sh

