def Add(No1, No2):
    return No1 + No2

def Sub(No1, No2):
    return No1 - No2

def Mul(No1, No2):
    return No1 * No2

def Div(No1, No2):
    if No2 == 0:
        return "DivisibleByZeroError"
    else:
        return No1 / No2