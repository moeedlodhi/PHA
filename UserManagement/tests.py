from django.test import TestCase
from UserManagement.models import user_roles
import pandas as pd
user_role=pd.read_csv('/home/moeed/Downloads/user_roles.csv')
print(user_role)

for items in user_role:
    print(items)



# Create your tests here.
