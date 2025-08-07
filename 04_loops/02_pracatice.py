# This function will be tested automatically. 
# Do not change the function name or parameters.
def mark_completed_tasks(tasks: list[str]) -> list[str]:
    # Write your code below this line
    completed = []
    for task in tasks:
        completed.append(f"Completed: {task}")
    return completed
  