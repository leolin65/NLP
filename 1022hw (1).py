import sys
from collections import Counter, defaultdict
import math, re
import numpy as np
k0 = 1
k1 = 1
U0 = 3
base_word = "avoid"
data_key=0
linedata=["str" for i in range(1000)]
data=[["str" for i in range(14)] for j in range(1000)]
c1_ans=["str" for i in range(1000)]
c1_num=0
sigma=0
c2_ans=["str" for i in range(1000)]
c2_num=0
c3_ans=["str" for i in range(1000)]
c3_num=0
def preprocess(text): 
    processed_data = re.findall(r'\w+', text.lower())
    return processed_data

def _map(text: str):
    global data_key
    tokens = preprocess(text)
    print(tokens)
    for i in range(0,13):
        data[data_key][i]=tokens[i]
        if i>1:
            data[data_key][i]=int(data[data_key][i])
    data_key=data_key+1

def C1_filter(base_word):
    print(base_word)
    print(data_key)
    c1_data=[float(-1) for i in range(1000)]
    k=0
    for i in range(0,data_key):
        print(data[i][0])
        if data[i][0]==base_word:
            c1_data[k]=data[i][2]
            print(c1_data[k])
            k=k+1
    c1_data=np.array(c1_data,dtype = 'float_')
    global sigma
    sigma=np.std(c1_data[0:k], ddof=0)#.astype(np.float)
    print(sigma)
    global c1_num
    for i in range(0,data_key):
        if data[i][0]==base_word and data[i][2]>sigma:
            c1_ans[c1_num]=data[i]
            c1_num=c1_num+1
    for i in range(0,c1_num):
        print (c1_ans[i][1]," strength: ",float(c1_ans[i][2])/sigma)

def weight(a):
    if(a<=7):
        return a-8
    return a-7

def C2_filter():
    global c1_num
    global c2_num
    global sigma
    for i in range(0,c1_num):
        amount=0
        #summery=0
        for j in range(3,13):
            amount=amount+c1_ans[i][j]
            #summery=summery+c1_ans[i][j]*weight(j)
        average=amount/10
        u=0
        for j in range(3,13):
            u=u+(c1_ans[i][j]-average)*(c1_ans[i][j]-average)
        u=u/10
        if u>U0 :
            print (c1_ans[i][1]," strength: ",float(c1_ans[i][2])/sigma," spread: ",u)
            c2_ans[c2_num]=c1_ans[i]
            c2_ans[c2_num][13]=u
            c2_num=c2_num+1


def C3_filter():
    global sigma
    global c2_num
    global c3_num
    c3_num=0
    for i in range(0,c2_num):
        maximum=0
        amount=0
        for j in range(3,13):
            maximum=max(maximum,c2_ans[i][j])
            amount=amount+c2_ans[i][j]
        average=amount/10
        
        if(maximum>average+k1*pow(c2_ans[i][13],0.5)):
            print (c2_ans[i][1]," strength: ",float(c2_ans[i][2])/sigma," spread: ",c2_ans[i][13]," peak ",maximum-average-k1*pow(c2_ans[i][13],0.5)," count",maximum)
            c3_ans[c3_num]=c2_ans[i]
            c3_num=c3_num+1

def find_strongest_collocation():
    global sigma
    global c3_num
    strength=0
    count=0
    pointer_i=-1
    pointer_j=-1
    for i in range(0,c3_num):
        for j in range(3,13):
            if(c3_ans[i][2]/sigma>strength or (c3_ans[i][2]/sigma==strength and c3_ans[i][j]>count)):
                strength=c3_ans[i][2]/sigma
                count=c3_ans[i][j]
                pointer_i=i
                pointer_j=j
    print("strongest_collocation: ",base_word," ",c3_ans[pointer_i][1],weight(pointer_j))

if __name__== "__main__" :
    for line in sys.stdin:
        _map(line)
    C1_filter(base_word)
    C2_filter()
    C3_filter()
    find_strongest_collocation()