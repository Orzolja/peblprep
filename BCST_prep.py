#BSCT feldolgozo. Elotte file-ok osszefuzese: masold be a windows command promptba ezt a kodot soronkent:
'''
#ez atmasolja a kulon mappaban (path_copy_from helyere masold az utvonalat) levo fajlokat egy nagy mappaba (a Path_destination helyere masold ennek az utvonalat):

md "path_destination"
cd /d "path_copy_from"
for /r %d in (*) do copy "%d" "path_destination"


##merge:

cd "path_destination"
copy *.txt mergedfile.txt

'''

#a _bcst.txt -t javitsd at a te fajlnevedde

#lefutas utan masold at eloszor az elso sort (a valtozok neveit) egy uj excel fulre, utana a tobbit is masold at transzponalva (paste options -- transpose) ala

data = open("_bcst.txt")
colNames = ["ID", "CatComp", "CatExp", "NrTrial", "Correct", "CorrectP", "TError", "TErrorP", "PersResp", "PersRespP", "PersRespPAR", "PersRespPARP", "PersError", "PersErrorP","PersErrorPAR", "PersErrorPARP", "NonPersError","NonPersErrorP",
            "UnError", "UnErrorP", "Cat1stTrial", "Failmaintaining", "Learningtolearn", "CLR", "minpersrun", "percentCLR", "maxpersrun", "meanpersrun", "totalpersrun"]
ID = [] #Participant Code
CatComp = []
CatExp = []
NrTrial = [] #Number of Trials
Correct = [] #Correct Responses
CorrectP = [] #Correct Responses %
TError = [] #Total Errors
TErrorP = [] #Total Errors %
PersResp = [] #Perseverative Responses 
PersRespP = [] #Perseverative Responses %
PersRespPAR = [] #PersResp corrected
PersRespPARP = [] #PersResp corrected %
PersError = [] #Perseverative Errors
PersErrorP = [] #Perseverative Errors %
PersErrorPAR = [] #PersError corrected
PersErrorPARP = [] #PersError corrected %
NonPersError = [] #Non-Perseverative Errors
NonPersErrorP = [] #Non-Perseverative Errors %
UnError = [] #Unique Errors
UnErrorP = [] #Unique Errors %
Cat1stTrial = [] #Trials to complete 1st cat
Failmaintaining = []
Learningtolearn = []
CLR = []
minpersrun = []
percentCLR = []
maxpersrun = []
meanpersrun = []
totalpersrun = []


for line in data:
    if line.startswith(" Participant"):
        words = line.split()       
        ID.append(words[2])
    if line.startswith("1. Categories"):
        words = line.split()       
        CatComp.append(words[3])
        CatExp.append(words[5])
    if line.startswith("2. Number"):
        words = line.split()       
        NrTrial.append(words[4])
    if line.startswith("3. Correct"):
        words = line.split()       
        Correct.append(words[3])
        CorrectP.append(words[4])
    if line.startswith("4. Total"):
        words = line.split()       
        TError.append(words[3])
        TErrorP.append(words[4])
    if line.startswith("5. Perseverative Responses"):
        if line.startswith("5. Perseverative Responses (PAR)"):
            words = line.split()       
            PersRespPAR.append(words[4])
            PersRespPARP.append(words[5])
        elif line.startswith("5. Perseverative Responses (PEBL)"):
            words = line.split()       
            PersResp.append(words[4])
            PersRespP.append(words[5])
        else:
            words = line.split()
            PersResp.append(words[3])
            PersRespP.append(words[4])
    if line.startswith("6. Perseverative Errors"):
        if line.startswith("6. Perseverative Errors    (PAR)"):
            words = line.split()       
            PersErrorPAR.append(words[4])
            PersErrorPARP.append(words[5])
        elif line.startswith("6. Perseverative Errors    (PEBL)"):
            words = line.split()       
            PersError.append(words[4])
            PersErrorP.append(words[5])
        else:
            words = line.split()       
            PersError.append(words[3])
            PersErrorP.append(words[4])
    if line.startswith("7. Non-Perseverative"):
        words = line.split()       
        NonPersError.append(words[3])
        NonPersErrorP.append(words[4])
    if line.startswith("8. Unique"):
        words = line.split()       
        UnError.append(words[3])
        UnErrorP.append(words[4])
    if line.startswith("8b. Trials") or line.startswith("8. Trials"):
        words = line.split()       
        Cat1stTrial.append(words[-1])
    if line.startswith("9. Failure"):
        words = line.split()       
        Failmaintaining.append(words[5])
    if line.startswith("10. Learning"):
        words = line.split()       
        if words[4] == "Not":
            Learningtolearn.append("")
        else:
            Learningtolearn.append(words[4])
    if line.startswith("11. Conceptual"):
        words = line.split()       
        CLR.append(words[4])
        line = next(data)
        words = line.split()
        percentCLR.append(words[2])
    if line.startswith("12. Perseverative"):
       line= next(data)
       words = line.split()
       if words[0] == "no":
           minpersrun.append("0")
           maxpersrun.append("0")
           meanpersrun.append("0")
           totalpersrun.append("0")
       else:
           minpersrun.append(words[0])
           maxpersrun.append(words[1])
           meanpersrun.append(words[2])
           totalpersrun.append(words[-1])
'''print (ID)
print (CatComp)
print (CatExp)
print (NrTrial)
print (Correct)
print (CorrectP)
print (TError)
print (TErrorP)
print (PersResp)
print (PersRespP)
print (PersError)
print (PersErrorP)
print (NonPersError)
print (NonPersErrorP)
print (UnError)
print (UnErrorP)
print (Cat1stTrial)
print (Failmaintaining)
print (Learningtolearn)
print (CLR)
print (percentCLR)
print (minpersrun)
print (maxpersrun)
print(meanpersrun)
print(totalpersrun)'''


columns = [colNames, ID, CatComp, CatExp, NrTrial, Correct, CorrectP, TError, TErrorP, PersResp, PersRespP, PersRespPAR, PersRespPARP, PersError, PersErrorP, PersErrorPAR, PersErrorPARP, NonPersError, NonPersErrorP, UnError, UnErrorP, Cat1stTrial, Failmaintaining, Learningtolearn, CLR, minpersrun, percentCLR, maxpersrun, meanpersrun, totalpersrun]


f=open('bcst.csv','w')
for column in columns:
    for ele in column:
        f.write(ele+',')
    f.write('\n')

f.close()

