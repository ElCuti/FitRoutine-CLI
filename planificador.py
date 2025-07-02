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
    quantity = trunc(time/5, 0)
    return quantity

def days2(quantity, time):

    #Primer dia
    trainingDay1 = trainingDay.copy()
    trainingDay1["muscles"] = ["Pecho", "Espalda", "Bíceps", "Tríceps"]
    trainingDay1["time"] = time
    trainingDay1["quantity"] = quantity
    trainingDay1["exercise"].append("Movilidad cuerpo")
    trainingDay1["exercise"].append("Rutina general de estiramientos")
    quantityDay1 = quantity-2 #30% Pecho, 30% Espalda, 20% Triceps, 20% Biceps
    chest = trunc(quantityDay1*0.3, 0)
    back = trunc(quantityDay1*0.3, 0)
    Triceps = trunc(quantityDay1*0.2, 0)
    Biceps = trunc(quantityDay1*0.2, 0)

    generateMusclesExercise(chest, "Pecho", trainingDay1)
    generateMusclesExercise(back, "Espalda", trainingDay1)
    generateMusclesExercise(Triceps, "Tríceps", trainingDay1)
    generateMusclesExercise(Biceps, "Bíceps", trainingDay1)


    #Segundo dia
    trainingDay2 = trainingDay.copy()
    trainingDay2["muscles"] = ["Pierna", "Hombro"]
    trainingDay2["time"] = time
    trainingDay2["quantity"] = quantity
    trainingDay2["exercise"].append("Movilidad pierna")
    trainingDay2["exercise"].append("Rutina general de estiramientos")
    quantityDay2 = quantity - 2
    leg = trunc(quantityDay2*0.7, 0)
    shoulder = trunc(quantityDay2 * 0.3, 0)

    generateMusclesExercise(leg, "Pierna", trainingDay2)
    generateMusclesExercise(shoulder, "Hombro", trainingDay2)