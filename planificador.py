import copy
import random
from math import trunc
from dataExercise import extractExercise


mapExercise = extractExercise()

trainingDay = {
    "exercise": [],
    "time": 0,
    "muscles": [],
    "quantity": 0,
}

def generateMusclesExercise(muscleGroup, muscleID, trainingDay):
    for _ in range(muscleGroup):
        exercise = random.choice(mapExercise[muscleID])
        while exercise in trainingDay["exercise"]:
            exercise = random.choice(mapExercise[muscleID])
        trainingDay["exercise"].append(exercise["name"])

def quantityExercise(days, time):
    quantity = trunc(time/5)
    return quantity

def days2(quantity, time):

    #Primer día: Pecho, Espalda, Biceps y Triceps
    trainingDay1 = trainingDay.copy()
    trainingDay1["muscles"] = ["Pecho", "Espalda", "Bíceps", "Tríceps"]
    trainingDay1["time"] = time
    trainingDay1["quantity"] = quantity
    trainingDay1["exercise"].append("Movilidad cuerpo")
    trainingDay1["exercise"].append("Rutina general de estiramientos")
    quantityDay1 = quantity-2 #30% Pecho, 30% Espalda, 20% Triceps, 20% Biceps
    chest = trunc(quantityDay1*0.3)
    back = trunc(quantityDay1*0.3)
    Triceps = trunc(quantityDay1*0.2)
    Biceps = trunc(quantityDay1*0.2)

    generateMusclesExercise(chest, "Pecho", trainingDay1)
    generateMusclesExercise(back, "Espalda", trainingDay1)
    generateMusclesExercise(Triceps, "Tríceps", trainingDay1)
    generateMusclesExercise(Biceps, "Bíceps", trainingDay1)


    #Segundo día: Pierna y hombro
    trainingDay2 = trainingDay.copy()
    trainingDay2["muscles"] = ["Pierna", "Hombro"]
    trainingDay2["time"] = time
    trainingDay2["quantity"] = quantity
    trainingDay2["exercise"].append("Movilidad pierna")
    trainingDay2["exercise"].append("Rutina general de estiramientos")
    quantityDay2 = quantity - 2 #70% Pierna y 30% hombro (Ya lo habremos trabajado de forma secundaria en pecho)
    leg = trunc(quantityDay2*0.7)
    shoulder = trunc(quantityDay2 * 0.3)

    generateMusclesExercise(leg, "Pierna", trainingDay2)
    generateMusclesExercise(shoulder, "Hombro", trainingDay2)

    return trainingDay


def days3(quantity, time):

    #Primer día: Pecho en gran medida, Hombro y Triceps para terminar de activarlo
    trainingDay1 = trainingDay.copy()
    trainingDay1["muscles"] = ["Pecho", "Tríceps"]
    trainingDay1["time"] = time
    trainingDay1["quantity"] = quantity
    trainingDay1["exercise"].append("Movilidad cuerpo")
    trainingDay1["exercise"].append("Rutina general de estiramientos")
    quantityDay1 = quantity - 2 #Pecho 65%, Hombros 20% y Tríceps 15%
    chest = trunc(quantityDay1*0.65)
    shoulder = trunc(quantityDay1*0.2)
    Triceps = trunc(quantityDay1*0.15)

    generateMusclesExercise(chest, "Pecho", trainingDay1)
    generateMusclesExercise(shoulder, "Hombro", trainingDay1)
    generateMusclesExercise(Triceps, "Tríceps", trainingDay1)

    #Segundo día: Espalda y biceps para terminar de activarlo
    trainingDay2 = trainingDay.copy()
    trainingDay2["muscles"] = ["Espalda", "Tríceps"]
    trainingDay2["time"] = time
    trainingDay2["quantity"] = quantity
    trainingDay2["exercise"].append("Movilidad cuerpo")
    trainingDay2["exercise"].append("Rutina general de estiramientos")
    quantityDay2 = quantity - 2  # 70% Espalda y 30% Biceps
    back = trunc(quantityDay2 * 0.7)
    Biceps = trunc(quantityDay2 * 0.3)

    generateMusclesExercise(back, "Espalda", trainingDay2)
    generateMusclesExercise(Biceps, "Bíceps", trainingDay2)

    #Tercer día: Pierna completa
    trainingDay3 = trainingDay.copy()
    trainingDay3["muscles"] = ["Pierna"]
    trainingDay3["time"] = time
    trainingDay3["quantity"] = quantity
    trainingDay3["exercise"].append("Movilidad pierna")
    trainingDay3["exercise"].append("Rutina general de estiramientos")
    quantityDay3 = quantity - 2  # 100% Pierna
    leg = trunc(quantityDay3)

    generateMusclesExercise(leg, "Pierna", trainingDay3)

def days4(quantity, time):
    #Primer día: Torso completo 1/2
    trainingDay1 = trainingDay.copy()
    trainingDay1["muscles"] = ["Pecho", "Espalda", "Bíceps", "Tríceps"]
    trainingDay1["time"] = time
    trainingDay1["quantity"] = quantity
    trainingDay1["exercise"].append("Movilidad cuerpo")
    trainingDay1["exercise"].append("Rutina general de estiramientos")
    quantityDay1 = quantity - 2  # 30% Pecho, 30% Espalda, 20% Triceps, 20% Biceps
    chest = trunc(quantityDay1 * 0.3)
    back = trunc(quantityDay1 * 0.3)
    Triceps = trunc(quantityDay1 * 0.2)
    Biceps = trunc(quantityDay1 * 0.2)

    generateMusclesExercise(chest, "Pecho", trainingDay1)
    generateMusclesExercise(back, "Espalda", trainingDay1)
    generateMusclesExercise(Triceps, "Tríceps", trainingDay1)
    generateMusclesExercise(Biceps, "Bíceps", trainingDay1)

    # Segundo día: Pierna completa 1/2
    trainingDay2 = trainingDay.copy()
    trainingDay2["muscles"] = ["Pierna"]
    trainingDay2["time"] = time
    trainingDay2["quantity"] = quantity
    trainingDay2["exercise"].append("Movilidad pierna")
    trainingDay2["exercise"].append("Rutina general de estiramientos")
    quantityDay2 = quantity - 2  # 100% Pierna
    leg = trunc(quantityDay2)

    generateMusclesExercise(leg, "Pierna", trainingDay2)

    # Tercer día: Torso completo 2/2
    trainingDay3 = trainingDay.copy()
    trainingDay3["muscles"] = ["Pecho", "Espalda", "Bíceps", "Tríceps"]
    trainingDay3["time"] = time
    trainingDay3["quantity"] = quantity
    trainingDay3["exercise"].append("Movilidad cuerpo")
    trainingDay3["exercise"].append("Rutina general de estiramientos")
    quantityDay3 = quantity - 2  # 30% Pecho, 30% Espalda, 20% Triceps, 20% Biceps
    chest = trunc(quantityDay3 * 0.3)
    back = trunc(quantityDay3 * 0.3)
    Triceps = trunc(quantityDay3 * 0.2)
    Biceps = trunc(quantityDay3 * 0.2)

    generateMusclesExercise(chest, "Pecho", trainingDay3)
    generateMusclesExercise(back, "Espalda", trainingDay3)
    generateMusclesExercise(Triceps, "Tríceps", trainingDay3)
    generateMusclesExercise(Biceps, "Bíceps", trainingDay3)

    # Cuarto día: Pierna completa 2/2
    trainingDay4 = trainingDay.copy()
    trainingDay4["muscles"] = ["Pierna"]
    trainingDay4["time"] = time
    trainingDay4["quantity"] = quantity
    trainingDay4["exercise"].append("Movilidad pierna")
    trainingDay4["exercise"].append("Rutina general de estiramientos")
    quantityDay4 = quantity - 2  # 100% Pierna
    leg = trunc(quantityDay4)

    generateMusclesExercise(leg, "Pierna", trainingDay4)

def days5(quantity, time):
    # Primer día: Pecho en gran medida, Hombro y Triceps para terminar de activarlo
    trainingDay1 = trainingDay.copy()
    trainingDay1["muscles"] = ["Pecho", "Tríceps"]
    trainingDay1["time"] = time
    trainingDay1["quantity"] = quantity
    trainingDay1["exercise"].append("Movilidad cuerpo")
    trainingDay1["exercise"].append("Rutina general de estiramientos")
    quantityDay1 = quantity - 2
    chest = trunc(quantityDay1 * 0.65)
    shoulder = trunc(quantityDay1 * 0.2, 0)
    Triceps = trunc(quantityDay1 * 0.15, 0)

    generateMusclesExercise(chest, "Pecho", trainingDay1)
    generateMusclesExercise(shoulder, "Hombro", trainingDay1)
    generateMusclesExercise(Triceps, "Tríceps", trainingDay1)

    # Segundo día: Espalda y biceps para terminar de activarlo
    trainingDay2 = trainingDay.copy()
    trainingDay2["muscles"] = ["Espalda", "Bíceps"]
    trainingDay2["time"] = time
    trainingDay2["quantity"] = quantity
    trainingDay2["exercise"].append("Movilidad cuerpo")
    trainingDay2["exercise"].append("Rutina general de estiramientos")
    quantityDay2 = quantity - 2  # 70% Espalda y 30% Biceps (Ya lo habremos trabajado de forma secundaria en Espalda)
    back = trunc(quantityDay2 * 0.7, 0)
    Biceps = trunc(quantityDay2 * 0.3, 0)

    generateMusclesExercise(back, "Espalda", trainingDay2)
    generateMusclesExercise(Biceps, "Bíceps", trainingDay2)

    # Tercer día: Pierna completa
    trainingDay3 = trainingDay.copy()
    trainingDay3["muscles"] = ["Pierna"]
    trainingDay3["time"] = time
    trainingDay3["quantity"] = quantity
    trainingDay3["exercise"].append("Movilidad pierna")
    trainingDay3["exercise"].append("Rutina general de estiramientos")
    quantityDay3 = quantity - 2  # 100% Pierna
    leg = trunc(quantityDay3, 0)

    generateMusclesExercise(leg, "Pierna", trainingDay3)

    # Cuarto día: Torso completo
    trainingDay4 = trainingDay.copy()
    trainingDay4["muscles"] = ["Pecho", "Espalda", "Bíceps", "Tríceps"]
    trainingDay4["time"] = time
    trainingDay4["quantity"] = quantity
    trainingDay4["exercise"].append("Movilidad cuerpo")
    trainingDay4["exercise"].append("Rutina general de estiramientos")
    quantityDay4 = quantity - 2  # 30% Pecho, 30% Espalda, 20% Triceps, 20% Biceps
    chest = trunc(quantityDay4 * 0.3, 0)
    back = trunc(quantityDay4 * 0.3, 0)
    Triceps = trunc(quantityDay4 * 0.2, 0)
    Biceps = trunc(quantityDay4 * 0.2, 0)

    generateMusclesExercise(chest, "Pecho", trainingDay4)
    generateMusclesExercise(back, "Espalda", trainingDay4)
    generateMusclesExercise(Triceps, "Tríceps", trainingDay4)
    generateMusclesExercise(Biceps, "Bíceps", trainingDay4)

    # Quinto día: Pierna completa
    trainingDay5 = trainingDay.copy()
    trainingDay5["muscles"] = ["Pierna"]
    trainingDay5["time"] = time
    trainingDay5["quantity"] = quantity
    trainingDay5["exercise"].append("Movilidad pierna")
    trainingDay5["exercise"].append("Rutina general de estiramientos")
    quantityDay5 = quantity - 2  # 100% Pierna
    leg = trunc(quantityDay5, 0)

    generateMusclesExercise(leg, "Pierna", trainingDay5)

def setDay(days, quantity, time):
    if days == 2:
        return days2(quantity, time)
    elif days == 3:
        return days3(quantity, time)
    elif days == 4:
        return days4(quantity, time)
    elif days == 5:
        return days5(quantity, time)