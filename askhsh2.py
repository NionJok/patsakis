import requests
import datetime

today = datetime.datetime.now().strftime("%d")
month = datetime.datetime.now().strftime("%m")
year = datetime.datetime.now().strftime("%Y")
numbers = []
mera = []
main_api = 'http://applications.opap.gr/DrawsRestServices/kino/drawDate/'

num = int(input("Δώστε τον πρώτο αριθμό"))
numbers.append(num)
num = int(input("Δώστε τον δεύτερο αριθμό"))
numbers.append(num)
num = int(input("Δώστε τον τρίτο αριθμό"))
numbers.append(num)
num = int(input("Δώστε τον τέταρτο αριθμό"))
numbers.append(num)
num = int(input("Δώστε τον πέμπτο αριθμό"))
numbers.append(num)
num = int(input("Δώστε τον έκτο αριθμό"))
numbers.append(num)
num = int(input("Δώστε τον έβδομο αριθμό"))
numbers.append(num)
num = int(input("Δώστε τον όγδοο αριθμό"))
numbers.append(num)
num = int(input("Δώστε τον ένατο αριθμό"))
numbers.append(num)
num = int(input("Δώστε τον δέκατο αριθμό"))
numbers.append(num)
arithmoi = 0
for k in range(0, int(today)):
    mera.append(0)

for i in range(1,int(today)+1):
    url = main_api +str(i)+"-"+str(month)+"-"+str(year)+".json"
    json_data = requests.get(url).json()
    for j in json_data ["draws"]["draw"]:
            for z in range (0,10):
                for p in range (0, 20):
                    if (j['results'][p] == numbers [z]):
                        arithmoi = arithmoi + 1
            if arithmoi >= 4:
                mera[i-1]= mera[i-1] + 1
            arithmoi=0    
success = max(mera)
flag=0
i=0
while flag==0:
    if success==mera[i]:
        flag=i+1
    i+=1    
print ("Η μέρα που θα είχες τις περισσότερες επιτυχίες στο KINO για αυτόν τον μήνα(μέχρι σήμερα) είναι η "+str(flag)+"η.")

                           
                        

                            
            


                    
                
                
            
        
    
    
        
        
        
        
        
    



