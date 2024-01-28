# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 14:16:49 2024

@author: 8086f
"""

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
  # code here
  def wrap(*arg):
      user1.valid =

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)