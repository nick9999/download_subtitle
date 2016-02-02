import hashlib
import os
import sys

PY_VERSION = sys.version_info[0]
#Added support for both versions of python
if PY_VERSION == 3:
    import urllib.request
if PY_VERSION == 2:
    import urllib2


#receives the name of the file and returns the hash code (Cpopied from documentation :P)
def get_hash(file_path):
    read_size = 64 * 1024
    with open(file_path, 'rb') as f:
        data = f.read(read_size)
        f.seek(-read_size, os.SEEK_END)
        data += f.read(read_size)
    return hashlib.md5(data).hexdigest()



def sub_downloader(file_path):
    try:
        root, extension = os.path.splitext(file_path)
        if extension not in [".avi", ".mp4", ".mkv", ".mpg", ".mpeg", ".mov", ".rm", ".vob", ".wmv", ".flv", ".3gp",".3g2"]:
            return

        if not os.path.exists(root + ".srt"):
            headers = {'User-Agent': 'SubDB/1.0 (download_subtitle/1.0; http://github.com/nick9999/download_subtitle.git)'}
            url = "http://api.thesubdb.com/?action=download&hash=" + get_hash(file_path) + "&language=en"
            if PY_VERSION == 3:
                req = urllib.request.Request(url, None, headers)
                response = urllib.request.urlopen(req).read()
            if PY_VERSION == 2:
                req = urllib2.Request(url, '', headers)
                response = urllib2.urlopen(req).read()

            with open(root + ".srt", "wb") as subtitle:
                subtitle.write(response)
    except:
        print("Error in fetching subtitle for " + file_path)
        print("Error", sys.exc_info())


def main():
    root, _ = os.path.splitext(sys.argv[0])

    if len(sys.argv) == 1:
        print("This program requires at least one parameter")
        sys.exit(1)

    for path in sys.argv:
        if os.path.isdir(path):
            for dir_path, _, file_names in os.walk(path):
                for filename in file_names:
                    file_path = os.path.join(dir_path, filename)
                    sub_downloader(file_path)
        else:
            sub_downloader(path)

if __name__ == '__main__':
    main()
