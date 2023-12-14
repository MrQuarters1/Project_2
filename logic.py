def valid_input(input):
    """
    :param input: string from lineedit
    function that changes the input into integer and returns error if input is a string or a negative
    :return none:
    """
    try:
        input = int(input)
        if input > 0:
            return input
        else:
            return ValueError
    except:
        return TypeError


