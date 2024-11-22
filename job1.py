# DSMFFINJFAP
def max_profit(jobs):
    
    jobs.sort(key = lambda x: x[1],reverse = True)
    
    max_deadline = max(job[0] for job in jobs)
    slots = [-1]*max_deadline
    total_profit = 0
    
    for deadline,profit in jobs:
        for j in range(min(max_deadline,deadline) -1,-1,-1):
            if slots[j] == -1:
                slots[j] = profit
                total_profit += profit
                break
    return total_profit

n = int(input("Enter the number of jobs"))

jobs = []
for i in range(n):
     deadline = int(input(f"Enter the deadline for the job {i+1}: "))
     profit = int(input(f"Enter the profit for the job {i+1}: ")) 
     jobs.append((deadline,profit))
     
result = max_profit(jobs)
print(f"The maximum profit is {result}")      

            
        
        
        
        
            



            
                
    
    
    
    