#!/bin/bash

source /Users/mah/Ballon/src/gpx2czml/.venv/bin/activate

#echo example: genczml -t 20210925-Stiwoll-Stallhofen.gpx  -T trajectory__2021-09-25T05_00_00.gpx 

python /Users/mah/Ballon/src/gpx2czml/genczml $*

