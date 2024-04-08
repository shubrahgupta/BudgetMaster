import json
import string
import random
import nltk
import numpy as num
from nltk.stem import WordNetLemmatizer  # It has the ability to lemmatize.
# A multidimensional array of elements is represented by this symbol.
import tensorflow as tf
# Sequential groups a linear stack of layers into a tf.keras.Model
from tensorflow.python.keras import Sequential
from tensorflow.python.keras.layers import Dense, Dropout

nltk.download("punkt")  # required package for tokenization
nltk.download("wordnet")  # word database
nltk.download('omw-1.4')


ourData = {"ourIntents": [

    {"tag": "gibberish",
     "patterns": ["hello", "hi", "bye", " whats up", "fuck you", "what's your name?", "who are you?",
                           "how are you doing", "' '", ",", "! @ # $ ^ % & * ( ) - _ = + / . ? > < : ;"],
     "responses": ["Use proper terms such as expense/income/received"]
     },

    {"tag": "income",
     "patterns": ["received income", "company paid me", "got my salary", "received salary", "income arrived", "income", "salary", "earned", "earns"],
     "responses": ["Categorising as income"]
     },
    {"tag": "expense",
     "patterns": ["spent", "purchase", "purchased on", "spent on", "spent for", "lost money", "expense", "lost", "burnt money", "burnt"],
     "responses": ["Categorising as expense"]
     },
    {"tag": "received",
     "patterns": ["received", "got as gift", "gift", "cashback", "got"],
     "responses": ["Categorising as extra received"]
     },
]}


lm = WordNetLemmatizer() #for getting words
# lists
ourClasses = []
newWords = []
documentX = []
documentY = []
# Each intent is tokenized into words and the patterns and their associated tags are added to their respective lists.
for intent in ourData["ourIntents"]:
    for pattern in intent["patterns"]:
        ournewTkns = nltk.word_tokenize(pattern)# tokenize the patterns
        newWords.extend(ournewTkns)# extends the tokens
        documentX.append(pattern)
        documentY.append(intent["tag"])


    if intent["tag"] not in ourClasses:# add unexisting tags to their respective classes
        ourClasses.append(intent["tag"])

newWords = [lm.lemmatize(word.lower()) for word in newWords if word not in string.punctuation] # set words to lowercase if not in punctuation
newWords = sorted(set(newWords))# sorting words
ourClasses = sorted(set(ourClasses))# sorting classes


trainingData = []  # training list array
outEmpty = [0] * len(ourClasses)
# bow model
for idx, doc in enumerate(documentX):
    bagOfwords = []
    text = lm.lemmatize(doc.lower())
    for word in newWords:
        bagOfwords.append(1) if word in text else bagOfwords.append(0)

    outputRow = list(outEmpty)
    outputRow[ourClasses.index(documentY[idx])] = 1
    trainingData.append([bagOfwords, outputRow])

random.shuffle(trainingData)
# coverting our data into an array afterv shuffling
trainingData = num.array(trainingData, dtype=object)

x = num.array(list(trainingData[:, 0]))  # first trainig phase
y = num.array(list(trainingData[:, 1]))  # second training phase

iShape = (len(x[0]),)
oShape = len(y[0])
# # parameter definition
# ourNewModel = Sequential()
# # In the case of a simple stack of layers, a Sequential model is appropriate

# # Dense function adds an output layer
# ourNewModel.add(Dense(128, input_shape=iShape, activation="relu"))
# # The activation function in a neural network is in charge of converting the node's summed weighted input into activation of the node or output for the input in question
# ourNewModel.add(Dropout(0.5))
# # Dropout is used to enhance visual perception of input neurons
# ourNewModel.add(Dense(64, activation="relu"))
# ourNewModel.add(Dropout(0.3))
# ourNewModel.add(Dense(oShape, activation = "softmax"))
# # below is a callable that returns the value to be used with no arguments
# md = tf.keras.optimizers.legacy.Adam(learning_rate=0.01, decay=1e-6)
# # Below line improves the numerical stability and pushes the computation of the probability distribution into the categorical crossentropy loss function.
# ourNewModel.compile(loss='categorical_crossentropy',
#               optimizer=md,
#               metrics=["accuracy"])
# # Output the model in summary
# print(ourNewModel.summary())
# # Whilst training your Nural Network, you have the option of making the output verbose or simple.
# ourNewModel.fit(x, y, epochs=200, verbose=1)
# # By epochs, we mean the number of times you repeat a training set.


def ourText(text):
  newtkns = nltk.word_tokenize(text)
  newtkns = [lm.lemmatize(word) for word in newtkns]
  return newtkns


def wordBag(text, vocab):
  newtkns = ourText(text)
  bagOwords = [0] * len(vocab)
  for w in newtkns:
    for idx, word in enumerate(vocab):
      if word == w:
        bagOwords[idx] = 1
  return num.array(bagOwords)


def Pclass(text, vocab, labels, ourNewModel):
  bagOwords = wordBag(text, vocab)
  ourResult = ourNewModel.predict(num.array([bagOwords]))[0]
  newThresh = 0.2
  yp = [[idx, res] for idx, res in enumerate(ourResult) if res > newThresh]

  yp.sort(key=lambda x: x[1], reverse=True)
  newList = []
  for r in yp:
    newList.append(labels[r[0]])
  return newList


def getRes(firstlist, fJson):
  tag = firstlist[0]
  listOfIntents = fJson["ourIntents"]
  ourResult = None
  for i in listOfIntents:
    if i["tag"] == tag:
      ourResult = random.choice(i["responses"])
      break
  arr = ["log", "response", "tag", "amount"]
  dic = {key: None for key in arr}
  dic["response"] = ourResult
  dic["tag"] = tag
  # arr.append(ourResult)
  # arr.append(tag)
  return dic


# flag = True
# while flag:

#     newMessage = input("")
#     if ("stop" in newMessage) | ("end" in newMessage) | ("exit" in newMessage):
#       flag = False
#       break
#     intents = Pclass(newMessage, newWords, ourClasses, ourNewModel)
#     ourResult = getRes(intents, ourData)
#     print(ourResult)


# model_json = ourNewModel.to_json()
# with open("budgetMaster_chatbot.json", "w") as json_file:
#     json_file.write(model_json)

# ourNewModel.save("budgetMaster_chatbot.h5")
