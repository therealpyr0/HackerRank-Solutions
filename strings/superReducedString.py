#!/bin/python

import sys

def super_reduced_string(s):
    # Complete this function
    alist=list(s)
    temp=[]
    temp.append(s[0])
    for i in range(1,len(s)):
        if len(temp)>0:
            if temp[-1]==s[i]:
                temp.pop(-1)
            else:
                temp.append(s[i])
        else:
            temp.append(s[i])
    if len(temp)>0:
        return "".join(temp)
    else:
        return "Empty String"
s = raw_input().strip()
result = super_reduced_string(s)
print(result)
