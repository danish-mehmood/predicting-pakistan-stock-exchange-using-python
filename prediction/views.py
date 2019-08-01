'''##############################################Imports for data prediction  module ############################################'''

from django.shortcuts import render
from django.http import HttpResponse
from .Predictions import get_nestle_dates_data , get_nestle_prediction 
from .Predictions import get_nestle_oppurtunity_prediction
from .Predictions import get_netsol_oppurtunity_prediction
from .Predictions import get_PIA_oppurtunity_prediction
from .Predictions import get_abbs_oppurtunity_prediction
from .Predictions import get_allied_oppurtunity_prediction
from .Predictions import get_abbs_dates_data , get_abbs_prediction
from .Predictions import get_allied_dates_data , get_allied_prediction
from .Predictions import get_netsol_dates_data , get_netsol_prediction
from .Predictions import get_PIA_dates_data , get_PIA_prediction
from .Predictions import get_future_dates

'''##############################################Imports for news module ############################################'''
from .newsPrediction import get_abbs_news_prediction
from .newsPrediction import get_allied_news_prediction
from .newsPrediction import get_nestle_news_prediction
from .newsPrediction import get_pia_news_prediction
from .newsPrediction import get_netsol_news_prediction


datesTbl1 , datesTbl2 ,datesTbl3 = get_future_dates()

'''getting all the data for nestle'''
nestle_tag= get_nestle_oppurtunity_prediction()
nestle_data , nestle_yesterday , nestle_recent_Open, nestle_recent_High, nestle_recent_Low, nestle_recent_turnover, nestle_recent_close = get_nestle_dates_data()
nestle_result1=get_nestle_prediction(nestle_data)
zipped_nestle1 = zip(datesTbl1 , nestle_result1 )
# zipped_nestle2 = zip(datesTbl2 , nestle_result2 )
# zipped_nestle3 = zip(datesTbl3 , nestle_result3 )


'''getting all the data for abbass'''
abbs_tag= get_abbs_oppurtunity_prediction()
abbs_data , abbs_yesterday , abbs_recent_Open, abbs_recent_High, abbs_recent_Low, abbs_recent_turnover, abbs_recent_close = get_abbs_dates_data()

abbs_result1 , abbs_result2 , abbs_result3 =get_abbs_prediction(abbs_data)
zipped_abbs1 = zip(datesTbl1 , abbs_result1 )
zipped_abbs2 = zip(datesTbl2 , abbs_result2 )
zipped_abbs3 = zip(datesTbl3 , abbs_result3 )



'''getting all the data for allied'''
allied_tag= get_allied_oppurtunity_prediction()
allied_data , allied_yesterday , allied_recent_Open, allied_recent_High, allied_recent_Low, allied_recent_turnover, allied_recent_close = get_allied_dates_data()

allied_result1 , allied_result2 , allied_result3 =get_allied_prediction(allied_data)
zipped_allied1 = zip(datesTbl1 , allied_result1 )
zipped_allied2 = zip(datesTbl2 , allied_result2 )
zipped_allied3 = zip(datesTbl3 , allied_result3 )



'''getting all the data for pia'''
pia_tag= get_PIA_oppurtunity_prediction()
pia_data , pia_yesterday , pia_recent_Open, pia_recent_High, pia_recent_Low, pia_recent_turnover, pia_recent_close = get_PIA_dates_data()

Pia_result1 , Pia_result2 , Pia_result3 =get_PIA_prediction(pia_data)
zipped_pia1 = zip(datesTbl1 , Pia_result1 )
zipped_pia2 = zip(datesTbl2 , Pia_result2 )
zipped_pia3 = zip(datesTbl3 , Pia_result3 )



'''getting all the data for netsol'''
netsol_tag= get_netsol_oppurtunity_prediction()
netsol_data , netsol_yesterday , netsol_recent_Open, netsol_recent_High, netsol_recent_Low, netsol_recent_turnover, netsol_recent_close = get_netsol_dates_data()

netsol_result1 , netsol_result2 , netsol_result3 =get_netsol_prediction(netsol_data)
zipped_netsol1 = zip(datesTbl1 , netsol_result1 )
zipped_netsol2 = zip(datesTbl2 , netsol_result2 )
zipped_netsol3 = zip(datesTbl3 , netsol_result3 )


''' getting news predictions '''

label_abbs, pos , neg , neu  = get_abbs_news_prediction()
label_nestle, pos , neg , neu = get_nestle_news_prediction()
label_pia, pos , neg , neu = get_pia_news_prediction()
label_netsol, pos , neg , neu = get_netsol_news_prediction()
label_allied, pos , neg , neu = get_allied_news_prediction()


def home (request ):
    return render(request , 'prediction/fyp1.html' , 
                  context={"nestle_tag":nestle_tag,"abbs_tag":abbs_tag,"allied_tag":allied_tag,"pia_tag":pia_tag,"netsol_tag":netsol_tag,
                           "zipped_nestle1":zipped_nestle1,"zipped_nestle2":zipped_nestle2,"zipped_nestle3":zipped_nestle3,"nestle_yesterday":nestle_yesterday,
                           "nestle_recent_Open":nestle_recent_Open,"nestle_recent_High":nestle_recent_High,"nestle_recent_Low":nestle_recent_Low,"nestle_recent_turnover":nestle_recent_turnover,"nestle_recent_close":nestle_recent_close,
                           "zipped_abbs1":zipped_abbs1,"zipped_abbs2":zipped_abbs2,"zipped_abbs3":zipped_abbs3,
                           "abbs_recent_Open":abbs_recent_Open,"abbs_recent_High":abbs_recent_High,"abbs_recent_Low":abbs_recent_Low,"abbs_recent_turnover":abbs_recent_turnover,"abbs_recent_close":abbs_recent_close,                           
                           "zipped_pia1":zipped_pia1,"zipped_pia2":zipped_pia2,"zipped_pia3":zipped_pia3,
                           "pia_recent_Open":pia_recent_Open,"pia_recent_High":pia_recent_High,"pia_recent_Low":pia_recent_Low,"pia_recent_turnover":pia_recent_turnover,"pia_recent_close":pia_recent_close,
                           "zipped_netsol1":zipped_netsol1,"zipped_netsol2":zipped_netsol2,"zipped_netsol3":zipped_netsol3,
                           "netsol_recent_Open":netsol_recent_Open,"netsol_recent_High":netsol_recent_High,"netsol_recent_Low":netsol_recent_Low,"netsol_recent_turnover":netsol_recent_turnover,"netsol_recent_close":netsol_recent_close,
                           "zipped_allied1":zipped_allied1,"zipped_allied2":zipped_allied2,"zipped_allied3":zipped_allied3,
                           "allied_recent_Open":allied_recent_Open,"allied_recent_High":allied_recent_High,"allied_recent_Low":allied_recent_Low,"allied_recent_turnover":allied_recent_turnover,"allied_recent_close":allied_recent_close,}
    ) 



# Create your views here.

def news (request ):
    return render(request , 'prediction/news.html' , context ={
"label_abbs":label_abbs,"label_pia":label_pia,"label_allied":label_allied,"label_netsol":label_netsol,"label_nestle":label_nestle
,"pos":pos,"neg":neg,"neu":neu
}) 

