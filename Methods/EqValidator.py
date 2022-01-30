import BCEConstants


def validate(equation):

    for x in BCEConstants.UNACCEPT:
        if chr(x) in equation:
            return False, x

    return True, 256
