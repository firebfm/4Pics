import os, sys
from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen, urlretrieve

# Get the url
while True:
	url = input('\nlink of 4chan thread: ')
	try:
		website = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		webpage = urlopen(website)
		break
	except ValueError:
		print('\nInvalid. Consider "http://" in your url')


# Make a folder
while True:
	folderName = input('Put folder name: ')

	try:
		os.mkdir(folderName)
		print('Folder "' + folderName + '" created.')
		break
	except FileExistsError:
		print('Folder "' + folderName + '" already exists.')
	except OSError:
		print("You can\'t name folder " + folderName)

# Look for images
soup = bs(webpage, 'html.parser')
images = []
for img in soup.findAll("a", {"class":"fileThumb"}):
    images.append('http:' + img.get('href'))
print('There are ' + str(len(images)) + ' images here')

# Download and save
os.chdir(folderName)
fileNumber = 1
for image in images:
	try:
		splited = image.split('/')
		print('\nDownloading ' + splited[-1] + '...')
		print('File ' + str(fileNumber) + ' out of ' + str(len(images)))
		urlretrieve(image, splited[-1])
		print('Done.')
		fileNumber += 1
	except KeyboardInterrupt:
		print('Exiting.')
		sys.exit()

print('\nImages are stored in ' + folderName + ' Folder.')
