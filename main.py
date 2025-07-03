from time import sleep
from dataExercise import extractExercise
from planificador import quantityExercise, setDay


def trainingSettings():
    """
    Función encargada de preguntar al user los días de entreno y el tiempo de cada entreno
    :return: Te devuelve los días totales de entrenamiento y el tiempo de los entrenamientos
    """
    days = 0
    time = 0
    while 2 > days or 5 < days:
        days = int(input("¿Cuantos dias vas a querer entrenar a la semana? (De 2 a 5): "))
    while 50 > time or 100 < time:
        time = int(input("¿Cuanto tiempo tienes para entrenar? (De 50 a 100 mins): "))
    return days, time

def formatExercise(listExercise):
    """
    Función encargada de guardar de forma estética los ejercicios a realizar
    :param listExercise: Lista de ejercicios que va a realizar ese día
    :return: Ejercicios a realizar en un día con formato limpio
    """
    count = 1
    textFormat = ""
    for exercise in listExercise:
        if count > 2:
            textFormat += "\n\t→ {}".format(exercise)
        count +=1
    return textFormat


def basicInfo(plan):
    """
    Función que printea al usuario el día de ejercicio y información relevante
    :param plan: Lista completa con todos los ejercicios en bruto
    """
    count = 1
    for day in plan:
        print("""
Rutina dia {}
Músculos a trabajar: {}
Calentamiento: {}
Ejercicios a realizar: {}
Estiramientos: {}
Duración estimada del entrenamiento: {}
Numero de ejercicios realizados: {}
        """.format(count, day["muscles"], day["exercise"][0], formatExercise(day["exercise"]), day["exercise"][1], day["time"], day["quantity"]))
        sleep(1)
        count +=1

def main():
    test= extractExercise()
    days, time= trainingSettings()
    quantity = quantityExercise(time)
    plan = setDay(days, quantity, time)
    basicInfo(plan)

if __name__ == "__main__":
    main()