def spn_scheduling(processes):
    total_waiting_time = 0
    current_time = 0

    processes.sort(key=lambda x: x[1])  # Sort processes based on burst time

    print("Process execution order (SPN):")

    for process in processes:
        print("Executing Process", process[0])
        total_waiting_time += current_time
        current_time += process[1]

    average_waiting_time = total_waiting_time / len(processes)
    print("\nAverage waiting time:", average_waiting_time)


# Example usage
if __name__ == "__main__":
    processes = [
        ("A", 5),
        ("B", 3),
        ("C", 8),
        ("D", 2)
    ]

    spn_scheduling(processes)
