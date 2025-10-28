processes = [1, 2, 3]
burst_time = [10, 5, 8]
n = len(processes)

quantum = int(input("Enter Time Quantum: "))

# Copy of burst time to track remaining burst time
remaining_bt = burst_time[:]
time = 0  # Current time

print("\nProcess Execution Order:")

while True:
    done = True

    for i in range(n):
        if remaining_bt[i] > 0:
            done = False
            print(f"P{processes[i]}", end=" -> ")

            if remaining_bt[i] > quantum:
                time += quantum
                remaining_bt[i] -= quantum
            else:
                time += remaining_bt[i]
                remaining_bt[i] = 0
                print(f"(Completed at time {time})")

    if done:
        break
