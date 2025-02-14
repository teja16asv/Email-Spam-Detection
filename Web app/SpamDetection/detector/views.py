from django.shortcuts import render

# Create your views here.
import pandas as pd #for handling dataset
from sklearn.feature_extraction.text import CountVectorizer # to convert text to nums
from sklearn.model_selection import train_test_split # for splitting data
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

from .forms import Messageform

dataset=pd.read_csv("E:\Projects\EmailSpam Detection\Dataset\emails.csv")

vectorizer=CountVectorizer()
x=vectorizer.fit_transform(dataset['text'])

x_train,x_test,y_train,y_test=train_test_split(x,dataset['spam'],test_size=0.2)

model=MultinomialNB()
model.fit(x_train,y_train)

def predictMsg(message):
    messageVector=vectorizer.transform([message])
    prediction=model.predict(messageVector)
    return 'Spam' if prediction[0]==1 else 'Ham'

def Home(request):
    result=None
    if request.method =='POST':
        form=Messageform(request.POST)
        if form.is_valid():
            message=form.cleaned_data['text']
            result=predictMsg(message)
    else:
        form=Messageform()
    return render(request, 'home.html', {'form': form, 'result': result})