import sys

if __name__== "__main__" :
    k=0
    total=0
    string0=""
    string1=""
    #line="a b c "
    linecount=0
    linedata=["str" for i in range(10000000)]
    a = [0,0,0,0,0,0,0,0,0,0]
    for line in sys.stdin:
        linedata[linecount]=line
        #linedata[linecount]=linedata[linecount].split()
        linecount=linecount+1
    linedata=sorted(linedata[0:linecount])
    for i in range(0,linecount):
        print (linedata[i])
        with open("shuffler.tsv", "a+") as f:
                    #print(string0," ",string1," ",total," ",a[0]," ",a[1]," ",a[2]," ",a[3]," ",a[4]," ",a[5]," ",a[6]," ",a[7]," ",a[8]," ",a[9])
                    print(linedata[i], file=f)            
    for i in range(0,linecount):
        linedata[i]=linedata[i].split()
        if not linedata[i][0]: continue
        # [ TODO ] collect the output from shuffler and generate reducer output
        # Now you need to calculate the skip-gram frequency with its distance information.
        # Input: 
        #   "{pivot}\t{word}\t{distance}\t{count}"
        # Output: 
        #   "{pivot}\t{word}\t{total_freq}\t{-5}\t{-4}\t{-3}\t{-2}\t{-1}\t{1}\t{2}\t{3}\t{4}\t{5}"
        # Example:
        #   See the sample output file given by TA.
        # Steps: 
        #   1) Parse the input from shuffler
        #   2) Check if this is the same skipgram
        #   3) If so, add the frequency according to its distance
        #   4) If not, output the previous skipgram data
        #...
        if k==0 or (linedata[i][0]==string0 and linedata[i][1]==string1):
            #continue
            k=1
            total=total+1
            if linedata[i][2]=="-5":
                a[0]=a[0]+1
            if linedata[i][2]=="-4":
                a[1]=a[1]+1
            if linedata[i][2]=="-3":
                a[2]=a[1]+1
            if linedata[i][2]=="-2":
                a[3]=a[3]+1
            if linedata[i][2]=="-1":
                a[4]=a[4]+1
            if linedata[i][2]=="1":
                a[5]=a[5]+1
            if linedata[i][2]=="2":
                a[6]=a[6]+1
            if linedata[i][2]=="3":
                a[7]=a[7]+1
            if linedata[i][2]=="4":
                a[8]=a[8]+1
            if linedata[i][2]=="5":
                a[9]=a[9]+1
            string0=linedata[i][0]
            string1=linedata[i][1]
        else:
            #print
            with open("reducer.tsv", "a+") as f:
                    #print(string0," ",string1," ",total," ",a[0]," ",a[1]," ",a[2]," ",a[3]," ",a[4]," ",a[5]," ",a[6]," ",a[7]," ",a[8]," ",a[9])
                    print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (string0,string1,total,a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9]), file=f)
            total=1
            for k in range (0,10):
                #print(" ",a[k])
                a[k]=0
            #print("\n")
            if linedata[i][2]=="-5":
                a[0]=a[0]+1
            if linedata[i][2]=="-4":
                a[1]=a[1]+1
            if linedata[i][2]=="-3":
                a[2]=a[1]+1
            if linedata[i][2]=="-2":
                a[3]=a[3]+1
            if linedata[i][2]=="-1":
                a[4]=a[4]+1
            if linedata[i][2]=="1":
                a[5]=a[5]+1
            if linedata[i][2]=="2":
                a[6]=a[6]+1
            if linedata[i][2]=="3":
                a[7]=a[7]+1
            if linedata[i][2]=="4":
                a[8]=a[8]+1
            if linedata[i][2]=="5":
                a[9]=a[9]+1
            string0=linedata[i][0]
            string1=linedata[i][1]
    #print

    with open("reducer.tsv", "a+") as f:
        
        print(string0," ",string1," ",total," ",a[0]," ",a[1]," ",a[2]," ",a[3]," ",a[4]," ",a[5]," ",a[6]," ",a[7]," ",a[8]," ",a[9])        
        print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (string0,string1,total,a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9]), file=f)

    total=1
    for i in range (0,10):
        #print(" ",a[i])
        a[i]=0
    #print("\n")
    total=total+1
    if linedata[linecount-1][2]=="-5":
        a[0]=a[0]+1
    if linedata[linecount-1][2]=="-4":
        a[1]=a[1]+1
    if linedata[linecount-1][2]=="-3":
        a[2]=a[1]+1
    if linedata[linecount-1][2]=="-2":
        a[3]=a[3]+1
    if linedata[linecount-1][2]=="-1":
        a[4]=a[4]+1
    if linedata[linecount-1][2]=="1":
        a[5]=a[5]+1
    if linedata[linecount-1][2]=="2":
        a[6]=a[6]+1
    if linedata[linecount-1][2]=="3":
        a[7]=a[7]+1
    if linedata[linecount-1][2]=="4":
        a[8]=a[8]+1
    if linedata[linecount-1][2]=="5":
        a[9]=a[9]+1
    string0=linedata[i][0]
    string1=linedata[i][1]