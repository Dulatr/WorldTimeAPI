import requests as req
import json

from WorldTimeAPI.schemas import *
from WorldTimeAPI.service import Client

payload = {"area":"EST"}

myclient = Client('timezone')

r = myclient.get(**payload)

if isinstance(r,ErrorJson):
    print(r.errMsg)
elif isinstance(r,DateTimeJson):
    print(r.datetime)

