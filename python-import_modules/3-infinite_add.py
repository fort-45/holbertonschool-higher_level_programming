#!/usr/bin/python3
import sys
def infinite_add():
    total_sum = 0
    # sys.argv[1:] creates a slice that includes only the arguments, 
    # skipping the script name (sys.argv[0]).
    arguments = sys.argv[1:]
    
    # Iterate through the argument strings
    for arg_string in arguments:
        # Cast the string argument to an integer and add it to the total sum
        try:
            number = int(arg_string)
            total_sum += number
        except ValueError:
            # According to the prompt, we can assume all arguments are integers,
            # but this structure is good practice for safety.
            pass

    # Print the final result followed by a new line
    print(total_sum)

if __name__ == "__main__":
    infinite_add()
