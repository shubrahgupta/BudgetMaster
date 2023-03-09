# BudgetMaster

**09/03/2023** <br>
**Idea:**<br>
This is supposed to be a webapp which can serve as a financial tracker. <br>
I will create a chatbot/NLP model which will be trained on basic terms to classify something as "expense/income/receipt/gibberish" <br>
On the webapp, an input box will be present which can take each line and convert them into some financial statement, <br>
  for e.g. received income --> income <br>
Then we would parse the statement for integer value and accordingly add in a google sheet which would be our financial dashboard <br>
We would later display important info from that excel sheet to the webapp. <br>

Key tasks: 
- [x] Train a chatbot model 
- [ ] Make a webapp
- [ ] Deploy chatbot model to connect with input box
- [ ] Connect input box with google sheet and update the sheet for every input [Task till here is absolutely necessary for the project]
- [ ] How to fetch data from google sheets to the webapp 

Future ideas:
1. Once fully functional for the basic activity, it is important to add user-authentication by google account.
2. Add telegram usage so that user can use speech-to-text feature of Google OS.
3. Also we can provide a feedback to check if we are getting correct categorization in the model as the data initially is limited.
  
