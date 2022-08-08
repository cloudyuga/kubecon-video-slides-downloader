from pathlib import Path
import requests
import urllib.request, urllib.error, urllib.parse
from pytube import Playlist
import argparse
from bs4 import BeautifulSoup
import re
import subprocess
import youtube_dl
import os

######## argument parsing - playlist name and length of playlist
parser = argparse.ArgumentParser()
parser.add_argument("-url", "--url", dest = "url",default='0', help="URL of playlist")
parser.add_argument("-link", "--link", dest = "link",default='0', help="URL of slides")

parser.add_argument("-d", "--date", dest = "date",default='0', help="dates of event")

parser.add_argument("-st", "--start", dest = "start", default = 1, help="Start of playlist",type=int)
parser.add_argument("-ed", "--end", dest = "end", default = 0, help="End of Playlist",type=int)

parser.add_argument("-sd", "--slidesD", dest = "slidesD", default = 'slides', help="where slides will be stored")

parser.add_argument("-f", "--folder", dest = "folder", default = 'slides', help="where slides location is to be given in outputfile")

parser.add_argument("-of", "--outputf", dest = "outputf", default = './', help="folder where output will be stored")
parser.add_argument("-ofl", "--Outfile", dest = "Outfile", default = 'README', help="outfile name")

args = parser.parse_args()



SlidesPath=args.slidesD
if not os.path.exists(SlidesPath):
    os.makedirs(SlidesPath)

url=' '+args.url
if args.url=='0':
    #print()
    url=' '+input('please provide url of playlist: ')

folder=args.folder
""" if folder=='0':
    folder = SlidesPath
 """

""" response = requests.get(url)
filename.write_bytes(response.content)
 """
LINK=args.link
if LINK=='0':
    LINK=input('please provide link of slides: ')
DAYS=args.date
if DAYS=='0':
    #print()
    DAYS=input('please provide atleast 1 date: ')
#DAYS="2021-10-15"


#LINK="https://kccncna2021.sched.com/"


os.system('touch kccncSlides.txt')
SlideFile = open('kccncSlides.txt', 'w')

dates = DAYS.split(" ")
for day in dates:
    xd=LINK+day+"/overview"
    
    response = urllib.request.urlopen(xd)
    webContent = response.read().decode('UTF-8')
    soup = BeautifulSoup(webContent,'html.parser')
    for link in soup("a", "name", href=True):
        name=(link['href'][11:])
        FILE_url=LINK+link['href']
        response = urllib.request.urlopen(FILE_url)
        webContent = response.read().decode('UTF-8')
        soup = BeautifulSoup(webContent,'html.parser')

        for link in soup("a", "file-uploaded file-uploaded-pdf", href=True):
            #print(link['href'])
            #print(name,file=SlideFile)

            if re.search(".pdf", link['href']):
                xp=name
                fn=xp+'.pdf'
                os.system('touch '+SlidesPath+'/'+fn)
                filename = Path(SlidesPath+'/'+fn)
                #local_file = xp+'.pdf'

            elif re.search(".pptx", link['href']):
                xp=name
                fn=xp+'.pptx'
                os.system('touch '+SlidesPath+'/'+fn)
                filename = Path(SlidesPath+'/'+fn)
                #local_file = xp+'.pdf'
            response = requests.get(link['href'])
            filename.write_bytes(response.content)
            print(fn,file=SlideFile)



os.system('touch out_test.txt')


start = args.start
end = args.end

######## to check number of videos in playlist
play_list = Playlist(url)
countV=len(play_list)
if end==0:
	end=countV

path = args.outputf

if not os.path.exists(path):
    os.makedirs(path)
filename=args.Outfile
filename = filename + '.md'

SlideFile.close()
#### file for taking the slides name (for matching purposes) and saving of ouputfile.md ####
sourceFile = open(os.path.join(path, filename), 'w')
text_content = open("./kccncSlides.txt", "r")
text_string = text_content.read().replace("\n", " ")
txt = list(text_string.split(" "))
text_content.close()


#url = ' ' + 'https://www.youtube.com/playlist?list=PLj6h78yzYM2MCEgkd8zH0vJWF7jdQ-GRR'
#start = 1
#print("Enter number of videos:")
#end = 245

cmd_code1 = 'python3 -m youtube_dl --no-check-certificate -e --playlist-start ' + \
    str(start)+' --playlist-end '+str(end)+url
print("executed code to fetch title as " + cmd_code1)
title = os.popen(cmd_code1).read().splitlines()

# For fetching the id of that particular video in playlist
cmd_code2 = 'python3 -m youtube_dl --no-check-certificate --get-id --playlist-start ' + \
    str(start)+' --playlist-end '+str(end)+url
video_id = os.popen(cmd_code2).read().splitlines()


print('| Topic        |      Video     |  Presentation |',file=sourceFile)
print('| ------------- |:-------------:| -----:|',file=sourceFile)
slide=0
for i in range(0, len(title)):

	kk = title[i].lower().replace("'", "")
	resy = res = re.findall(r'\w+', kk)

	count=True
	for k in txt:
		resi = re.findall(r'\w+', k.lower())
		if resy[:3] == resi[:3]:
            # print(k)
			#print(k,file=testfile)

			print('|' + title[i] + '|[Watch Here](https://www.youtube.com/watch?v=' +video_id[i]+')|'+'[Slides]('+folder+'/' + k + ')|', file=sourceFile)
			count=False
			slide=slide+1
			break
	if count:
		print('|' + title[i] + '|[Watch Here](https://www.youtube.com/watch?v='+video_id[i]+')|'+'-|',file=sourceFile)
		#pass
		#break
'''
logfile = open('kccncVideos.txt', 'r')
loglist = logfile.readlines()
logfile.close()
logfile1 = open('out_test.txt', 'r')
loglist1 = logfile1.readlines()
logfile1.close()
found = False
print(type(logfile1))

for line in loglist:
    if line in loglist1:
        pass
    else:
        print(line)
    #print(line1)
'''
os.system('rm out_test.txt')
sourceFile.close()
#os.system(('rm kccncVideos.txt'))

print(slide)
