import datetime
import time
from plyer import notification

# Dictionary to store tasks with reminder times
tasks = {}

# Function to add a new task with user input
def add_task():
    task_name = input("Enter the task name: ")
    reminder_time = input("Enter the reminder time in 24-hour format (HH:MM): ")

    # Validate time format
    try:
        # Check if the entered time is in correct format
        datetime.datetime.strptime(reminder_time, '%H:%M')
        tasks[task_name] = reminder_time
        print(f"Task '{task_name}' added with reminder at {reminder_time}")
    except ValueError:
        print("Invalid time format. Please use HH:MM format.")

# Function to check and send notifications
def check_reminders():
    print("Checking reminders every minute...")
    while True:
        current_time = datetime.datetime.now().strftime('%H:%M')
        print(f"Current time: {current_time}")  # Debugging line to check current time
        
        # Iterate over each task in the tasks dictionary
        for task, reminder_time in list(tasks.items()):
            if current_time == reminder_time:
                # Send notification for the task
                notification.notify(
                    title="Task Reminder",
                    message=f"Time to do: {task}",
                    timeout=10
                )
                print(f"Reminder for '{task}' sent.")  # Debug message
                del tasks[task]  # Remove task after notification

        time.sleep(60)  # Wait for 60 seconds before checking again

# Main loop to add tasks
print("Welcome to the Task Scheduler!")
while True:
    add_task()
    more_tasks = input("Do you want to add another task? (yes/no): ").strip().lower()
    if more_tasks != 'yes':
        print("Starting reminders...")
        break

# Start checking reminders
check_reminders()
