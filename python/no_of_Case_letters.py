from typing import Mapping


def upper_case(s):
    u=0
    for i in s :
        if i.isupper():
            u+=1
    return u

def lower_case(s):
    l=0
    for i in s :
        if i.islower():
            l+=1
    return l

def char_counter(s):
    c=0
    for i in s:
        if i!=' ':
            c+=1
    return c

def word_counter(s):
    if s!='':
        c=1
        for i in s :
          if i==' ':
             c+=1
        return c 
    else :
        return 0





