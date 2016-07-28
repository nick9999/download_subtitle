#!/bin/bash
for i in "$@"
do 
	python /Users/patiln/Documents/Download_subtitles/download_subtitle/download_subtitle.py "$i"
	osascript -e 'display notification "'$i'" with title "Notification Title"'
done
