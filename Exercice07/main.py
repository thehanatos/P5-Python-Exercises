# Écrivez votre code ici !
def square(nb):
    """
    Calculate the square of a given number.

    Args:
        nb (int or float): number

    Returns:
        int or float: returns the square of the number
    """
    if isinstance(nb, str) is True:
        print("Le paramètre doit être un nombre !")
        return None
    else:
        result = nb * nb
        return print(result)


# Examples of use :
square(3)

square(3.3)

square('ab')
