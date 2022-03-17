# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup
import re
import sys



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv)>1:
        url = sys.argv[1]
    else:
        sys.exit("Please enter the Ted talk Url")
    r = requests.get(url)
    print("Download about to start")
    soup = BeautifulSoup(r.content,features= "html")
    for val in soup.findAll("script"):
        if (re.search("__NEXT_DATA__",str(val))) is not None:
            result = str(val)
    result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)",result).group("url")
    mp4_url = result_mp4.split('"')[0]+"mp4"
    print("Downloading video from ...." + mp4_url)
    file_name = mp4_url.split("/")[len(mp4_url.split("/"))-1].split('?')[0]
    print("Sorting video in ....." + file_name)
    r = requests.get(mp4_url)
    with open(file_name,'wb') as f:
        f.write(r.content)





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
