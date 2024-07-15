def fcfs_scheduling(arrival_time, burst_time):


    n = len(arrival_time)  # Number of processes

    # Sort the data by arrival time for FCFS scheduling
    sorted_data = sorted(zip(arrival_time, burst_time))
    arrival_time, burst_time = zip(*sorted_data)

    waiting_time = [0] * n  # Initialize waiting times for each process
    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + burst_time[i - 1]  # Calculate waiting time for each process

    response_time = [waiting_time[i] + burst_time[i] for i in range(n)]  # Calculate response time for each process

    # Calculate the average response time (ATT)
    average_response_time = sum(response_time) / n

    return average_response_time


# Test example
arrival_time = [0, 1, 2, 3, 4]
burst_time = [3, 4, 1, 2, 5]

average_response_time = fcfs_scheduling(arrival_time, burst_time)

print(f"Average response time (ATT): {average_response_time}")


#Average response time (ATT): 8.6
