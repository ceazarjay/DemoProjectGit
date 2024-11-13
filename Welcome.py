# Welcome message
print("Welcome, everyone, to the GitHub tutorial!")

# Brief task: define a simple function and call it
def introduction_task():
    print("\n--- Python Task ---")
    print("Let’s start by writing a function that adds two numbers!")

    # Sample function
    def add_numbers(a, b):
        return a + b

    # Task: Use the function with example values
    num1 = 5
    num2 = 7
    result = add_numbers(num1, num2)
    print(f"The result of adding {num1} and {num2} is: {result}")
    print(result * 2) #ADDED CHANGE
# Run the task
introduction_task()
