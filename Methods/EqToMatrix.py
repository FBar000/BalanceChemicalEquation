import BCEClasses
import BCEConstants



#Return a list of lists with the coefficients of each unknown, given the equation as a string
# IN: String / OUT: 2d list
def equationToMatrix(equation):

    # matrix to be returned
    result = []


    # Hold each term of the equation. RHS specified with *
    term_array = findDistinctTerms(equation)

    # Keep track of all elements
    element_array = findDistinctElements(equation)

    # Loop over element
    for element in element_array:
        row = []

        # Loop over term
        for term in term_array:

            # Keep track of instances of element in term
            instance_array = findDistinctInstances(element, term)

            # Initialize entry
            coefficient = 0

            # Loop over insances
            for instance in instance_array:
                 coefficient += count(instance, term)


            # Account for the role in the reaction
            if term[0] == "*":
                coefficient *= -1

            row.append(coefficient)
        result.append(row)


    # Keep track of terms' identities
    result.append(term_array)


    return result


# TODO
# IN: dict / OUT: String
def wrapSolution(solution):

    bal_eq = ""

    toggle = 0


    # Get term identities
    keys = list(solution)

    sol = 0
    for k in keys:
        if k[0] != "*":
            if solution[k] != 0:
                sol += 1
                
    if sol == 0:
        return "All zeros"

    for k in keys:

        # Control for side of the equation
        if k[0] == "*":
            toggle += 1
        if toggle == 1:
            bal_eq = bal_eq[:-2] + ": "

        t = k
        if toggle > 0:
            t = k[1:]

        # Add non one coefficients
        coef = ""
        if solution[k] > 1:
            coef = str(solution[k]) + " "

        # Check if coefficient is zero
        if solution[k] == 0:
            coef = "0 "


        bal_eq += coef + t + " + "

    bal_eq = bal_eq[:-3]

    return bal_eq


# Functional
# Record distinct atoms in the equation
# IN: String / OUT: 1d string list
def findDistinctElements(equation):

    # To return
    atoms = []

    # Loop over characters
    for i in range(len(equation)):

        # Process Character
        s = equation[i]
        s_ascii = ord(s)

        # Check if character is upper cased
        if 64 < s_ascii and s_ascii < 91:

            if i < len(equation) - 1:
                nxt_ascii = ord(equation[i+1])
                # Check if the following is lowercase               (Potential bug: what if it is a coefficient in that range?)
                # Update the current element if so
                if 96 < nxt_ascii and nxt_ascii < 123:
                    s += equation[i + 1]

            # Count atom if new
            if not s in atoms:
                atoms.append(s)

    return atoms


# Functional
# Record distinct terms in the equation, specify RHS with *
# IN: String / OUT: 1d string list
def findDistinctTerms(equation):

    # To return
    terms = []

    index = 0
    prodSide = False
    tmp = ""
    # Loop over characters
    while index < len(equation):

        tmp += equation[index]

        # The equality signals a new term
        if equation[index] == ":":
            terms.append(tmp[:-1].strip())
            tmp = ""
            prodSide = True

        # Each + signals a new term
        if equation[index] == "+":
            tmp = tmp[:-1].strip()

            if prodSide:
                tmp = "*" + tmp

            terms.append(tmp)
            tmp = ""

        index += 1

    # Includes the last term
    terms.append("*" + tmp.strip())

    return terms


# Return an array with all the instances of an element in a term
# In: element (string) / Out: list of pointers to units of that element
def findDistinctInstances(element, term):

    # To return
    result = []

    lo = -1
    # Loop until no more instances of element can be found in term
    while True:
        lo = term.find(element, lo+1)

        # Exit switch
        if lo == -1:
            break

        hi = lo + len(element) - 1

        tmp = BCEClasses.Unit(lo, hi)
        result.append(tmp)

    return result


# Functional
# Return the count of instances of a thing (unit) in a given term (string)
# Positive count for reactants, Negative for products
# IN: Unit / OUT: int
def count(thing, term):

    ct = 0;

    if (thing.hi+1 >= len(term)) or (not term[thing.hi+1].isnumeric()):
        ct += 1
    else:
        ct += int(term[thing.hi+1])

    gp = group(thing, term)

    if gp != BCEConstants.NULL_UNIT:
        ct *= count(gp, term)

    return ct


# Functional
# Return the unit a given unit is in. NULL_UNIT if there is no super unit
# IN: Unit / Out: Unit
def group(thing, term):

    # Split the term into the parts to be analyzed
    left = term[:thing.lo]
    right = term[thing.hi:]

    # Initialize the default values of the output unit
    new_lo = -1
    new_hi = -1


    # Look for bracket on left
    count = 0
    fromRight = 1
    while fromRight < len(left):

        if left[-fromRight] == "(":
            count += -1
        elif left[-fromRight] == ")":
            count += 1

        if count < 0:
            new_lo = len(left) - fromRight
            break

        fromRight += 1

    # Look for bracket on right
    count = 0
    fromLeft = 1
    while fromLeft < len(right):

        if right[fromLeft] == ")":
            count += -1
        elif right[fromLeft] == "(":
            count += 1

        if count < 0:
            new_hi = len(left) + fromLeft + thing.size()
            break


        fromLeft += 1

    # Package results in new (unit) object
    if (new_lo == -1 or new_hi == -1):
        return BCEConstants.NULL_UNIT

    return BCEClasses.Unit(new_lo, new_hi)