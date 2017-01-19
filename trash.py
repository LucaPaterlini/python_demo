from mongoengine import *
from datetime import datetime
s=map(int,raw_input().split())
print datetime(*s)

