import os
import hashlib
import sys

TYPE = sys.version_info[0]
#Added support for both versions of python
if TYPE == 3:
    import urllib.request
if TYPE == 2:
    import urllib2


#receives the name of the file and returns the hash code (Cpopied from documentation :P)
def get_hash(req_path):
    read_size = 64 * 1024
    with open(req_path, 'rb') as f:
        data = f.read(read_size)
        f.seek(-read_size, os.SEEK_END)
        data += f.read(read_size)
    return hashlib.md5(data).hexdigest()


#think of more possible extensions are possible
def is_valid_extention(extension):
    possible_extensions=[ ".mp4",".avi", ".mkv",".flv",".mpg", ".mpeg", ".mov", ".vob", ".wmv",".3gp",".3g2"]
    if extension not in possible_extensions:
        return True
    else :
        return False

def download_subtitle(req_path):
    try:
        op_path, extension = os.path.splitext(req_path)
        if is_valid_extention(extension):
            return 

        if not os.path.exists(op_path + ".srt"):
            headers = {'User-Agent': 'SubDB/1.0 (download_subtitle/1.0; http://github.com/nick9999/download_subtitle.git)'}
            url = "http://api.thesubdb.com/?action=download&hash=" + get_hash(req_path) + "&language=en"
            if TYPE == 3:
                req = urllib.request.Request(url, None, headers)
                response = urllib.request.urlopen(req).read()
            if TYPE == 2:
                req = urllib2.Request(url, '', headers)
                response = urllib2.urlopen(req).read()

            with open(op_path + ".srt", "wb") as subtitle:
                subtitle.write(response)
    except:
        print("Could not get subtitle for " + req_path)


def main():
    if len(sys.argv) == 1:
        print("This program requires at least one parameter")
        sys.exit(1)

    for path in sys.argv:

        if os.path.isdir(path):
            # if this is a directory then download subtitles for each file 
            for directory_path, _, file_names in os.walk(path):
                for filename in file_names:
                    req_path = os.path.join(directory_path, filename)
                    download_subtitle(req_path)
        else:
            download_subtitle(path)



if __name__ == '__main__':
    main()
