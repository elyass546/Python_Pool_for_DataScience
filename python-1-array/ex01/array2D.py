def slice_me(family: list, start: int, end: int) -> list:
    # Check if 'family' is a 2D list
    if not isinstance(family, list) or not all(
            isinstance(row, list) for row in family):
        print("Error: Input should be a 2D list.")
        exit()

    # Check if the list is empty or if the sublists are empty
    if not family or any(len(row) == 0 for row in family):
        print("Error: The 2D list should not be empty.")
        exit()

    first_shape = len(family)
    second_shape = len(family[0])

    if not all(len(row) == second_shape for row in family):
        print("Error: All rows must have the same number of columns.")
        exit()

    # Handle negative slicing indices (Python allows negative indexing)
    if end < 0:
        end = first_shape + end

    # Print the shape of the original 2D array
    print(f"My shape is : ({first_shape}, {second_shape})")

    # Slice the array based on 'start' and 'end'
    truncated = family[start:end]

    # Print the shape of the new truncated array
    new_shape = (len(truncated), second_shape)
    print(f"My new shape is : {new_shape}")

    # Return the truncated version of the array
    return truncated
