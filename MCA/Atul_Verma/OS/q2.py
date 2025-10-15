# Implement FCFS cpu scheduling algorithm

n = int(input("Enter No. of processes: "))
bt = [] # Burst Time

for i in range(n):
    bt.append(int(input(f"Enter bt for process {i+1}: ")))

wt = [0]*n # Waiting Time
tat = [0]*n # Turn Around Time

for i in range(1,n):
    wt[i] = wt[i-1] + bt[i-1]

for i in  range(n):
    tat[i] = wt[i] + bt[i]


print('\nProcess\tBurst\tWaiting\tTurnaround')
for i in range(n):
    print(f"pr{i+1}\t{bt[i]}\t{wt[i]}\t{tat[i]}")

