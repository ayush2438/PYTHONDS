
# This function will be tested automatically. Do not change the function name or parameter type.
def multiplication_table(number: int) -> list[str]:
    result = []
    for i in range(1, 11):
        result.append(f"{number} x {i} = {number * i}")
    return result