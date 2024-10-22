def NULL_not_found(obj) -> int:
    """
    Prints the type of 'null-like' values and returns 0 if all goes well,
    or 1 in case of error (i.e., if an unexpected value is passed).
    """
    try:
        if obj is None:
            print(f"Nothing : {type(obj)}")
        elif isinstance(obj, float) and obj != obj:  # NaN is the only value where obj != obj is True
            print(f"Garlic : {type(obj)}")
        elif obj == 0 and type(obj) is int:
            print(f"Zero : {type(obj)}")
        elif obj == '':
            print(f"Empty : {type(obj)}")
        elif obj is False:
            print(f"Fake : {type(obj)}")
        else:
            # If it's not any of the "null-like" values, print a message and return 1 (error).
            print("Brian is in the kitchen : <class 'str'>")
            return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1

    return 0  # Return 0 if everything goes well
