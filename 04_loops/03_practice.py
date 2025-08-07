# This function will be tested automatically. 
# Do not change the function name or parameters.
def generate_numbered_tasks(tasks: list[str]) -> list[str]:
	# Write your code below this line
    final=[]
    for index, task in enumerate(tasks, start=1):
        final.append(f"{index}. {task}")
    return final