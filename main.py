from dataExercise import extractExercise
from planificador import quantityExercise


def trainingSettings():
    days = 0
    time = 0
    while 2 > days or 5 < days:
        days = int(input("¿Cuantos dias vas a querer entrenar a la semana? (De 2 a 5): "))
    while 50 > time or 100 < time:
        time = int(input("¿Cuanto van a durar tus entrenos? (De 50 a 100 mins): "))
    return days, time

def setTraining():


def main():
    test= extractExercise()
    days, time= trainingSettings()
    quantityExercise(days, time)

if __name__ == "__main__":
    main()