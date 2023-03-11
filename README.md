# BudgetMaster

**Idea:**<br>

This is supposed to be a webapp which can serve as a financial tracker. <br>
I will create a chatbot/NLP model which will be trained on basic terms to classify something as "expense/income/receipt/gibberish" <br>
On the webapp, an input box will be present which can take each line and convert them into some financial statement, <br>
  for e.g. received income --> income <br>
Then we would parse the statement for integer value and accordingly add in a google sheet which would be our financial dashboard <br>
We would later display important info from that excel sheet to the webapp. <br>

Key tasks: 
- [x] Train a chatbot model 
- [x] Make a webapp
- [x] Deploy chatbot model to connect with input box
- [ ] Create a decent UI
- [ ] Connect input box with google sheet and update the sheet for every input [Task till here is absolutely necessary for the project]
- [ ] How to fetch data from google sheets to the webapp 

**11/03/2023** <br>
Using https://www.kdnuggets.com/2021/04/deploy-machine-learning-models-to-web.html as reference.<br>
We will use FAST API, Uvicorn(a server) and Flask in Python. <br>
Created GET and POST request and successfully returns the classification of the tag for the input.<br>
<br>
Server runs on the command

```
uvicorn app:app --reload
```

**09/03/2023** <br>
Idea generated, chatbot model trained and tested using NLP


Future ideas:
1. Once fully functional for the basic activity, it is important to add user-authentication by google account.
2. Add telegram usage so that user can use speech-to-text feature of Google OS.
3. Also we can provide a feedback to check if we are getting correct categorization in the model as the data initially is limited.
  


Resources:
* Chatbot making: https://www.section.io/engineering-education/creating-chatbot-using-natural-language-processing-in-python/
