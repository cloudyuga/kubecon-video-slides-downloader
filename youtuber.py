import youtube_dl
import os
import re

os.system('touch Output_mark.md')
sourceFile = open('Output_mark.md', 'w')

os.system('touch out_test.txt')

testfile = open('out_test.txt', 'w')
text_content = open("./kccncVideos.txt", "r")
text_string = text_content.read().replace("\n", " ")

print("Enter the url:")
url=' '+input()
print("Enter starting point of videos:")
start = int(input())
print("Enter number of videos:")
end = int(input())


#url = ' ' + 'https://www.youtube.com/playlist?list=PLj6h78yzYM2MCEgkd8zH0vJWF7jdQ-GRR'
#start = 1
#print("Enter number of videos:")
#end = 245

cmd_code1 = 'python3 -m youtube_dl --no-check-certificate -e --playlist-start ' + \
    str(start)+' --playlist-end '+str(end)+url
print("executed code to fetch title as " + cmd_code1)
title = os.popen(cmd_code1).read().splitlines()
# print(title[0])

# For fetching the id of that particular video in playlist
cmd_code2 = 'python3 -m youtube_dl --no-check-certificate --get-id --playlist-start ' + \
    str(start)+' --playlist-end '+str(end)+url
video_id = os.popen(cmd_code2).read().splitlines()


txt = list(text_string.split(" "))
text_content.close()


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
			print(k,file=testfile)

			print('|' + title[i] + '|[Watch Here](https://www.youtube.com/watch?v=' +video_id[i]+')|'+'[Slides](slides/' + k + ')|', file=sourceFile)
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
print(slide)
