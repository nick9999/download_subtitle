IFS_BAK=$IFS
IFS="
"

for line in $NEMO_SCRIPT_SELECTED_FILE_PATHS; do
        full_path="/home/"$USER"/Documents/download_subtitle/"download_subtitle.py
        python $full_path $line 
        notify-send $line
done

IFS=$IFS_BAK

