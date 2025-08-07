# Global variable
loyalty_points = 0

def process_transactions(transactions: list[int]) -> int:
    total = sum(transactions)  # sum of all transactions

    def apply_bonus():
        nonlocal total
        if total > 1000:
            total += 50  # Add bonus

    apply_bonus()  # Apply bonus if needed

    global loyalty_points
    points_earned = total // 100
    loyalty_points += points_earned  # update global points

    return total  # Return final amount (after bonus)
