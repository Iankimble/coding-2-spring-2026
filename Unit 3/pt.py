# 1. Data Abstraction: A list to store exercise durations
exercise_log = [30, 45, 20]

# 2. Procedure: This contains sequencing, selection, and iteration
def analyze_fitness(log_list):
    total_minutes = 0
    
    # Iteration: Looping through the list
    for minutes in log_list:
        total_minutes += minutes
    
    # Selection: Logical if-statement to provide feedback
    if total_minutes >= 150:
        feedback = "Goal reached! You are meeting weekly CDC guidelines."
    else:
        diff = 150 - total_minutes
        feedback = f"Keep going! You need {diff} more minutes to hit your goal."
    
    return total_minutes, feedback

# 3. Input/Output and Program Flow
def main():
    print("--- Personal Fitness Tracker ---")
    
    # Input: Taking data from the user
    new_entry = int(input("Enter minutes for today's workout: "))
    exercise_log.append(new_entry)
    
    # Calling the procedure with a parameter
    total, msg = analyze_fitness(exercise_log)
    
    # Output: Displaying the result
    print(f"\nTotal minutes logged: {total}")
    print(f"Status: {msg}")

# Run the program
main()