import sys
from collections import Counter, defaultdict
import math, re


def preprocess(text): 
    processed_data = re.findall(r'\w+', text.lower())
    return processed_data


def _map(text: str):
    tokens = preprocess(text)
    print(tokens)
    cnt=0
    for num, item in enumerate(tokens):
        print("num,item",num,item)
        tokens[num] = item
        cnt=num
            
    print(tokens[0])
    print(tokens[1])
    print(tokens[2])
        
    # [ TODO ] generate the mapper output
    # Output: "{pivot}\t{word}\t{distance}\t{count}"
    # Example: 
    #   predict is  -3  1
    #   predict used    -2  1
    #   predict the -1  1
    #   predict the 1   1
    #   ...
    #...
    for num, item in enumerate(tokens):
        for i in range(1,6):
            if num+i-6>=0:
                print(tokens[num]," ",tokens[num+i-6]," ",i-6,"1")
        for i in range(1,6):
            if num+i<=cnt:
                print(tokens[num]," ",tokens[num+i]," ",i,"1")
    
if __name__== "__main__" :
    for line in sys.stdin:
        _map(line)
     