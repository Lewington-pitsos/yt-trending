#!/bin/bash

timestamp=`date +%F_%H-%M-%S`
filename="/home/lewington/code/scrapers/yt-trending/logs/$timestamp.log"

cd /home/lewington/code/scrapers/yt-trending
source env/bin/activate

python3 scrape.py > $filename

deactivate

exit