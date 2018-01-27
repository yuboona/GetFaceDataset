import urllib.request as request
import socket
import os


# make a dir to save pics
os.mkdir('./img')


# set the timeout for photos  couldn't be fetched
timeout = 20
socket.setdefaulttimeout(timeout)


# read all the urls from .txt
urls = []
with open('./url.data') as f:
    for i in f.readlines():
        if i != '':
            urls.append(i)
        else:
            pass


# requests gets the all imgs
bad_url = []
count = 1
for url in urls:
    url.rstrip('\n')
    print(url)
    try:
        pic = request.urlretrieve(url, './img/%d.jpg' % count)
        print('pic %d' % count)
        count += 1
    except Exception as e:
        print(Exception, ':', e)
        bad_url.append(url)
    print('\n')
print('got all photos that can be got')


# save the photos urls not being fetched
with open('bad_url.data', 'w') as f:
    for i in bad_url:
        f.write(i)
        f.write('\n')
    print('saved bad urls')
