# class and functions

def durchschnitt(list_in):
    print("brechne durchschnitt")
    summe = 0
    for i in list_in:
        summe = summe + i

    lenght = len(list_in)
    mean = summe // lenght
    return mean

durch = durchschnitt([1, 3, 5])
