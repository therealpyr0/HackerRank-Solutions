#!/bin/python

import sys

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    l=len(password)
    digits=0
    special=0
    lower=0
    upper=0
    specials=list("!@#$%^&*()-+")
    for i in range(l):
        ch=password[i]
        if ch>='a' and ch<='z':
            lower+=1
        if ch>='A' and ch<='Z':
            upper+=1
        if ch>='0' and ch<='9':
            digits+=1
        if ch in specials:
            special+=1
    req=0
    if digits==0:
        req+=1
    if special==0:
        req+=1
    if lower==0:
        req+=1
    if upper==0:
        req+=1
    #print(req)
    if l>=6:
        #print(upper,lower,digits,special)
        return req
    if l<6:
        if req==0:
            return 6-l
        else:
            return max(6-l,req)

if __name__ == "__main__":
    n = int(raw_input().strip())
    password = raw_input().strip()
    answer = minimumNumber(n, password)
    print answer
