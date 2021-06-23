import pandas as pd
data=pd.read_csv('/home/moeed/Downloads/users_format.csv')
print(data)
import datetime as dt
from UserManagement.models import Users

data['created_at']=pd.to_datetime((data['created_at']).apply(lambda x:
                                    dt.datetime.strptime(x,'%Y-%m-%d %H:%M:%S')))

data['updated_at']=pd.to_datetime((data['updated_at']).apply(lambda x:
                                    dt.datetime.strptime(x,'%Y-%m-%d %H:%M:%S')))

print(data)




