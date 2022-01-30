import DataStruct


def validate(equation):

    for x in DataStruct.UNACCEPT:
        if chr(x) in equation:
            return False, x

    return True, 256
