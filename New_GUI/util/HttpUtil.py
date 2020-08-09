def validateRequest(request, *args):
    u"""Used to validate that the specified fields have been set

    
    𝗥𝗲𝘁𝘂𝗿𝗻𝘀: A KeyError exception if one or more key names n args don't exist.
    𝗥𝗮𝗶𝘀𝗲𝘀: nothing
    :param request:    Flask.request object. Holds the data we wish to validate
    :param *args:  A list of strings that this function checks to see if they exist.
            If they don't all exist, a KeyError exception is raised.
    """
    for arg in args:
        if request.form[str(arg)] == None:
            raise KeyError("Key '{arg}' not found :(")

