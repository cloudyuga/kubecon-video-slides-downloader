# Youtube Kubecon-to-markdown  

**How to run?**  
### Getting the Presentation Slides:

- Get the schedule link and exact dates from Sched

eg. Link for Kubecon22 EU : [https://kccnceu2022.sched.com](https://kccnceu2022.sched.com)

    Dates : "2022-05-16" "2022-05-17" "2022-05-18" "2022-05-19" "2022-05-20"

- Execute the kubecon.sh script.
- You have to provide 2 arguments for -u flag (Link of site) 
and -d flag (dates for which you want the slides)
- You can provide a single date
```
./kubecon.sh -u https://kccnceu2022.sched.com -d "2022-05-17" 
```
- Or provide multiple dates at once.
```
./kubecon.sh -u "https://kccnceu2022.sched.com" -a "2022-05-16 2022-05-17 2022-05-18 2022--05-19"
```
It will start downloading the files in slides folder

### Getting the Presentation playlist and making the markdown file.:

Now that you have got Presentation slides it's time to create the markdown file (Presentation title along with Video link and slide link )

- Create a virtual environment using `python3 -m venv venv`, where the second venv is the name of the virtual environment
- Activate the virtual environment using `source venv/bin/activate`
- Import all the packages as per requirements.txt (Run `pip3 install -r requirements.txt` in Terminal)
- Run this command `git checkout pull-feature` for getting the corresponding files
- Run `python3 youtuber.py`
- Enter the url of the corresponding playlist you wish to scrape
```
eg. Link for Kubecon EU 2022 https://www.youtube.com/playlist?list=PLj6h78yzYM2MCEgkd8zH0vJWF7jdQ-GRR
```
- It will ask you to enter the start point of videos 
- Also to enter the end point of videos you wish to get
- Now the output is obtained in the markdown format to get the tabular display on the github repository. [Example](https://github.com/cloudyuga/kubecon19-china)  

**Description:**  
This piece of code let us iterate through the playlist in youtube to track down the title and respective URLs.
It also prints out the formatting or say template.
In a way which can be copied to github as in markdown language for tabular display.  