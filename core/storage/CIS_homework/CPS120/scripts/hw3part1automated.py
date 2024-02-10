# this doesn't work, but with a little effort and debugging it could.
def part_one():
    #1) If W = 4, X = 14, Y = -7, and Z = 18, evaluate the following conditions.  Note that a condition evaluates to either True or False.
    W = 4
    X = 14
    Y = -7
    Z = 18
    input_values = """
    W == 4
    Y >= 33
    (W + X) != Z
    not (Y > (Y * W))
    (W == X) or (Y == Z)
    (Z < X) or not (Z < Y)
    (X <= Z) and (Y != Z)
    (W <= Y) and ((Y + Z) < X)
    """
    value_list = [item.strip() for item in input_values.split('\n') if item.strip() != '']
    print(value_list)
    for evaluation in value_list:
        try:
            result = eval(evaluation)
            print(f"{evaluation} is {result}")
        except SyntaxError as e:
            print(f"Error evaluating {evaluation}: {e}")

#part_one()



