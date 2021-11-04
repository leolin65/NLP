#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import groupby
from operator import itemgetter

last_item=[" " for i in range(0,6)]
storage=[[0 for x in range(6)] for y in range(10000000)]
ptr=0; 
output=[[0 for x in range(6)] for y in range(10000000)]
output_amount=0
first=0

def inverted_index_reduce(items1,items2):
    global last_item
    global storage
    global ptr
    global output
    global output_amount
    global first
    if first==0:
        last_item=items1
        first=1
    flag=0;
    for i in range(0,6):
        if(last_item[i]!=items1[i]):
            flag=1
    if flag==1:
        output[output_amount]=last_item
        output_amount=output_amount+1
        for i in range(0,ptr):
            output[output_amount]=storage[i]
            output_amount=output_amount+1
        ptr=1
        last_item=items1
        storage[0]=items2
    else:
        storage[ptr]=items2
        ptr=ptr+1

if __name__ == '__main__':
    import fileinput
    input_file = map(str.split, fileinput.input())
    for line in input_file:
        iterable=line
        iterable_1=[" " for i in range(0,6)]
        iterable_2=[" " for i in range(0,6)]
        for i in range(0,int((len(iterable)-1)/2)):
            iterable_1[i]=iterable[i]
        for i in range(0,int((len(iterable)-1)/2)):
            iterable_2[i]=iterable[i+int((len(iterable)-1)/2)]
        iterable_2[int((len(iterable)-1)/2)]=iterable[len(iterable)-1]
        inverted_index_reduce(iterable_1,iterable_2)
        for i in range(0,output_amount):
            print(output[i][0],output[i][1],output[i][2],output[i][3],output[i][4],output[i][5],end='')
        if output_amount!=0:
            print(" ")
        output_amount=0
    iterable_1=[" " for i in range(0,6)]
    iterable_2=[" " for i in range(0,6)]
    inverted_index_reduce(iterable_1,iterable_2)