import BCEConstants


def validate(equation):

    for x in BCEConstants.UNACCEPT:
        if chr(x) in equation:
            print(x)
            return False

    return True
