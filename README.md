**YOYOYOYOE**


**Clone Repository**

```bash
git clone [<repository_url>](https://github.com/101Viper777/AI-Capstone-project/tree/main)
```


**Activate Python Environment**

Activate the included Python environment for Jupyter Notebook:

```bash
source env/bin/activate
```


*No need to run the requirements.txt file.*


**Run Code**




## notes

1 chat interaction (1 user and 1 ai message is around 16k tokens
1mil / 16k = is roughly 60 question/ answer responses


The average cost per typical interaction with the GPT Vision model is $0.1655 USD

so roughly:
- 1 interaction: $0.1655
- 5 interactions: $0.8274
- 10 interactions: $1.6547
- 20 interactions: $3.3095
- 50 interactions: $8.2736
- 100 interactions: $16.5473

its only expensive when reading the image and most of the time they will have writtern work. so to distinguish between writtern and graph im thinking of making it by default use a free ocr model and have the user toggle on when their drawing something, hence using the gpt-vision model when they are drawing only
