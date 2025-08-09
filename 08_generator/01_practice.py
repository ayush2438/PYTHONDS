def token_dispenser(start: int = 1):
    """
    Infinite generator that simulates a token dispenser.
    
    - Yields incrementing token numbers starting from start.
    - Accepts input via send() to optionally reset the counter to a new value.
    - Gracefully stops if close() is called.
    """
    current = start
    try:
        while True:
            new_value = yield current
            if new_value is not None:
                current = new_value
            else:
                current += 1
    except GeneratorExit:
        print("Dispenser closed.")
