# Youtube Kubecon-to-markdown  
To download the Kubecon talks slides and create a markdown file of KubeCon Youtube videos along with their slides.
This piece of code downloads the slides of presentation and let us iterate through the playlist in youtube to track down the title and respective URLs.
It also prints out the formatting or say template in a way which can be copied to github as in markdown language for tabular display.  

## Getting the Presentation Slides , Youtube Videos Playlist and generating the markdown file
- Youtube Videos playlist
```
eg. Link for Kubecon EU 2022 https://www.youtube.com/playlist?list=PLj6h78yzYM2MCEgkd8zH0vJWF7jdQ-GRR
```
- Presentation link from KubeCon Sched schedule and its dates.
```
eg. Link for Kubecon22 EU : [https://kccnceu2022.sched.com](https://kccnceu2022.sched.com)

Dates : "2022-05-16" "2022-05-17" "2022-05-18" "2022-05-19" "2022-05-20"
```
**NOTE** : Please select dates for KubeCon talks accordingly , not for co-located events. 
## To run the Python code
- Install all the python as per `requirements.txt`  ( Run `pip3 install -r requirements.txt` in Terminal)
- Run `python3 youtuber.py`
- Enter the url of presentation slides (Sched URL of KubeCon) you wish to download (using flag or when the prompt comes)
- Enter the url of the corresponding KubeCon youtube video playlist you wish to scrape

### Entering the dates
- You can provide single or multiple dates of the KubeCon
```
python3 youtuber.py -link https://kccnceu2022.sched.com -d "2022-05-18" 
```
```
python3 youtuber.py -link "https://kccnceu2022.sched.com" -d "2022-05-18 2022-05-19 2022-05-20"
```
- The slides will be downloaded in the `slides` folder repsectively.
- The output will be obtained in the markdown file to get the tabular display of videos and slides, [KubeCon EU 2022](https://github.com/cloudyuga/kubecon-talks/blob/main/Kubecon_EU-22.md)  
- The output file by default is KUBECON.md (you can change it using -ofl tag)

### Flags to be used
| flag tag | description                                   | default value                      |
|----------|-----------------------------------------------|------------------------------------|
| url      | URL of Youtube PlayList                       | Mandatory                          |
| link     | URL of Presentation Slides                    | Mandatory                          |
| d        | Dates of event                                | Mandatory                          |
| st       | Start of playlist to be listed                | 1                                  |
| ed       | End of playlist to be listed                  | Total number of videos in playlist |
| sd       | location of downloaded slides                 | slides folder                      |
| f        | slides location given in output markdown file | slides folder                      |
| of       | Output file storage location                  | Same folder                        |
| ofl      | Output file name                              | README.md                          |

### Debugging the file

There are chances that certain presentation files do not get matched with their correct presentation (either because there is a difference in name or some other reasons).
For those conditions you can check the files as follows:
- At the end of python execution you get the total number of files added to markdown.md, you can verify the number with total number of lines in kccncSlides.txt file (names of all slides being downloaded)
