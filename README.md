**YOYOYOYOE**


**Clone Repository**

```bash
git clone https://github.com/101Viper777/AI-Capstone-project/tree/main
```


**Activate Python Environment**

Activate the included Python environment for Jupyter Notebook:

```bash
source env/bin/activate
```


*No need to run the requirements.txt file.*


**Run Code**




## notes

1 chatgpt vision interaction (1 user and 1 ai message is around 16k tokens
1mil / 16k = is roughly 60 question/ answer responses


The average cost per typical interaction with the GPT Vision model is $0.1655 USD

so roughly:
- 1 interaction: $0.1655
- 5 interactions: $0.8274
- 10 interactions: $1.6547
- 20 interactions: $3.3095
- 50 interactions: $8.2736
- 100 interactions: $16.5473

it's only expensive when reading the image and most of the time they will have written work. so to distinguish between written and graph I'm thinking of making it by default use a free OCR model and have the user toggle on when they're drawing something, hence using the GPT-vision model when they are drawing only


also i dont think we need data collection for the tutor but it will only be for the content generation we need to work this out



# costs so far (US)
openai credit - $8.49
claude - $20
