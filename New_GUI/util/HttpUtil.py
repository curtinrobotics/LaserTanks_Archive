def validateRequest(request, *args):
    """Used to validate that the specified fields have been set
    request:    Flask.request object. Holds the data we wish to validate
    *args:  A list of strings that this function checks to see if they exist.
            If they don't all exist, a NameError exception is raised.
    Raises: A NameError exception if one or more key names n args don't exist.
    Returns: nothing
    """
    for arg in args:
        if request.data[str(arg)] == None:
            raise NameError("Argument '{arg}' not found :(")
    return True