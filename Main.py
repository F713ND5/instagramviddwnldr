#!/usr/bin/env python
# ©Redza Saleh Permana
import requests
import sys
import subprocess
import re
from urllib.request import urlopen

class FBDownloader:
    def __init__(self,link):
        self.link = link
        self.source_code = ''
        self.urlvid = ''
    def requesting(self):
        try:
            r = requests.get(self.link)
            self.source_code = r.text
        except:
            print('ERROR: Pastikan LINK yang anda cantumkan benar!')
            sys.exit(0)
    def findvid(self):
        onlength = self.source_code.find('og:video:secure_url')
        self.urlvid = self.source_code[onlength+30:onlength+30+200]
        try:
            regex = re.compile(r'https://.+nc_cat=\d+')
            matching = regex.search(self.urlvid)
            self.urlvid = matching.group()
        except AttributeError:
            print("ERROR: Pastikan LINK yang anda cantumkan benar!")
            sys.exit(0)
    def finddir(self):
        if sys.platform.startswith('win32'):
            command = 'dir'
            process = subprocess.Popen(command.split(), shell=True, stdout=subprocess.PIPE)
            output, error = process.communicate()
            if str(output).find('Downloaded') < 0:
                command = 'mkdir Downloaded'
                process = subprocess.Popen(command.split(), shell=True, stdout=subprocess.PIPE)
        elif sys.platform.startswith('linux'):
            command = 'ls'
            process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            if output.find('Downloaded'):
                command = 'mkdir Downloaded'
                process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    def download(self):
        filename = input('Download as name: ')
        if filename.find('.mp4') > 0:
            filename = filename
        else:
            filename = filename+'.mp4'
        dwnld = urlopen(self.urlvid)
        with open('Downloaded/'+filename,'wb') as f:
            f.write(dwnld.read())
        print('Downloaded on: Downloaded/'+ filename)

print('|= Rdzsp Instagram Video Downloader =|')
print('|= hanya bisa digunakan di video 1 page =|')
url = input('URL of Video(LINK): ')
download = FBDownloader(url)
download.requesting()
download.finddir()
download.findvid()
download.download()
