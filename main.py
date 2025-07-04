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
    :return: lista completa de todos los entrenos
    """
    trainComplete = []
    count = 1
    for day in plan:
        completeDay =("""
Rutina dia {}
Músculos a trabajar: {}
Calentamiento: {}
Ejercicios a realizar: {}
Estiramientos: {}
Duración estimada del entrenamiento: {}
Numero de ejercicios realizados: {}
        """.format(count, day["muscles"], day["exercise"][0], formatExercise(day["exercise"]), day["exercise"][1], day["time"], day["quantity"]))
        print(completeDay)
        sleep(1)
        count +=1
        trainComplete.append(completeDay)
    return trainComplete

def userOk():
    """
    Función para preguntarle al usuario si le gusta su rutina o quiere otra
    :return: Decisión tomada por el user
    """
    while True:
        decision = input("¿Te gusta esta rutina de ejercicio [S] o quieres que te genere otra [N]? (Si guardas esta se borrara otra que tengas guardada): ").upper().strip()
        if decision == "S" or decision == "N":
            return decision
        print("Por favor, introduce o S o N")

def writerExercise(trainComplete):
    """
    Función encargada de escribir en un documento txt la rutina
    :param trainComplete: Lista de entrenamiento
    """
    text = "\n\n".join(trainComplete) #Transformamos la lista en str
    with open("Rutina_Entreno.txt", "w", encoding="utf-8") as fichero: #abrimos un fichero de texto para escribir la rutina
        fichero.write(text) #Escribimos la rutina

def main():
    decision = ""
    while decision != "S":
        extractExercise()
        days, time= trainingSettings()
        quantity = quantityExercise(time)
        plan = setDay(days, quantity)
        trainComplete = basicInfo(plan)
        decision = userOk()
        if decision == "S":
            input("Tu rutina ha sido guardada en Rutina_Entreno.txt, pulse cualquier boton para salir")
            writerExercise(trainComplete)

if __name__ == "__main__":
    main()