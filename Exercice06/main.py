# Fonction calculate_average
def calculate_average(list):
    sum = 0
    for number in list:
        sum = sum + number
    return sum / len(list)


# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("La moyenne est :", average)
