# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 21:26:37 2018

@author: Yugant
"""

import pandas as pd
import matplotlib.pyplot as plt
import datetime
plt.style.use('ggplot')


data = get_history(symbol="SBIN", start=date(2015,1,1), end=date(2015,1,31))


from datetime import date
from nsepy import get_history
sbin = get_history(symbol='SBIN',
                   start=date(2015,1,1),
                   end=date(2015,1,10))


data.head()
#moving avg for closing stock
rolmean_1 = pd.Series((data['Close']).rolling(window=4).mean())
rolmean_1
rolmean_2 = pd.Series((data['Close']).rolling(window=16).mean())
rolmean_2
rolmean_3 = pd.Series((data['Close']).rolling(window=52).mean())
rolmean_3



# NIFTY Next 50 index
nifty_next50 = get_history(symbol="NIFTY NEXT 50",
                            start=date(2015,1,1),
                            end=date(2015,1,10),
                            index=True)
nifty_next50.head()


#moving avg for indices
rollmean_1=pd.Series((nifty_next50['Close']).rolling(window=4).mean())
rollmean_1

rollmean_2=pd.Series((nifty_next50['Close']).rolling(window=16).mean())
rollmean_2

rollmean_3= pd.Series((nifty_next50['Close']).rolling(window=52).mean())
rollmean_3















#dummy variables
import pandas as pd
from datetime import date
from nsepy import get_history
sbin = get_history(symbol='SBIN',start=date(2015,1,1),end=date(2015,1,10))
sbin
from datetime import date
from nsepy import get_history

s=pd.Series(sbin.iloc[:,-2])

pd.get_dummies(s)







#visualizing
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams


data = get_history(symbol="SBIN", start=date(2015,1,1), end=date(2015,1,31))

data[['Close']].plot()


def plottig(timeseries):
    orig = plt.plot(timeseries, color='blue',label='Original')
    mean = plt.plot(rollmean_, color='red',label='Rolling Mean')
    
plt.title('Rolling Mean')
plt.show(block=False)
