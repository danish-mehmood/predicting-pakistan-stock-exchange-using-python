import pickle

import quandl as qd 
import datetime
import pickle
import pandas as pd 
from sklearn.externals.joblib import dump, load
from sklearn import preprocessing

from sklearn import preprocessing 

qd.ApiConfig.api_key='xyk5HJcTB7AfgKcjE9xa'




def get_future_dates():
      
      dates =[]
# days=[]
      date  = datetime.datetime.now()
      add= datetime.timedelta(days=1)
      for i in range(50):
    
           date=date+add
           day=date.weekday()
#     print(day)
           if day==5 or day==6:
               continue
           else :
               dates.append(date)
      print(len(dates)) 
      weekdays= ['Monday',"Tuesday", "Wednesday", "Thursday" , "Friday"] 
      days=[]
      len(dates)
      for i in range(30):
          day=dates[i].weekday()
    
          days.append(weekdays[day])
      print(days)
      final_dates1=[]
      final_dates2=[]
      final_dates3=[]
      for i in range(10):    
          date = dates[i]
          date='{}-{}-{}'.format(date.year,date.month,date.day)
          final_dates1.append(date)
     
      for i in range(10,20):    
          date = dates[i]
          date='{}-{}-{}'.format(date.year,date.month,date.day)
          final_dates2.append(date)   

      for i in range(20,30):    
          date = dates[i]
          date='{}-{}-{}'.format(date.year,date.month,date.day)
          final_dates3.append(date)

      return final_dates1,final_dates2,final_dates3 




f1 , f2 , f3 =get_future_dates()
# print(f1)
# print(f2)
# print(f3)
# for date in f1 :
      # print(date)



''' ######################################### THE PROCESSES FOR Nestle STARTS HERE ###################'''
def get_nestle_dates_data():
      # ls=[]
      # data = pd.read_csv("nestle.csv")
      # df=data['Date']

      # for i in range(len(df)):
      #     ls.append(df[i])
      # return ls 
      # qd.ApiConfig.api_key = 'ty_xYk5GENzxGxyKYeG6'
      
      date  = datetime.datetime.now()

      enddate = '{}-{}-{}'.format(date.year , date.month,date.day)
      dd = datetime.timedelta(days=30)
      dd2  =datetime.timedelta(days=40)
      dd
      start_date = date-dd
      start_date = start_date-dd2
      start_date = '{}-{}-{}'.format(start_date.year , start_date.month, start_date.day)
      # print(start_date) 
      # print(enddate)
      data = qd.get("PSX/NESTLE", start_date=start_date, end_date=enddate)

      data = data.tail(30)
      nestle_recent = data.tail(1)
      nestle_recent_Open=nestle_recent["Open"].values[0]
      nestle_recent_High=nestle_recent["High"].values[0]
      nestle_recent_Low=nestle_recent["Low"].values[0]
      nestle_recent_Turnover=nestle_recent["Turnover"].values[0]
      nestle_recent_LastDayClose=nestle_recent["Last Day Close"].values[0]

      nestle_yesterday=nestle_recent["Last Day Close"].values[0]
      # nestle_yesterday =yesterday.to_string(index=False)
      
     
      # print(data)
      # print("yesterday : " , yesterday)
      # print("recent " , recent)
      # print("the last is =" ,data.tail(1))
      # print(data)
      return data , nestle_yesterday , nestle_recent_Open,nestle_recent_High,nestle_recent_Low,nestle_recent_Turnover ,nestle_recent_LastDayClose

# get_nestle_dates_data();
data, yesterday , Open , High , Low , Turnover , close = get_nestle_dates_data()
# print(Open , High , Low  , Turnover , close)
# print(data)

# # print(recent['Low'].values[0])
# print("this is the yesterday", yesterday)






def get_nestle_prediction (pass_data):
      
      data=pass_data
      # data =  pd.read_csv('nestle.csv')
      df= data['Last Day Close']


      ls1= [[] for _ in range(10)]
      # ls2= [[] for _ in range(10)]
      # ls3= [[] for _ in range(10)]


# print(ls)

      for i in range(10):
            ls1[i].append(df[i+20])
      # for i in range(10):
      #       ls2[i].append(df[i+10])
      # for i in range(10):
      #       ls3[i].append(df[i])            
      ls1.reverse()
      # ls2.reverse()
      # ls3.reverse()
      # print("list 1 ",ls1)
      # print("leist 2 " , ls2)
      # print("list3",ls3)    

      # print("the list 1 input is  = ", ls1)
      # print("the list 2 input is  = ", ls2)
      # print("the list 3 input is  = ", ls3)
      
      sc=load('nestle_scaler.bin')
      print("the input size is  = " , len(ls1))
      final1  = sc.transform(ls1)
      # final2  = sc.transform(ls2)
      # final3  = sc.transform(ls3)
      # print(final1)
      # print(final2)
      # print(final3)
# print(final)
      filename= 'nestle_original_model.sav'
      loaded_model = pickle.load(open(filename, 'rb'))
# result = loaded_model.score(X_test, Y_test)
      result1= loaded_model.predict(final1)
      result1=abs(result1)

      # result2= loaded_model.predict(final2)
      # result2=abs(result2)

      # result3= loaded_model.predict(final3)
      # result3=abs(result3)
      
      for i in range(len(result1)):
            new = round(result1[i] , 2)
            result1[i]=new
      
      # for i in range(len(result2)):
      #       new = round(result2[i] , 2)
      #       result2[i]=new

      # for i in range(len(result3)):
            # new = round(result3[i] , 2)
            # result3[i]=new      


      return result1 


get_nestle_prediction(data)

# zipped = zip(f1 , res1)
# for d , p in zipped:
#       print(d,p)


def get_nestle_oppurtunity_prediction():
     data, yesterday , Open , High , Low , Turnover , close = get_nestle_dates_data()
     res1 = get_nestle_prediction(data)
#      print(res1)
#      print(res2)
#      print(res3)
     data = qd.get("PSX/NESTLE")
     forecast_out = int(1)
     data['previous day close'] = data['Last Day Close'].shift(forecast_out)
     data = data.tail(1)
     data['next Day Close']= res1[0]
     
# result2=abs(result2)
     data['Day']=0
     data['Day of the year']=1
#      data.reset_index()
#      data = pd.DataFrame(data, index=None)
#      data['Date']=data.index
#      data.index=[1]
     
#      Date = data['Date']
#      Date=str(Date)
#      Date = Date.split('-')
#      print(Date)
#      Date=datetime(int(Date[0]),int(Date[1]),int(Date[2]))
#      Date=datetime.date(Date)
#      data['Day']=Date.weekday()
#      day_of_year = Date.timetuple().tm_yday
#      data['Day of the year']=day_of_year
     filename= 'final_randomforest_model_nestle.sav'
     loaded_model = pickle.load(open(filename, 'rb'))
     Predicted_class= loaded_model.predict(data)
     if Predicted_class[0] == 1:
           predicted_tag = "Very Good"
     elif Predicted_class[0] == 2:
           predicted_tag = "Good"
     elif Predicted_class[0] == 3:
           predicted_tag = "Average"
     elif Predicted_class[0] == 4:
           predicted_tag = "Bad" 

     return predicted_tag           

#      print("class is ",result2)
#      print(data)







# get_nestle_oppurtunity_prediction()




''' ######################################### THE PROCESSES FOR ABBASS STARTS HERE ###################'''


def get_netsol_dates_data():
      # ls=[]
      # data = pd.read_csv("nestle.csv")
      # df=data['Date']

      # for i in range(len(df)):
      #     ls.append(df[i])
      # return ls 
      # qd.ApiConfig.api_key = 'ty_xYk5GENzxGxyKYeG6'
      
      date  = datetime.datetime.now()

      enddate = '{}-{}-{}'.format(date.year , date.month,date.day)
      dd = datetime.timedelta(days=30)
      dd2  =datetime.timedelta(days=40)
      dd
      start_date = date-dd
      start_date = start_date-dd2
      start_date = '{}-{}-{}'.format(start_date.year , start_date.month, start_date.day)
      # print(start_date) 
      # print(enddate)
      data = qd.get("PSX/NETSOL", start_date=start_date, end_date=enddate)
      data = data.tail(30)
      
      netsol_recent = data.tail(1)
      netsol_recent_Open=netsol_recent["Open"].values[0]
      netsol_recent_High=netsol_recent["High"].values[0]
      netsol_recent_Low=netsol_recent["Low"].values[0]
      netsol_recent_Turnover=netsol_recent["Turnover"].values[0]
      netsol_recent_LastDayClose=netsol_recent["Last Day Close"].values[0]

      netsol_yesterday=netsol_recent["Last Day Close"].values[0]
      # nestle_yesterday =yesterday.to_string(index=False)
      
      # print(data)
       
      return data , netsol_yesterday , netsol_recent_Open,netsol_recent_High,netsol_recent_Low,netsol_recent_Turnover ,netsol_recent_LastDayClose

# data = get_netsol_dates_data()
# print(data)
# data = get_nestle_dates_data()



def get_netsol_prediction (pass_data):
      
      data=pass_data
      # data =  pd.read_csv('nestle.csv')
      df= data['Last Day Close']


      ls1= [[] for _ in range(10)]
      ls2= [[] for _ in range(10)]
      ls3= [[] for _ in range(10)]


# print(ls)

      for i in range(10):
            ls1[i].append(df[i+20])
      for i in range(10):
            ls2[i].append(df[i+10])
      for i in range(10):
            ls3[i].append(df[i])            
      ls1.reverse()
      ls2.reverse()
      ls3.reverse()
    #   print(ls)    

      # print("the list 1 input is  = ", ls1)
      # print("the list 2 input is  = ", ls2)
      # print("the list 3 input is  = ", ls3)
      
      sc=load('netsol_scaler.bin')
      # print("the input size is  = " , len(ls1))
      final1  = sc.transform(ls1)
      final2  = sc.transform(ls2)
      final3  = sc.transform(ls3)
      # print(final1)
      # print(final2)
      # print(final3)
# print(final)
      filename= 'netsol_final_model.sav'
      loaded_model = pickle.load(open(filename, 'rb'))
# result = loaded_model.score(X_test, Y_test)
      result1= loaded_model.predict(final1)
      result1=abs(result1)

      result2= loaded_model.predict(final2)
      result2=abs(result2)

      result3= loaded_model.predict(final3)
      result3=abs(result3)
      
      for i in range(len(result1)):
            new = round(result1[i] , 2)
            result1[i]=new
      
      for i in range(len(result2)):
            new = round(result2[i] , 2)
            result2[i]=new

      for i in range(len(result3)):
            new = round(result3[i] , 2)
            result3[i]=new      


      return result1 , result2 , result3

# res , res2 , res3 = get_netsol_prediction(data)
# print(res)
# print(res2)
# print(res3)



def get_netsol_oppurtunity_prediction():
     data, yesterday , Open , High , Low , Turnover , close = get_netsol_dates_data()
     res1 , res2,res3 = get_netsol_prediction(data)
#      print(res1)
#      print(res2)
#      print(res3)
     data = qd.get("PSX/NETSOL")
     forecast_out = int(1)
     data['previous day close'] = data['Last Day Close'].shift(forecast_out)
     data = data.tail(1)
     data['next Day Close']= res1[0]
     
# result2=abs(result2)
     data['Day']=0
     data['Day of the year']=1
#      data.reset_index()
#      data = pd.DataFrame(data, index=None)
#      data['Date']=data.index
#      data.index=[1]
     
#      Date = data['Date']
#      Date=str(Date)
#      Date = Date.split('-')
#      print(Date)
#      Date=datetime(int(Date[0]),int(Date[1]),int(Date[2]))
#      Date=datetime.date(Date)
#      data['Day']=Date.weekday()
#      day_of_year = Date.timetuple().tm_yday
#      data['Day of the year']=day_of_year
     filename= 'final_randomforest_model_netsol.sav'
     loaded_model = pickle.load(open(filename, 'rb'))
     Predicted_class= loaded_model.predict(data)
     if Predicted_class[0] == 1:
           predicted_tag = "Very Good"
     elif Predicted_class[0] == 2:
           predicted_tag = "Good"
     elif Predicted_class[0] == 3:
           predicted_tag = "Average"
     elif Predicted_class[0] == 4:
           predicted_tag = "Bad" 

     return predicted_tag           


tag = get_netsol_oppurtunity_prediction()
# print("thshe tag is =" , tag)




''' ######################################### THE PROCESSES FOR PIA STARTS HERE ###################'''

def get_PIA_dates_data():
      # ls=[]
      # data = pd.read_csv("nestle.csv")
      # df=data['Date']

      # for i in range(len(df)):
      #     ls.append(df[i])
      # return ls 
      # qd.ApiConfig.api_key = 'ty_xYk5GENzxGxyKYeG6'
      
      date  = datetime.datetime.now()

      enddate = '{}-{}-{}'.format(date.year , date.month,date.day)
      dd = datetime.timedelta(days=30)
      dd2  =datetime.timedelta(days=40)
      dd
      start_date = date-dd
      start_date = start_date-dd2
      start_date = '{}-{}-{}'.format(start_date.year , start_date.month, start_date.day)
      # print(start_date) 
      # print(enddate)
      data = qd.get("PSX/PIAA", start_date=start_date, end_date=enddate)
      data = data.tail(30)
      # print(data)
      pia_recent = data.tail(1)
      pia_recent_Open=pia_recent["Open"].values[0]
      pia_recent_High=pia_recent["High"].values[0]
      pia_recent_Low=pia_recent["Low"].values[0]
      pia_recent_Turnover=pia_recent["Turnover"].values[0]
      pia_recent_LastDayClose=pia_recent["Last Day Close"].values[0]

      pia_yesterday=pia_recent["Last Day Close"].values[0]
      # nestle_yesterday =yesterday.to_string(index=False)
      
      # print(data)
       
      return data , pia_yesterday , pia_recent_Open, pia_recent_High, pia_recent_Low, pia_recent_Turnover ,pia_recent_LastDayClose


# data = get_PIA_dates_data()
# print(data)
# data = get_nestle_dates_data()



def get_PIA_prediction (pass_data):
      
      data=pass_data
      # data =  pd.read_csv('nestle.csv')
      df= data['Last Day Close']


      ls1= [[] for _ in range(10)]
      ls2= [[] for _ in range(10)]
      ls3= [[] for _ in range(10)]


# print(ls)

      for i in range(10):
            ls1[i].append(df[i+20])
      for i in range(10):
            ls2[i].append(df[i+10])
      for i in range(10):
            ls3[i].append(df[i])            
    


      ls1.reverse()
      ls2.reverse()
      ls3.reverse()
    #   print(ls)    

      # print("the list 1 input is  = ", ls1)
      # print("the list 2 input is  = ", ls2)
      # print("the list 3 input is  = ", ls3)
      
      sc=load('PIA_scaler.bin')
      # print("the input size is  = " , len(ls1))
      final1  = sc.transform(ls1)
      final2  = sc.transform(ls2)
      final3  = sc.transform(ls3)
      # print(final1)
      # print(final2)
      # print(final3)
# print(final)
      filename= 'PIA_final_model.sav'
      loaded_model = pickle.load(open(filename, 'rb'))
# result = loaded_model.score(X_test, Y_test)
      result1= loaded_model.predict(final1)
      result1=abs(result1)

      result2= loaded_model.predict(final2)
      result2=abs(result2)

      result3= loaded_model.predict(final3)
      result3=abs(result3)
      
      for i in range(len(result1)):
            new = round(result1[i] , 2)
            result1[i]=new
      
      for i in range(len(result2)):
            new = round(result2[i] , 2)
            result2[i]=new

      for i in range(len(result3)):
            new = round(result3[i] , 2)
            result3[i]=new      


      return result1 , result2 , result3


# res , res2 , res3 = get_PIA_prediction(data)
# print(res)
# print(res2)
# print(res3)



def get_PIA_oppurtunity_prediction():
     data, yesterday , Open , High , Low , Turnover , close = get_PIA_dates_data()
     res1 , res2,res3 = get_PIA_prediction(data)
#      print(res1)
#      print(res2)
#      print(res3)
     data = qd.get("PSX/PIAA")
     forecast_out = int(1)
     data['previous day close'] = data['Last Day Close'].shift(forecast_out)
     data = data.tail(1)
     data['next Day Close']= res1[0]
     
# result2=abs(result2)
     data['Day']=0
     data['Day of the year']=1
#      data.reset_index()
#      data = pd.DataFrame(data, index=None)
#      data['Date']=data.index
#      data.index=[1]
     
#      Date = data['Date']
#      Date=str(Date)
#      Date = Date.split('-')
#      print(Date)
#      Date=datetime(int(Date[0]),int(Date[1]),int(Date[2]))
#      Date=datetime.date(Date)
#      data['Day']=Date.weekday()
#      day_of_year = Date.timetuple().tm_yday
#      data['Day of the year']=day_of_year
     filename= 'final_randomforest_model_PIA.sav'
     loaded_model = pickle.load(open(filename, 'rb'))
     Predicted_class= loaded_model.predict(data)
     if Predicted_class[0] == 1:
           predicted_tag = "Very Good"
     elif Predicted_class[0] == 2:
           predicted_tag = "Good"
     elif Predicted_class[0] == 3:
           predicted_tag = "Average"
     elif Predicted_class[0] == 4:
           predicted_tag = "Bad" 

     return predicted_tag           






''' ######################################### THE PROCESSES FOR ALLIED STARTS HERE ###################'''


def get_allied_dates_data():
      # ls=[]
      # data = pd.read_csv("nestle.csv")
      # df=data['Date']

      # for i in range(len(df)):
      #     ls.append(df[i])
      # return ls 
      # qd.ApiConfig.api_key = 'ty_xYk5GENzxGxyKYeG6'
      
      date  = datetime.datetime.now()

      enddate = '{}-{}-{}'.format(date.year , date.month,date.day)
      dd = datetime.timedelta(days=30)
      dd2  =datetime.timedelta(days=40)
      dd
      start_date = date-dd
      start_date = start_date-dd2
      start_date = '{}-{}-{}'.format(start_date.year , start_date.month, start_date.day)
      # print(start_date) 
      # print(enddate)
      data = qd.get("PSX/ABL", start_date=start_date, end_date=enddate)
      data = data.tail(30)
      # print(data)
      allied_recent = data.tail(1)
      allied_recent_Open=allied_recent["Open"].values[0]
      allied_recent_High=allied_recent["High"].values[0]
      allied_recent_Low=allied_recent["Low"].values[0]
      allied_recent_Turnover=allied_recent["Turnover"].values[0]
      allied_recent_LastDayClose=allied_recent["Last Day Close"].values[0]

      allied_yesterday=allied_recent["Last Day Close"].values[0]
      # nestle_yesterday =yesterday.to_string(index=False)
      
      # print(data)
       
      return data , allied_yesterday , allied_recent_Open, allied_recent_High, allied_recent_Low, allied_recent_Turnover , allied_recent_LastDayClose
 

# data = get_allied_dates_data()
# print(data)
# data = get_nestle_dates_data()



def get_allied_prediction (pass_data):
      
      data=pass_data
      # data =  pd.read_csv('nestle.csv')
      df= data['Last Day Close']


      ls1= [[] for _ in range(10)]
      ls2= [[] for _ in range(10)]
      ls3= [[] for _ in range(10)]


# print(ls)

      for i in range(10):
            ls1[i].append(df[i+20])
      for i in range(10):
            ls2[i].append(df[i+10])
      for i in range(10):
            ls3[i].append(df[i])            
    
    #   print(ls)    

      print("the list 1 input is  = ", ls1)
      print("the list 2 input is  = ", ls2)
      print("the list 3 input is  = ", ls3)
      
      sc=load('allied_scaler.bin')
      print("the input size is  = " , len(ls1))
      final1  = sc.transform(ls1)
      final2  = sc.transform(ls2)
      final3  = sc.transform(ls3)
      print(final1)
      print(final2)
      print(final3)
# print(final)
      filename= 'allied_final_model_model.sav'
      loaded_model = pickle.load(open(filename, 'rb'))
# result = loaded_model.score(X_test, Y_test)
      result1= loaded_model.predict(final1)
      result1=abs(result1)

      result2= loaded_model.predict(final2)
      result2=abs(result2)

      result3= loaded_model.predict(final3)
      result3=abs(result3)
      
      for i in range(len(result1)):
            new = round(result1[i] , 2)
            result1[i]=new
      
      for i in range(len(result2)):
            new = round(result2[i] , 2)
            result2[i]=new

      for i in range(len(result3)):
            new = round(result3[i] , 2)
            result3[i]=new      


      return result1 , result2 , result3


# res , res2 , res3 = get_allied_prediction(data)
# print(res)
# print(res2)
# print(res3)




def get_allied_oppurtunity_prediction():
     data, yesterday , Open , High , Low , Turnover , close = get_allied_dates_data()
     res1 , res2,res3 = get_allied_prediction(data)
#      print(res1)
#      print(res2)
#      print(res3)
     data = qd.get("PSX/ABL")
     forecast_out = int(1)
     data['previous day close'] = data['Last Day Close'].shift(forecast_out)
     data = data.tail(1)
     data['next Day Close']= res1[0]
     
# result2=abs(result2)
     data['Day']=0
     data['Day of the year']=1
#      data.reset_index()
#      data = pd.DataFrame(data, index=None)
#      data['Date']=data.index
#      data.index=[1]
     
#      Date = data['Date']
#      Date=str(Date)
#      Date = Date.split('-')
#      print(Date)
#      Date=datetime(int(Date[0]),int(Date[1]),int(Date[2]))
#      Date=datetime.date(Date)
#      data['Day']=Date.weekday()
#      day_of_year = Date.timetuple().tm_yday
#      data['Day of the year']=day_of_year
     filename= 'final_randomforest_model_allied.sav'
     loaded_model = pickle.load(open(filename, 'rb'))
     Predicted_class= loaded_model.predict(data)
     if Predicted_class[0] == 1:
           predicted_tag = "Very Good"
     elif Predicted_class[0] == 2:
           predicted_tag = "Good"
     elif Predicted_class[0] == 3:
           predicted_tag = "Average"
     elif Predicted_class[0] == 4:
           predicted_tag = "Bad" 

     return predicted_tag           



''' ######################################### THE PROCESSES FOR ABBASS STARTS HERE ###################'''



def get_abbs_dates_data():
      # ls=[]
      # data = pd.read_csv("nestle.csv")
      # df=data['Date']

      # for i in range(len(df)):
      #     ls.append(df[i])
      # return ls 
      # qd.ApiConfig.api_key = 'ty_xYk5GENzxGxyKYeG6'
      
      date  = datetime.datetime.now()

      enddate = '{}-{}-{}'.format(date.year , date.month,date.day)
      dd = datetime.timedelta(days=30)
      dd2  =datetime.timedelta(days=40)
      dd
      start_date = date-dd
      start_date = start_date-dd2
      start_date = '{}-{}-{}'.format(start_date.year , start_date.month, start_date.day)
      # print(start_date) 
      # print(enddate)
      data = qd.get("PSX/AABS", start_date=start_date, end_date=enddate)
      
      data = data.tail(30)
      # print(data)
      abbs_recent = data.tail(1)
      abbs_recent_Open=abbs_recent["Open"].values[0]
      abbs_recent_High=abbs_recent["High"].values[0]
      abbs_recent_Low=abbs_recent["Low"].values[0]
      abbs_recent_Turnover=abbs_recent["Turnover"].values[0]
      abbs_recent_LastDayClose=abbs_recent["Last Day Close"].values[0]

      abbs_yesterday=abbs_recent["Last Day Close"].values[0]
      

      # nestle_yesterday =yesterday.to_string(index=False)
      
      # print(data)
       
      return data , abbs_yesterday , abbs_recent_Open,abbs_recent_High,abbs_recent_Low,abbs_recent_Turnover ,abbs_recent_LastDayClose
 

# data = get_abbs_dates_data()
# print(data)
# data = get_nestle_dates_data()



def get_abbs_prediction (pass_data):
      
      data=pass_data
      # data =  pd.read_csv('nestle.csv')
      df= data['Last Day Close']


      ls1= [[] for _ in range(10)]
      ls2= [[] for _ in range(10)]
      ls3= [[] for _ in range(10)]


# print(ls)

      for i in range(10):
            ls1[i].append(df[i+20])
      for i in range(10):
            ls2[i].append(df[i+10])
      for i in range(10):
            ls3[i].append(df[i])            
    
    #   print(ls)    
      ls1.reverse()
      ls2.reverse()
      ls3.reverse()
      print("the list 1 input is  = ", ls1)
      print("the list 2 input is  = ", ls2)
      print("the list 3 input is  = ", ls3)
      
      sc=load('abbs_scaler.bin')
      print("the input size is  = " , len(ls1))
      final1  = sc.transform(ls1)
      final2  = sc.transform(ls2)
      final3  = sc.transform(ls3)
      print(final1)
      print(final2)
      print(final3)
# print(final)
      filename= 'abbass_final_model.sav'
      loaded_model = pickle.load(open(filename, 'rb'))
# result = loaded_model.score(X_test, Y_test)
      result1= loaded_model.predict(final1)
      result1=abs(result1)

      result2= loaded_model.predict(final2)
      result2=abs(result2)

      result3= loaded_model.predict(final3)
      result3=abs(result3)
      
      for i in range(len(result1)):
            new = round(result1[i] , 2)
            result1[i]=new
      
      for i in range(len(result2)):
            new = round(result2[i] , 2)
            result2[i]=new

      for i in range(len(result3)):
            new = round(result3[i] , 2)
            result3[i]=new      


      return result1 , result2 , result3






# res , res2 , res3 = get_abbs_prediction(data)
# print(res)
# print(res2)
# print(res3)




def get_abbs_oppurtunity_prediction():
     data, yesterday , Open , High , Low , Turnover , close = get_abbs_dates_data()
     res1 , res2,res3 = get_abbs_prediction(data)
#      print(res1)
#      print(res2)
#      print(res3)
     data = qd.get("PSX/AABS")
     forecast_out = int(1)
     data['previous day close'] = data['Last Day Close'].shift(forecast_out)
     data = data.tail(1)
     data['next Day Close']= res1[0]
     
# result2=abs(result2)
     data['Day']=0
     data['Day of the year']=1
#      data.reset_index()
#      data = pd.DataFrame(data, index=None)
#      data['Date']=data.index
#      data.index=[1]
     
#      Date = data['Date']
#      Date=str(Date)
#      Date = Date.split('-')
#      print(Date)
#      Date=datetime(int(Date[0]),int(Date[1]),int(Date[2]))
#      Date=datetime.date(Date)
#      data['Day']=Date.weekday()
#      day_of_year = Date.timetuple().tm_yday
#      data['Day of the year']=day_of_year
     filename= 'final_randomforest_model_abbs.sav'
     loaded_model = pickle.load(open(filename, 'rb'))
     Predicted_class= loaded_model.predict(data)
     if Predicted_class[0] == 1:
           predicted_tag = "Very Good"
     elif Predicted_class[0] == 2:
           predicted_tag = "Good"
     elif Predicted_class[0] == 3:
           predicted_tag = "Average"
     elif Predicted_class[0] == 4:
           predicted_tag = "Bad" 

     return predicted_tag           
