def cache_results(func):
    cache = {}  # Dictionary to store previous results

    def wrapper(a, b):
        key = (a, b)  # Use a tuple of arguments as the key
        if key in cache:
            return f"From Cache: {cache[key]}"
        else:
            result = func(a, b)  # Perform the actual computation
            cache[key] = result  # Store in cache
            return f"Computed: {result}"

    return wrapper


@cache_results
def multiply(a: int, b: int) -> int:
    return a * b
