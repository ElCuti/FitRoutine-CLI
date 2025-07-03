import copy
import random
from math import trunc
from dataExercise import extractExercise


mapExercise = extractExercise()

trainingDayScheme = {
    "exercise": [],
    "time": 0,
    "muscles": [],
    "quantity": 0,
}

def generateMusclesExercise(muscleGroup, muscleID, trainingDay):
    """
    Función encargada de crear los ejercicios del día de forma aleatoria, siempre evitando la repetición
    :param muscleGroup: Cantidad de ejercicios de un músculo en concreto
    :param muscleID: Nombre del músculo en concreto
    :param trainingDay: Lista donde almacenamos el bruto del entrenamiento
    """
    for _ in range(muscleGroup):
        exercise = random.choice(mapExercise[muscleID])
        nameExercise = exercise["name"]+ " " +exercise["repetitions"]
        while nameExercise in trainingDay["exercise"]:
            exercise = random.choice(mapExercise[muscleID])
            nameExercise = exercise["name"] + " " + exercise["repetitions"]
        trainingDay["exercise"].append(nameExercise)

def quantityExercise(time):
    """
    Función para calcular los ejercicios totales del día
    :param time: Tiempo de entrenamiento
    :return: Cantidad de ejercicios totales
    """
    quantity = trunc(time/5)
    return quantity

def days2(quantity):
    """
    Función para crear la rutina de X días, escogidos por el usuario
    :param quantity:
    :param time:
    :return:
    """
    #Primer día: Pecho, Espalda, Biceps y Triceps
    trainingDay1 = copy.deepcopy(trainingDayScheme) 
    trainingDay1["muscles"] = ["Pecho", "Espalda", "Bíceps", "Tríceps"]
    trainingDay1["exercise"].append("Movilidad cuerpo")
    trainingDay1["exercise"].append("Rutina general de estiramientos")
    quantityDay1 = quantity-2 #30% Pecho, 30% Espalda, 20% Triceps, 20% Biceps
    chest = trunc(quantityDay1*0.3)
    back = trunc(quantityDay1*0.3)
    Triceps = trunc(quantityDay1*0.2)
    Biceps = trunc(quantityDay1*0.2)
    trainingDay1["quantity"] = chest + back + Triceps + Biceps
    trainingDay1["time"] = trainingDay1["quantity"]*5+10

    generateMusclesExercise(chest, "Pecho", trainingDay1)
    generateMusclesExercise(back, "Espalda", trainingDay1)
    generateMusclesExercise(Triceps, "Tríceps", trainingDay1)
    generateMusclesExercise(Biceps, "Bíceps", trainingDay1)


    #Segundo día: Pierna y hombro
    trainingDay2 = copy.deepcopy(trainingDayScheme) 
    trainingDay2["muscles"] = ["Pierna", "Hombro"]


    trainingDay2["exercise"].append("Movilidad pierna")
    trainingDay2["exercise"].append("Rutina general de estiramientos")
    quantityDay2 = quantity - 2 #70% Pierna y 30% hombro (Ya lo habremos trabajado de forma secundaria en pecho)
    leg = trunc(quantityDay2*0.7)
    shoulder = trunc(quantityDay2 * 0.3)
    trainingDay2["quantity"] = leg + shoulder
    trainingDay2["time"] = trainingDay2["quantity"]*5+10

    generateMusclesExercise(leg, "Pierna", trainingDay2)
    generateMusclesExercise(shoulder, "Hombro", trainingDay2)

    return [trainingDay1, trainingDay2]


def days3(quantity):

    #Primer día: Pecho en gran medida, Hombro y Triceps para terminar de activarlo
    trainingDay1 = copy.deepcopy(trainingDayScheme) 
    trainingDay1["muscles"] = ["Pecho", "Tríceps"]
    trainingDay1["exercise"].append("Movilidad cuerpo")
    trainingDay1["exercise"].append("Rutina general de estiramientos")
    quantityDay1 = quantity - 2 #Pecho 65%, Hombros 20% y Tríceps 15%
    chest = trunc(quantityDay1*0.65)
    shoulder = trunc(quantityDay1*0.2)
    Triceps = trunc(quantityDay1*0.15)
    trainingDay1["quantity"] = chest + shoulder + Triceps
    trainingDay1["time"] = trainingDay1["quantity"]*5+10

    generateMusclesExercise(chest, "Pecho", trainingDay1)
    generateMusclesExercise(shoulder, "Hombro", trainingDay1)
    generateMusclesExercise(Triceps, "Tríceps", trainingDay1)

    #Segundo día: Espalda y biceps para terminar de activarlo
    trainingDay2 = copy.deepcopy(trainingDayScheme) 
    trainingDay2["muscles"] = ["Espalda", "Tríceps"]


    trainingDay2["exercise"].append("Movilidad cuerpo")
    trainingDay2["exercise"].append("Rutina general de estiramientos")
    quantityDay2 = quantity - 2  # 70% Espalda y 30% Biceps
    back = trunc(quantityDay2 * 0.7)
    Biceps = trunc(quantityDay2 * 0.3)
    trainingDay2["quantity"] = back + Biceps
    trainingDay2["time"] = trainingDay2["quantity"]*5+10

    generateMusclesExercise(back, "Espalda", trainingDay2)
    generateMusclesExercise(Biceps, "Bíceps", trainingDay2)

    #Tercer día: Pierna completa
    trainingDay3 = copy.deepcopy(trainingDayScheme) 
    trainingDay3["muscles"] = ["Pierna"]
    trainingDay3["exercise"].append("Movilidad pierna")
    trainingDay3["exercise"].append("Rutina general de estiramientos")
    quantityDay3 = quantity - 2  # 100% Pierna
    leg = trunc(quantityDay3)
    trainingDay3["quantity"] = leg
    trainingDay3["time"] = trainingDay3["quantity"]*5+10

    generateMusclesExercise(leg, "Pierna", trainingDay3)

    return [trainingDay1, trainingDay2, trainingDay3]

def days4(quantity):
    #Primer día: Torso completo 1/2
    trainingDay1 = copy.deepcopy(trainingDayScheme) 
    trainingDay1["muscles"] = ["Pecho", "Espalda", "Bíceps", "Tríceps"]
    trainingDay1["exercise"].append("Movilidad cuerpo")
    trainingDay1["exercise"].append("Rutina general de estiramientos")
    quantityDay1 = quantity - 2  # 30% Pecho, 30% Espalda, 20% Triceps, 20% Biceps
    chest = trunc(quantityDay1 * 0.3)
    back = trunc(quantityDay1 * 0.3)
    Triceps = trunc(quantityDay1 * 0.2)
    Biceps = trunc(quantityDay1 * 0.2)
    trainingDay1["quantity"] = chest + back + Triceps + Biceps
    trainingDay1["time"] = trainingDay1["quantity"] * 5 + 10

    generateMusclesExercise(chest, "Pecho", trainingDay1)
    generateMusclesExercise(back, "Espalda", trainingDay1)
    generateMusclesExercise(Triceps, "Tríceps", trainingDay1)
    generateMusclesExercise(Biceps, "Bíceps", trainingDay1)

    # Segundo día: Pierna completa 1/2
    trainingDay2 = copy.deepcopy(trainingDayScheme) 
    trainingDay2["muscles"] = ["Pierna"]
    trainingDay2["exercise"].append("Movilidad pierna")
    trainingDay2["exercise"].append("Rutina general de estiramientos")
    quantityDay2 = quantity - 2  # 100% Pierna
    leg = trunc(quantityDay2)
    trainingDay2["quantity"] = leg
    trainingDay2["time"] = trainingDay2["quantity"] * 5 + 10

    generateMusclesExercise(leg, "Pierna", trainingDay2)

    # Tercer día: Torso completo 2/2
    trainingDay3 = copy.deepcopy(trainingDayScheme) 
    trainingDay3["muscles"] = ["Pecho", "Espalda", "Bíceps", "Tríceps"]
    trainingDay3["exercise"].append("Movilidad cuerpo")
    trainingDay3["exercise"].append("Rutina general de estiramientos")
    quantityDay3 = quantity - 2  # 30% Pecho, 30% Espalda, 20% Triceps, 20% Biceps
    chest = trunc(quantityDay3 * 0.3)
    back = trunc(quantityDay3 * 0.3)
    Triceps = trunc(quantityDay3 * 0.2)
    Biceps = trunc(quantityDay3 * 0.2)
    trainingDay3["quantity"] = chest + back + Triceps + Biceps
    trainingDay3["time"] = trainingDay3["quantity"] * 5 + 10

    generateMusclesExercise(chest, "Pecho", trainingDay3)
    generateMusclesExercise(back, "Espalda", trainingDay3)
    generateMusclesExercise(Triceps, "Tríceps", trainingDay3)
    generateMusclesExercise(Biceps, "Bíceps", trainingDay3)

    # Cuarto día: Pierna completa 2/2
    trainingDay4 = copy.deepcopy(trainingDayScheme) 
    trainingDay4["muscles"] = ["Pierna"]
    trainingDay4["exercise"].append("Movilidad pierna")
    trainingDay4["exercise"].append("Rutina general de estiramientos")
    quantityDay4 = quantity - 2  # 100% Pierna
    leg = trunc(quantityDay4)
    trainingDay4["quantity"] = leg
    trainingDay4["time"] = trainingDay4["quantity"] * 5 + 10

    generateMusclesExercise(leg, "Pierna", trainingDay4)

    return [trainingDay1, trainingDay2, trainingDay3, trainingDay4]

def days5(quantity):
    # Primer día: Pecho en gran medida, Hombro y Triceps para terminar de activarlo
    trainingDay1 = copy.deepcopy(trainingDayScheme) 
    trainingDay1["muscles"] = ["Pecho", "Tríceps"]
    trainingDay1["exercise"].append("Movilidad cuerpo")
    trainingDay1["exercise"].append("Rutina general de estiramientos")
    quantityDay1 = quantity - 2
    chest = trunc(quantityDay1 * 0.65)
    shoulder = trunc(quantityDay1 * 0.2)
    Triceps = trunc(quantityDay1 * 0.15)
    trainingDay1["quantity"] = chest + shoulder + Triceps
    trainingDay1["time"] = trainingDay1["quantity"]*5+10

    generateMusclesExercise(chest, "Pecho", trainingDay1)
    generateMusclesExercise(shoulder, "Hombro", trainingDay1)
    generateMusclesExercise(Triceps, "Tríceps", trainingDay1)

    # Segundo día: Espalda y biceps para terminar de activarlo
    trainingDay2 = copy.deepcopy(trainingDayScheme) 
    trainingDay2["muscles"] = ["Espalda", "Bíceps"]
    trainingDay2["exercise"].append("Movilidad cuerpo")
    trainingDay2["exercise"].append("Rutina general de estiramientos")
    quantityDay2 = quantity - 2  # 70% Espalda y 30% Biceps (Ya lo habremos trabajado de forma secundaria en Espalda)
    back = trunc(quantityDay2 * 0.7)
    Biceps = trunc(quantityDay2 * 0.3)
    trainingDay2["quantity"] = back + Biceps
    trainingDay2["time"] = trainingDay2["quantity"]*5+10

    generateMusclesExercise(back, "Espalda", trainingDay2)
    generateMusclesExercise(Biceps, "Bíceps", trainingDay2)

    # Tercer día: Pierna completa
    trainingDay3 = copy.deepcopy(trainingDayScheme) 
    trainingDay3["muscles"] = ["Pierna"]
    trainingDay3["exercise"].append("Movilidad pierna")
    trainingDay3["exercise"].append("Rutina general de estiramientos")
    quantityDay3 = quantity - 2  # 100% Pierna
    leg = trunc(quantityDay3)
    trainingDay3["quantity"] = leg
    trainingDay3["time"] = trainingDay3["quantity"] * 5 + 10

    generateMusclesExercise(leg, "Pierna", trainingDay3)

    # Cuarto día: Torso completo
    trainingDay4 = copy.deepcopy(trainingDayScheme) 
    trainingDay4["muscles"] = ["Pecho", "Espalda", "Bíceps", "Tríceps"]
    trainingDay4["exercise"].append("Movilidad cuerpo")
    trainingDay4["exercise"].append("Rutina general de estiramientos")
    quantityDay4 = quantity - 2  # 30% Pecho, 30% Espalda, 20% Triceps, 20% Biceps
    chest = trunc(quantityDay4 * 0.3)
    back = trunc(quantityDay4 * 0.3)
    Triceps = trunc(quantityDay4 * 0.2)
    Biceps = trunc(quantityDay4 * 0.2)
    trainingDay4["quantity"] = chest + back + Triceps + Biceps
    trainingDay4["time"] = trainingDay4["quantity"] * 5 + 10

    generateMusclesExercise(chest, "Pecho", trainingDay4)
    generateMusclesExercise(back, "Espalda", trainingDay4)
    generateMusclesExercise(Triceps, "Tríceps", trainingDay4)
    generateMusclesExercise(Biceps, "Bíceps", trainingDay4)

    # Quinto día: Pierna completa
    trainingDay5 = copy.deepcopy(trainingDayScheme) 
    trainingDay5["muscles"] = ["Pierna"]
    trainingDay5["exercise"].append("Movilidad pierna")
    trainingDay5["exercise"].append("Rutina general de estiramientos")
    quantityDay5 = quantity - 2  # 100% Pierna
    leg = trunc(quantityDay5)
    trainingDay5["quantity"] = leg
    trainingDay5["time"] = trainingDay5["quantity"] * 5 + 10

    generateMusclesExercise(leg, "Pierna", trainingDay5)

    return [trainingDay1, trainingDay2, trainingDay3, trainingDay4, trainingDay5]

def setDay(days, quantity, time):
    if days == 2:
        return days2(quantity)
    elif days == 3:
        return days3(quantity)
    elif days == 4:
        return days4(quantity)
    elif days == 5:
        return days5(quantity)

