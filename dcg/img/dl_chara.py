import urllib.request, urllib.error

for i in range(449):
	link = 'https://img.gamewith.jp/article_tools/destiny-child/gacha/c' + str(i+1).zfill(3) + '_i.png'
	filename = link.split('/')[-1]
	try:
		urllib.request.urlretrieve(link, filename)
	except urllib.error.URLError as e:
		print (str(e.code) + ' : ' + link)