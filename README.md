# BudgetMaster

**Idea:**<br>

This is supposed to be a webapp that can serve as a financial tracker. <br>
I will create a chatbot/NLP model which will be trained on basic terms to classify a transaction as "expense/income/receipt/gibberish" <br>
On the webapp, an input box will be present which can take each line and convert them into some financial statement <br>
  for e.g. received income --> income <br>
Then we would parse the statement for integer value and accordingly make a financial dashboard <br>

<br>

Key tasks: 
- [x] Train a chatbot model 
- [x] Make a webapp
- [x] Deploy chatbot model to connect with input box
- [x] Create a decent UI



![budgetMaster_in_action](https://github.com/shubrahgupta/BudgetMaster/assets/50666757/e0da90ea-1779-43ef-a33c-0aa884b5a321)


The server runs on the command

```
uvicorn app:app --reload
```

<br>
Workflow:<br><br>

![BudgetMaster drawio](https://github.com/shubrahgupta/BudgetMaster/assets/50666757/b3ff317f-2869-4cf1-81c3-60c8603849ae)

**21/08/2023** <br>
1. On clicking the button after entering text in the box, a post request was made to the API but a new page was loaded with a JSON response (undesirable, I wanted to get the response without reloading), fixed it by using AJAX, stopped the default button click event, and later triggered it manually.

2. The black responseArea where the text needed to be published, I brought the JSON response there, and then replaced it with a table instead, with one entry filled. To my delight, entering the text in the box and clicking the button every time inserted a new record in the table.


**14/03/2023** <br>
Created a decent UI with a template, need to change the rect(responseArea) to look like a terminal, and the layover text will appear using some effect(search more on this)

**12/03/2023** <br>
A dictionary with components tag, log, amount, and response will be returned through a POST request. <br>
Implemented regex to parse the string and return int, added exception handling to prevent IndexError<br>


**11/03/2023** <br>
Using https://www.kdnuggets.com/2021/04/deploy-machine-learning-models-to-web.html as reference.<br>
We will use FAST API, Uvicorn(a server), and Flask in Python. <br>
Created GET and POST requests and successfully returns the classification of the tag for the input.<br>
<br>

**09/03/2023** <br>
Idea generated, chatbot model trained and tested using NLP


Future ideas:
1. Add telegram usage so that users can use the speech-to-text feature of Google OS in smartphones.
2. Also users can provide feedback to check if we are getting correct categorization in the model as the data initially is limited.
  


Resources:
* Chatbot making: https://www.section.io/engineering-education/creating-chatbot-using-natural-language-processing-in-python/
