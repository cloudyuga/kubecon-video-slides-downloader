#!/usr/bin/env bash

# Download KubeCon + CloudNativeCon Europe 2019 presentations from Sched
# Forked https://gist.github.com/hobbsh/35091c54970fff0b86a64cd72f02e8e3
# Forked https://gist.github.com/superbrothers/2c2d3713d8d30a785cabf77831489fcd

while getopts u:d: flag
do
    case "${flag}" in
        u) SchedUrl=${OPTARG};;
        d) Days=${OPTARG};;
    esac
done

if [ -z "$Days" ]
then
      echo "Provide at least 1 Date"
fi

#https://kccnceu2022.sched.com
SchedLink=($SchedUrl)
#DAYS=(2022-05-16 2022-05-17 2022-05-18 2022-05-19 2022-05-20)
DAYS=($Days)
mkdir -p "slides/"

for DAY in "${DAYS[@]}"; do
  LINKS=($(curl -s ${SchedLink}//${DAY}/overview | grep -oEi "f='(.*)' cl" | cut -d\' -f 2 | tr '\n' ' '))
  echo $LINKS
  for LINK in "${LINKS[@]}"; do
    echo $LINK
    FILE_URL=$(curl -s ${SchedLink}/${LINK} | grep "file-uploaded" | cut -d\" -f 4)
    echo  $FILE_URL
    if [ -n "${FILE_URL}" ]; then
      FILEPATHwrite="$(echo $(echo ${LINK} | cut -b 12-)).${FILE_URL##*.}"
      FILEPATH="slides/$(echo $(echo ${LINK} | cut -b 12-)).${FILE_URL##*.}"
      #curl -o "${FILEPATH}" -s "${FILE_URL}"
      echo $FILEPATHwrite >> kccncVideos.txt

      #if [[ ! -f "${FILEPATH}" ]]; then
       # curl -o "${FILEPATH}" -s "${FILE_URL}"
      #fi
    fi
  done
done
echo "Done and over"

