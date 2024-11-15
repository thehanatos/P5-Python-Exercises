students = {
    'Alice': {
        'Mathematiques': 90,
        'Francais': 80,
        'Histoire': 95
    },
    'Bob': {
        'Mathematiques': 75,
        'Francais': 85,
        'Histoire': 70
    },
    'Charlie': {
        'Mathematiques': 88,
        'Francais': 92,
        'Histoire': 78
    }
}
student_name = input("Entrez le nom de l’étudiant :  ")

try:
    print("Notes de", student_name,
          ": Mathematiques : {}, Francais : {}, Histoire : {}".format(
              students[student_name]['Mathematiques'],
              students[student_name]['Francais'],
              students[student_name]['Histoire']))
    average_note = (int(students[student_name]['Mathematiques']) +
                    int(students[student_name]['Francais']) +
                    int(students[student_name]['Histoire'])) / 3
    print(f"Moyenne de {student_name} : {average_note}")
except KeyError:
    print(f"L'étudiant {student_name} n'existe pas dans la liste.")
