def statistics_decorator(func):
    """
    Decorator function to print statistics of numbers read.
    """
    def wrapper(numbers):
        print("Numbers read:", numbers)
        print("Count of numbers:", len(numbers))
        if numbers:
            print("Average of numbers:", sum(numbers) / len(numbers))
            print("Maximum number:", max(numbers))
        print("-------------------------------------")
    return wrapper

@statistics_decorator
def process_numbers(numbers):
    """
    Function to process numbers and apply the statistics decorator.
    """
    pass  # This function is wrapped by the decorator, so no explicit implementation is needed.

def printStats(t):
    """
    Retrieves data from a text file t and applies a decorator function to print statistics
    for each line of numbers.
    """
    with open(t, 'r') as file:
        for line in file:
            # Convert line of numbers to a list of integers
            numbers = [int(num) for num in line.strip().split()]
            
            # Apply the decorator function to print statistics
            process_numbers(numbers)


printStats('q4.txt')










