import sys
import math, re


def preprocess(text): 
    processed_data = re.findall(r'\w+', text.lower())
    return processed_data


def _map(text: str):
    tokens = preprocess(text)
    #print(tokens)
    cnt=0
    for num, item in enumerate(tokens):
        #print("num,item",num,item)
        tokens[num] = item
        cnt=num
            
        
    # [ TODO ] generate the mapper output
    # Output: "{pivot}\t{word}\t{distance}\t{count}"
    # Example: 
    #   predict is  -3  1
    #   predict used    -2  1
    #   predict the -1  1
    #   predict the 1   1
    #   ...
    #...
    #from __future__ import print_function
    #with open("mapper.tsv", "w") as f:
    for num, item in enumerate(tokens):
        for i in range(1,6):
            if num+i-6>=0:
                with open("mapper.tsv", "a+") as f:
                    #print(tokens[num]," ",tokens[num+i-6]," ",i-6,"1")
                    print("%s\t%s\t%s\t%s" % (tokens[num],tokens[num+i-6],i-6,"1"), file=f)
        for i in range(1,6):            
            if num+i<=cnt:                
                with open("mapper.tsv", "a+") as f:                  
                    #print(tokens[num],'\t',tokens[num+i],'\t',i,"1")
                    print("%s\t%s\t%s\t%s" % (tokens[num],tokens[num+i-6],i-6,"1"), file=f)
    
    
if __name__== "__main__" :
    for line in sys.stdin:
        _map(line)
     