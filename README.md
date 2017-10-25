Simple One Click Subtitle Downloader
-----------------------
-----------------------

For Linux Users

Nemo/Nautilus file manager

 * Place file nemo.sh in ~/.gnome2/nemo-scripts and also change the path for download_subtitle as per required
 * Place file nemo.sh in ~/.gnome2/nautilus-scripts and also change the path for download_subtitle as per required
 * Also make sure that script has permissions to allow it execute as a program.
     You can do it by going to **'Properties → Permissions → Allow executing file as program'** 
     or use command **chmod +x name-of-script**
 * Just right click on movie file and click Scripts and then click on nemo.sh(nautilus.sh)

For Mac Users

* Create a workflow in mac so that you can use this as service just by right click on the movie file you will be able to download subtitles for the video file.
* For creating the workflow open Automator in mac by clicking command + space and then add a workflow in the section of files and folder the following picture will help you to do it.
![alt tag](https://github.com/nick9999/download_subtitle/blob/master/Screen%20Shot%202017-02-28%20at%2012.32.25%20AM.png)
* The shell script you can copy from the mac.sh from the file in this repo and change the path for python script as per required.
* Just right click on movie file and click Service and then sub_download (the workflow name) and enjoy the movie with subtitles.
