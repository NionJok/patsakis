import random


values =list(range(1,81))
bingo=[]
geniko=0
print("Περιμέντε αρκετή ώρα μέχρι να εμφανιστεί το αποτέλεσμα...")
for i in range (0,1000):
    paiktes=[[]]
    w, h = 5, 100
    paiktes=[[0 for x in range(w)] for y in range(h)]
    flag=False
    metrhths=0
    bingo=[]
    for j in range (0,100):
        for k in range(0,5):
            paiktes[j][k]=random.choice(values)
    while flag==False:
        bingo=[]
        geniko=geniko + 5
        for j in range(0,5):
            bingo.append(random.choice(values))
        for j in range(0,100):
            metrhths=0
            for k in range(0,5):
                for z in range(0,5):
                    if paiktes[j][k]==bingo[z]:
                        metrhths=metrhths+1
            if metrhths==5:
                
                flag=True
                
mesos=(geniko/1000)
print("Χρειάζεται να αναγγελθούν κατά μέσο όρο "+str(mesos)+" αριθμοί ώστε να έχουμε μπίνγκο.")
                
                

            
        
        

        
            
        
                    
                    
                        
                     
         
                                                                                                         
                                                                                                         
        
        
     
