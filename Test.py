job = []
didJob = set()


for i in range(int(input())): #예제 1 에서는 2가 들어감
    job.append(input()) # Hero와 Paladin이 들어감
    
for i in range(int(input())): # 1이 들어감
    didJob.update([input()]) # Hero 들어감
    

for i in list(didJob):
    if i in job: 
        job.remove(i)
    
    
print(len(job))
for i in job:
  print(i)