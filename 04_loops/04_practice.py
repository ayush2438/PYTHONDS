# This function will be tested automatically. 
# Do not change the function name or parameters.
def generate_score_report(names: list[str], scores: list[int]) -> list[str]:
    # Write your code below this line
    
    new=[]
    for name, score in zip(names, scores):
        new.append(f"{name} scored {score} marks") 
    return new