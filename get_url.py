pic_url = []
with open('./Miley_Cyrus.txt') as f:
    for i in f.readlines():
        pic_url.append(i.strip('\r\n'))

urls = []
for s in pic_url:
    _, _, _, url, _, _ = s.split()
    urls.append(url)

with open('url.data', 'w') as f:
    for i in urls:
        f.write(i)
        f.write('\n')
