# -*- coding: cp1250 -*-
#Go-no go feldolgozo. Elotte file-ok osszefuzese: masold be a windows command promptba ezt a kodot soronkent:
'''
#ez atmasolja a kulon mappaban (path_copy_from helyere masold az utvonalat) levo fajlokat egy nagy mappaba (a Path_destination helyere masold ennek az utvonalat):

md "path_destination"
cd /d "path_copy_from"
for /r %d in (*) do copy "%d" "path_destination"


##merge:

cd "path_destination"
copy *.txt mergedfile.txt

##A fajl lefuttatasa utan masold at az első sort (fejlec) egy uj fulre, aztan jelold ki es ctrl-c-zd az osszes tobbi adatot, majd a fejlc ala transzponalva masold (Paste options - transpose)

'''

#add meg ezeket a valtozokat:

Path_to_your_data = "_gng.txt" ###copy here the path to the merged file
N = 48 #Nr of participants


data = open(Path_to_your_data)
Lines = [] #the list of file's rows
ID = [] #Participant Code
Time = [] #date
MeanPone = [] 
SdPone = [] 
MeanRone = [] 
SdRone   = [] 
MeanPtwo = [] 
SdPtwo = [] 
MeanRtwo = [] 
SdRtwo  = [] 
NPone = [] 
Ponemedian = [] 
MeanPonetime = [] 
SdPonetime   = [] 
NRone = [] 
Ronemedian = [] 
MeanRonetime = [] 
SdRonetime = []
NPtwo = []
Ptwomedian = []
MeanPtwotime = []
SdPtwotime = []
NRtwo  = [] 
Rtwomedian = [] 
MeanRtwotime = [] 
SdRtwotime = [] 
MeanAcc = []


##going through the data seeing if there are any missing Ps or Rs
#it will save us a lot of suffering with shifted lines later on

for line in data:
	Lines.append(line)

for j in range(N):
        #the 19th line of each participant should contain round 1 P accuracy data 
        words = Lines[19+j*45].split()
        if words[0] != "P" or words == []:
                Lines[19+j*45:19+j*45] = ["P	NA	NA	NA	NA" + "\n"]
        #         print("P The new line is " + str(Lines[19+j*45]))
        #the 20th line should be round1 R accuracy
        words = Lines[20+j*45].split()
        if words[0] != "R" or words == []:
                Lines[20+j*45:20+j*45] = ["R	NA	NA	NA	NA" + "\n"]
        #         print("R The new line is " + str(Lines[20+j*45]))
        #line 25 is round2 P acc data
        words = Lines[25+j*45].split()
        if words[0] != "P" or words == []:
                Lines[25+j*45:25+j*45] = ["P	NA	NA	NA	NA" + "\n"]
        #         print("P The new line is " + str(Lines[25+j*45]))
        #line 26 is round2 R acc data
        words = Lines[26+j*45].split()
        if words[0] != "R" or words == []:
                Lines[26+j*45:26+j*45] = ["R	NA	NA	NA	NA" + "\n"]
        #         print("R The new line is " + str(Lines[36+j*45]))
        #34 is P1 RT
        words = Lines[34+j*45].split()
        if words[0] != "P" or words == []:
                Lines[34+j*45:34+j*45] = ["P	NA	NA	NA	NA" + "\n"]
        #         print("P The new line is " + str(Lines[34+j*45]))
        #35 is R1 RT
        words = Lines[35+j*45].split()
        if words[0] != "R" or words == []:
                Lines[35+j*45:35+j*45] = ["R	NA	NA	NA	NA" + "\n"]
        #         print("R The new line is " + str(Lines[35+j*45]))
        ##43 is P2 RT
        words = Lines[43+j*45].split()
        if words[0] != "P" or words == []:
                Lines[43+j*45:43+j*45] = ["P	NA	NA	NA	NA" + "\n"]
        #         print("P The new line is " + str(Lines[43+j*45]))
        #44 is R2 RT
        words = Lines[44+j*45].split()
        if words[0] != "R" or words == []:
                Lines[44+j*45:44+j*45] = ["R	NA	NA	NA	NA" + "\n"]
        #        print("R The new line is " + str(Lines[44+j*45]))

#exporting the corrected data:

f=open('gng_corrected_input.txt','w')
for ele in Lines:
        f.write(ele)
f.write('\n')
f.close()

#overwriting the previous data and Lines

data = open('gng_corrected_input.txt')

Lines = []

for line in data:
	Lines.append(line)


#now extracting the variables and saving them in lists
 
for line in Lines:
        if line.startswith("Subject"):
                words = line.split()       
                ID.append(words[2])
        if line.startswith("Time"):
                words = line.rstrip("Time:")       
                Time.append(words)
        if line.startswith("Mean Accuracy"):
                words = line.split()       
                MeanAcc.append(words[2])


for i in range(N):
        words = Lines[19+i*45].split()
        MeanPone.append(words[3])
        SdPone.append(words[4])
        
        words = Lines[20+i*45].split()
        MeanRone.append(words[3])
        SdRone.append(words[4])
        
        words = Lines[25+i*45].split()    
        MeanPtwo.append(words[3])
        SdPtwo.append(words[4])

        words = Lines[26+i*45].split()
        MeanRtwo.append(words[3])
        SdRtwo.append(words[4])
	
        words = Lines[34+i*45].split()
        NPone.append(words[1])
        Ponemedian.append(words[2])
        MeanPonetime.append(words[3])
        SdPonetime.append(words[4])
		
        words = Lines[35+i*45].split()    
        NRone.append(words[1])
        Ronemedian.append(words[2])
        MeanRonetime.append(words[3])
        SdRonetime.append(words[4])

        words = Lines[43+i*45].split()
        NPtwo.append(words[1])
        Ptwomedian.append(words[2])
        MeanPtwotime.append(words[3])
        SdPtwotime.append(words[4])
		  	
        words = Lines[44+i*45].split()    
        NRtwo.append(words[1])
        Rtwomedian.append(words[2])
        MeanRtwotime.append(words[3])
        SdRtwotime.append(words[4])


print (ID)
print (Time)
print (MeanAcc)
print(MeanPone)
print(SdPone)
print(MeanRone)
print(SdRone)
print(MeanPtwo)
print(SdPtwo)
print(MeanRtwo)
print(SdRtwo)
print(NPone)
print(Ponemedian)
print(MeanPonetime)
print(SdPonetime)
print(NRone)
print(Ronemedian)
print(MeanRonetime)
print(SdRonetime)
print(NPtwo)
print(Ptwomedian)
print(MeanPtwotime)
print(SdPtwotime)
print(NRtwo)
print(Rtwomedian)
print(MeanRtwotime)
print(SdRtwotime)


columnNames = ["ID", "MeanPone", "SdPone", "MeanRone", "SdRone", "MeanPtwo", "SdPtwo", "MeanRtwo", "SdRtwo", "NPone", "Ponemedian", "MeanPonetime", "SdPonetime", "NRone", "Ronemedian", "MeanRonetime", "SdRonetime", "NPtwo", "Ptwomedian", "MeanPtwotime", "SdPtwotime", "NRtwo", "Rtwomedian", "MeanRtwotime", "SdRtwotime", "MeanAcc"]	


columns = [columnNames, ID, MeanPone, SdPone, MeanRone, SdRone, MeanPtwo, SdPtwo, MeanRtwo, SdRtwo, NPone, Ponemedian, MeanPonetime, SdPonetime, NRone, Ronemedian, MeanRonetime, SdRonetime, NPtwo, Ptwomedian, MeanPtwotime, SdPtwotime, NRtwo, Rtwomedian, MeanRtwotime, SdRtwotime, MeanAcc]	

for i in range(len(columns)):
               columns[i].append(columnNames[i])


f=open('gng.csv','w')
for column in columns:
    for ele in column:
        f.write(ele+',')
    f.write('\n')

f.close()

		

