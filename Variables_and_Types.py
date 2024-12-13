# Global variable
x = "I am global"

def demonstrate_scope():
    # Local variable
    y = "I am local"
    print("Inside function, global x:", x)  # Accessing global variable
    print("Inside function, local y:", y)  # Accessing local variable

    # Modifying the global variable using the global keyword
    global x
    x = "I am modified globally"
    print("Inside function, modified global x:", x)

# Calling the function
demonstrate_scope()

# Accessing the global variable outside the function
print("Outside function, global x:", x)
