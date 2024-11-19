def log_decorator(func):
    """
    A decorator that logs messages before and after the execution of the given
    function. Works only with functions without arguments.
    """
    def wrapper():
        print(f"Starting execution of {func.__name__}...")
        func()  # Call the original function
        print(f"Finished execution of {func.__name__}.")
    return wrapper


@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")


function_test()
