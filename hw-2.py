import sys
from collections import Counter, defaultdict
import math, re
import numpy as np
k0 = 1
k1 = 1
U0 = 10
base_word = "depend"
data_key=0
linedata=["str" for i in range(10000000)]
data=[["str" for i in range(14)] for j in range(10000000)]
c1_ans=["str" for i in range(10000000)]
c1_num=0
sigma=0
average=0
c2_ans=["str" for i in range(10000000)]
c2_num=0
c3_ans=["str" for i in range(10000000)]
c3_num=0
def preprocess(text): 
    processed_data = re.findall(r'\w+', text.lower())
    return processed_data

def _map(text: str):
    global data_key
    tokens = preprocess(text)
    print(tokens)
    if(len(tokens)!=13):
        return
    for i in range(0,13):
        data[data_key][i]=tokens[i]
        if i>1:
            data[data_key][i]=int(data[data_key][i])
    data_key=data_key+1

def C1_filter(base_word):
    global average
    #with open("11.tsv", "a+") as f:
    #    print("%s" % ("HELLO_C1"), file=f)
    print(base_word)
    print(data_key)
    c1_data=[float(-1) for i in range(10000000)]
    k=0
    for i in range(0,data_key):
        with open("pre_c1.tsv", "a+") as f:
            print("%s print(data[i][0])" % ("start"), file=f)
            print("%s print(data[i][0])" % (data[i][0]), file=f)

    
        print(data[i][0])
        if data[i][0]==base_word:
            c1_data[k]=data[i][2]
            average=average+data[i][2]
            with open("pre_c1.tsv", "a+") as f:
                print("%s print(c1_data[k])" % ("start"), file=f)
                print("%s print(data[i][0])" % (c1_data[k]), file=f)
        
            print(c1_data[k])
            k=k+1
    c1_data=np.array(c1_data,dtype = 'float_')
    average=average/(k+1)
    print("average",average)
    global sigma
    sigma=np.std(c1_data[0:k], ddof=0)#.astype(np.float)
    print("sigma",sigma)
    with open("pre_c1.tsv", "a+") as f:
        print("%s print(sigma)" % ("start"), file=f)
        print("%s print(sigma)" % (sigma), file=f)
        
    global c1_num
    for i in range(0,data_key):
        if data[i][0]==base_word and data[i][2]-average>sigma:
            c1_ans[c1_num]=data[i]
            c1_num=c1_num+1
            print("c1_num",c1_num)
    for i in range(0,c1_num):
        with open("C1.tsv", "a+") as f:
            print("%s {strength: %s}" % (c1_ans[i][1],round(float(c1_ans[i][2]-average)/sigma,4)), file=f)
    
        #print (c1_ans[i][1]," strength: ",float(c1_ans[i][2])/sigma)

def weight(a):
    if(a<=7):
        return a-8
    return a-7

def C2_filter(base_word,filtered_by_C1):
    with open("C2.tsv", "a+") as f:
        print("%s" % ("HELLO_C2"), file=f)
    global c1_num
    global c2_num
    global sigma
    global average
    for i in range(0,c1_num):
        amount=0
        #summery=0
        for j in range(3,13):
            amount=amount+c1_ans[i][j]
            #summery=summery+c1_ans[i][j]*weight(j)
        average2=amount/10
        u=0
        for j in range(3,13):
            u=u+(c1_ans[i][j]-average2)*(c1_ans[i][j]-average2)
        u=u/10
        if u>U0 :
            with open("C2.tsv", "a+") as f:
                print("%s {strength: %s spread: %s}" % (c1_ans[i][1],round(float(c1_ans[i][2]-average)/sigma,4),u), file=f)
                
            #print (c1_ans[i][1]," strength: ",float(c1_ans[i][2])/sigma," spread: ",u)
            c2_ans[c2_num]=c1_ans[i]
            c2_ans[c2_num][13]=u
            c2_num=c2_num+1


def C3_filter(base_word,filtered_by_C2):
    with open("C3.tsv", "a+") as f:
        print("%s" % ("HELLO_C3"), file=f)
    global sigma
    global c2_num
    global c3_num
    global average
    c3_num=0
    for i in range(0,c2_num):
        maximum=0
        amount=0
        for j in range(3,13):
            maximum=max(maximum,c2_ans[i][j])
            amount=amount+c2_ans[i][j]
        average2=amount/10
        
        if(maximum>average2+k1*pow(c2_ans[i][13],0.5)):
            #with open("C3.tsv", "a+") as f:
                #print("%sstrength:%sspread:%speak:%scount:%s" % (c1_ans[i][1],float(c1_ans[i][2]-average)/sigma,u,maximum-average2-k1*pow(c2_ans[i][13],0.5),maximum), file=f)
                #print("%s {strength: %s spread: %s peak:%s count:%s }" % (c1_ans[i][1],round(float(c1_ans[i][2]-average)/sigma,4),u,maximum-average2-k1*pow(c2_ans[i][13],0.5), file=f)
            #    print("%s {strength: %s spread: %s peak:%s count:%s }" % (c1_ans[i][1],round(float(c1_ans[i][2]-average)/sigma,4),u,maximum-average2-k1*pow(c2_ans[i][13],0.5), file=f)
                #print (c2_ans[i][1]," strength: ",float(c2_ans[i][2])/sigma," spread: ",c2_ans[i][13]," peak ",maximum-average-k1*pow(c2_ans[i][13],0.5)," count",maximum)
            with open("C3.tsv", "a+") as f:
                print("%s" % ("HELLO_C2"), file=f)    
                print("%s {strength: %s spread: %s peak:%s count:%s }" % (c1_ans[i][1],round(float(c1_ans[i][2]-average)/sigma,4),c2_ans[i][13],(maximum-average2-k1*pow(c2_ans[i][13],0.5)),maximum), file=f)
                
            c3_ans[c3_num]=c2_ans[i]
            c3_num=c3_num+1

def find_strongest_collocation(base_word, filtered_by_C3):
    with open("11.tsv", "a+") as f:
        print("%s" % ("HELLO_find_strongest_collocation"), file=f)
    global sigma
    global c3_num
    strength=0
    count=0
    pointer_i=-1
    pointer_j=-1
    for i in range(0,c3_num):
        for j in range(3,13):
            if((c3_ans[i][2]-average)/sigma>strength or ((c3_ans[i][2]-average)/sigma==strength and c3_ans[i][j]>count)):
                strength=(c3_ans[i][2]-average)/sigma
                count=c3_ans[i][j]
                pointer_i=i
                pointer_j=j
    with open("find.tsv", "a+") as f:
        print("strongest_collocation:%s  %s  %s" % (base_word,c3_ans[pointer_i][1],weight(pointer_j)), file=f)
        #print("strongest_collocation: ",base_word," ",c3_ans[pointer_i][1],weight(pointer_j))
        

if __name__== "__main__" :
    for line in sys.stdin:
        _map(line)
        #with open("11.tsv", "a+") as f:
        #    print("%s" % ("HELLO"), file=f)
    C1_filter(base_word)
    C2_filter(base_word,c1_ans)
    C3_filter(base_word,c2_ans)
    find_strongest_collocation(base_word,c3_ans)