import quandl as qd 
import datetime
import pickle
import pandas as pd 
from sklearn.externals.joblib import dump, load
from sklearn import preprocessing
from bs4 import BeautifulSoup
import requests
# import unicodecsv as csv
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
sia=SentimentIntensityAnalyzer()
import numpy as np


qd.ApiConfig.api_key='xyk5HJcTB7AfgKcjE9xa'



def get_stocks_data(symbol):
   date = datetime.datetime.now()
   enddate = '{}-{}-{}'.format(date.year , date.month,date.day)
   # enddate
   dd = datetime.timedelta(days=5)
   # dd
   start= date-dd
   # start
   start='{}-{}-{}'.format(start.year , start.month,start.day)
   

   # start
   stock_symbol="PSX/{}".format(symbol)
   data = qd.get(stock_symbol, start_date=start, end_date=enddate)
   data = data.tail(1)
   return data , enddate
   
# stocks , enddate=get_stocks_data("AABS")


def get_dawn_news_data(date):



      url="https://www.dawn.com/archive/{0}".format(date)
      # url='https://www.dawn.com/archive/{}'.format(enddate)
      source2 = requests.get(url).text
      soup2 = BeautifulSoup(source2  , 'lxml') 
      listan=[]   
      for content in soup2.find_all(class_='story__title'):
                    tag= content
                    tag= tag.a.text
                    listan.append(tag)
#                     print(tag)
      listan = listan[0]              
      return listan     

def get_sentiment(stock):
    data , enddate = get_stocks_data(stock)
    sentence = get_dawn_news_data(enddate)

    ps=sia.polarity_scores(sentence)             
    df1=pd.DataFrame()
    df2 =pd.DataFrame(data)

    indexes=[1]
    df1['index']=indexes
    df1['compund']=ps['compound']
    df1['neg']=ps['neg']
    df1['neu']=ps['neu']
    df1['pos']=ps['pos']
    df1['Open']=df2['Open'][0]
    df1['High']=df2['High'][0]
    df1['Low']=df2['Low'][0]
    df1['Last Day Close']=df2['Last Day Close'][0]
    df1['Turnover']=df2['Turnover'][0]
    

    
    print(df1)

    input =[]
    input.append(df1['compund'][0])
    input.append(df1['neg'][0])
    input.append(df1['neu'][0])
    input.append(df1['pos'][0])
    input.append(df1['Open'][0])
    input.append(df1['High'][0])
    input.append(df1['Low'][0])
    input.append(df1['Last Day Close'][0])
    input.append(df1['Turnover'][0])
    pos= df1['pos']
    neg=df1['neg']
    neu=df1['neu']
    return input , pos , neg , neu 



def get_abbs_news_prediction():
     input , pos , neg , neu  = get_sentiment("AABS")

     input=[input]
     listan=[input]
     arrays = np.array(listan)
     arrays=arrays.reshape(1,-1)
     print(arrays)

     filename= 'final_news_classifier_model_for_abbs.sav'
     loaded_model = pickle.load(open(filename, 'rb'))

     prediction=loaded_model.predict(arrays)
    #  print(prediction[0])
     if prediction[0]==1:
         label = "up" 
     if prediction[0]==2:
         label = "down" 
     if prediction[0]==3:
         label = "unchanged"         

     return label, pos , neg , neu 




def get_nestle_news_prediction():
     input , pos , neg , neu = get_sentiment("NESTLE")

     input=[input]
     listan=[input]
     arrays = np.array(listan)
     arrays=arrays.reshape(1,-1)
     print(arrays)

     filename= 'final_news_classifier_model_for_nestle.sav'
     loaded_model = pickle.load(open(filename, 'rb'))

     prediction=loaded_model.predict(arrays)
    #  print(prediction[0])
     if prediction[0]==1:
         label = "up" 
     if prediction[0]==2:
         label = "down" 
     if prediction[0]==3:
         label = "unchanged"         

     return label, pos , neg , neu 







def get_allied_news_prediction():
     input , pos , neg , neu = get_sentiment("ABL")

     input=[input]
     listan=[input]
     arrays = np.array(listan)
     arrays=arrays.reshape(1,-1)
     print(arrays)

     filename= 'final_news_classifier_model_for_allied.sav'
     loaded_model = pickle.load(open(filename, 'rb'))

     prediction=loaded_model.predict(arrays)
    #  print(prediction[0])
     if prediction[0]==1:
         label = "up" 
     if prediction[0]==2:
         label = "down" 
     if prediction[0]==3:
         label = "unchanged"         

     return label, pos , neg , neu 





def get_netsol_news_prediction():
     input, pos , neg , neu  = get_sentiment("NETSOL")

     input=[input]
     listan=[input]
     arrays = np.array(listan)
     arrays=arrays.reshape(1,-1)
     print(arrays)

     filename= 'final_news_classifier_model_for_netsol.sav'
     loaded_model = pickle.load(open(filename, 'rb'))

     prediction=loaded_model.predict(arrays)
    #  print(prediction[0])
     if prediction[0]==1:
         label = "up" 
     if prediction[0]==2:
         label = "down" 
     if prediction[0]==3:
         label = "unchanged"         

     return label, pos , neg , neu 






def get_pia_news_prediction():
     input , pos , neg , neu  = get_sentiment("PIAA")

     input=[input]
     listan=[input]
     arrays = np.array(listan)
     arrays=arrays.reshape(1,-1)
     print(arrays)

     filename= 'final_news_classifier_model_for_pia.sav'
     loaded_model = pickle.load(open(filename, 'rb'))

     prediction=loaded_model.predict(arrays)
    #  print(prediction[0])
     if prediction[0]==1:
         label = "up" 
     if prediction[0]==2:
         label = "down" 
     if prediction[0]==3:
         label = "unchanged"         

     return label, pos , neg , neu 





lable_nestle = get_nestle_news_prediction()
lable_abbs = get_abbs_news_prediction()
lable_netsol = get_netsol_news_prediction()
lable_allied = get_allied_news_prediction()
lable_pia = get_pia_news_prediction()


print(lable_abbs)
print(lable_nestle)
print(lable_netsol)
print(lable_allied)
print(lable_pia)