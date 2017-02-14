import re

#open the filenamesfile
fnamesname = 'filenamesfile.txt'
handle1 = open(fnamesname)

#open output file that will contain all the 2Nms
fout = open('extractednms_wier.csv','w')

#first row of output file will have titles: pop0 pop1 2N0m0 2N1m1
fout_line1 = 'pop0,pop1,t,q0,q1,q2,2N0m0>1,2N1m1>0\n'
fout.write(fout_line1)

#loop through all filenames
for filename in handle1:
    #find the two pop names from the filename
    pop1 = re.findall(r'(S\S+)S',filename)
    pop2 = re.findall(r'S.(S\S+)_',filename)
    print (pop1[0],pop2[0])
    #strip the enter from EOL and add _out.txt
    filename = re.findall('\S+_',filename)[0]
    filename = filename + 'out.txt'
    #open the file (i.e. output file from Ima2)
    handle2 = open(filename)
    #loop through the outfile
    for line in handle2:
        #find and read the section with the t and q values
        
        #find and read the section with the two 2Nm values
        if line == '\tValue  \t 2N0m0>1\t 2N1m1>0\n':
            line2 = next(handle2)
            line3 = next(handle2)
            line4 = next(handle2)
            print(line4)
            #extract the two Nms from line4
            first=re.findall(r'\s([0-9]+\.[0-9]+)\s',line4)
            second=re.findall(r'[0-9]+\s+([0-9]+\.[0-9]+)',line4)
            print (first,second)
    #write the two pop_names and the two 2Nms to the outfile
    fout_lineX = pop1[0] + ',' + pop2[0] + ',' + first[0] + ',' + second[0] + '\n'
    fout.write(fout_lineX)
    #close the Ima2p file
    handle2.close()
#close the outfile
fout.close()