# This code demonstrates the concept of pass-by-assignment in Python.
def immutable_example():
    """
    Example 1: Pass-by-assignment of immutable objects

    Desctription:
    - Immutable objects include:
        - Integers, floats, booleans
        - Strings
        - Tuples
    - When an immutable object is passed to a function, the function receives 
        a reference to the object.
    - If the function modifies the object, it creates a new object instead of 
        modifying the original object.
    """
    x: int = 10
    print (f"Value of x: {x}")
    print (f"Address of x: {id(x)}")

    def my_func(x: int) -> int:
        """This function returns the square of the input integer."""
        print(f"Value of x in my_func before-cal: {x}")
        print(f"Address of x in my_func before-cal: {id(x)}")
        x = x + 1
        print(f"Value of x in my_func after-cal: {x}")
        print(f"Address of x in my_func after-cal: {id(x)}")

        return x

    my_func(x)
    print(f"Value of x after my_func: {x}")
    print(f"Address of x after my_func: {id(x)}")

# Example 2: Pass-by-assignment of mutable objects
def mutable_example():
    """
    Example 2: Pass-by-assignment of mutable objects

    Description:
    - Mutable objects include:
        - Lists
        - Dictionaries
        - Sets
    - When a mutable object is passed to a function, the function receives 
        a reference to the object.
    - If the function modifies the object, it modifies the original object.
    """
    my_list = [1, 2, 3]
    print(f"Value of my_list: {my_list}")
    print(f"Address of my_list: {id(my_list)}")

    def modify_list(lst: list) -> None:
        """This function appends an element to the input list."""
        print(f"Value of lst in modify_list before-cal: {lst}")
        print(f"Address of lst in modify_list before-cal: {id(lst)}")
        lst.append(4)
        print(f"Value of lst in modify_list after-cal: {lst}")
        print(f"Address of lst in modify_list after-cal: {id(lst)}")

    modify_list(my_list)
    print(f"Value of my_list after modify_list: {my_list}")
    print(f"Address of my_list after modify_list: {id(my_list)}")

# Run the examples
if __name__ == "__main__":
    print("Immutable Example:")
    immutable_example()
    print("\nMutable Example:")
    mutable_example()