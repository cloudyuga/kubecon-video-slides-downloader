# Youtube Kubecon-to-markdown  

**How to run?**  
### Getting the Presentation Slides , playlist and making the markdown file.:

- Get the schedule link, exact dates from Sched and presentation playlist of the event from Youtube.

Presentation playlist.
```
eg. Link for Kubecon EU 2022 https://www.youtube.com/playlist?list=PLj6h78yzYM2MCEgkd8zH0vJWF7jdQ-GRR
```


eg. Link for Kubecon22 EU : [https://kccnceu2022.sched.com](https://kccnceu2022.sched.com)

    Dates : "2022-05-16" "2022-05-17" "2022-05-18" "2022-05-19" "2022-05-20"

- You can provide a single date
```
python3 youtuber.py -link https://kccnceu2022.sched.com -d "2022-05-17" 
```
- Or provide multiple dates at once.
```
python3 youtuber.py -link "https://kccnceu2022.sched.com" -d "2022-05-16 2022-05-17 2022-05-18 2022-05-19"
```
### Running the python file.
- Create a virtual environment using `python3 -m venv venv`, where the second venv is the name of the virtual environment
- Activate the virtual environment using `source venv/bin/activate`
- Import all the packages as per requirements.txt (Run `pip3 install -r requirements.txt` in Terminal)
- Run this command `git checkout pull-feature` for getting the corresponding files
- Run `python3 youtuber.py`
- Enter the url of the corresponding playlist you wish to scrape

- Now the output is obtained in the markdown format to get the tabular display on the github repository. [Example](https://github.com/cloudyuga/kubecon19-china)  
- The output file by default is Output_mark.md

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

**Description:**  
This piece of code downloads the slides of presentation and let us iterate through the playlist in youtube to track down the title and respective URLs.
It also prints out the formatting or say template.
In a way which can be copied to github as in markdown language for tabular display.  

### Debugging the file

There are chances that certain presentation files do not get matched with their correct presentation (either because there is a difference in name or some other reasons).
For those conditions you can check the files as follows:
- At the end of python execution you get the total number of files added to markdown.md, you can verify the number with total number of lines in kccncVideos.txt file (names of all slides downloaded by kubecon.sh)
- You can then look for the left out files by executing the commented lines of code (present at the last section of python file).
