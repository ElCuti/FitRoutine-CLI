dataExercise = {
    "name": "",
    "repetitions": "",
    "muscle": ""
}

mapExercise = {
    "Pecho": [],
    "Pierna": [],
    "Espalda": [],
    "Bíceps": [],
    "Tríceps": [],
    "Hombro": []
}


listExercise = [
# Pecho
    "Press banca, 4x12, Pecho",
    "Press inclinado con mancuernas, 3x12, Pecho",
    "Press martillo en banco inclinado con mancuernas, 3x12, Pecho",
    "Aperturas en banco inclinado, 3x10, Pecho",
    "Press de banca declinado alternado con mancuernas, 3x12, Pecho",
    "Flexiones, 4x10, Pecho",
    "Máquina Peck Deck, 3x12, Pecho",
    "Dips en paralelas (pecho), 3x8, Pecho",
    "Press con barra agarre estrecho, 3x10, Pecho",
    "Aperturas en máquina, 3x12, Pecho",

    # Pierna
    "Sentadilla, 4x10, Pierna",
    "Sentadilla sumo con pesa rusa, 4x10, Pierna",
    "Sentadilla split con mancuernas, 4x10, Pierna",
    "Sentadilla split con barra, 4x10, Pierna",
    "Sentadillas con salto, 4x12, Pierna",
    "Sentadilla búlgara, 3x10, Pierna",
    "Prensa de piernas, 4x12, Pierna",
    "Peso muerto rumano, 4x10, Pierna",
    "Curl femoral tumbado, 4x12, Pierna",
    "Extensión de cuádriceps en máquina, 4x12, Pierna",

    # Espalda
    "Remo supino con mancuernas, 4x10, Espalda",
    "Remo sentado con banda elástica, 4x10, Espalda",
    "Remo inclinado en banco con mancuernas (agarre prono), 4x10, Espalda",
    "Remo con banda elástica (de pie), 4x10, Espalda",
    "Remo al cuello con banda elástica, 4x10, Espalda",
    "Peso muerto con barra, 4x10, Espalda",
    "Jalón al pecho en polea alta, 4x12, Espalda",
    "Dominadas pronas, 4x8, Espalda",
    "Pullover con mancuerna, 3x12, Espalda",
    "Jalón con agarre estrecho en polea, 4x12, Espalda",

    # Bíceps
    "Curl con barra, 4x10, Bíceps",
    "Curl alternado con banda elástica, 3x10, Bíceps",
    "Curl agarre prono con mancuernas, 3x10, Bíceps",
    "Curl invertido con barra, 4x10, Bíceps",
    "Curl martillo con mancuernas, 3x10, Bíceps",
    "Curl en predicador con barra, 3x10, Bíceps",
    "Curl concentrado, 3x12, Bíceps",
    "Curl en banco inclinado, 3x12, Bíceps",
    "Curl 21s con barra, 3 series, Bíceps",
    "Curl con cable en polea baja, 4x12, Bíceps",

    # Tríceps
    "Press de copa con mancuerna de pie, 4x10, Tríceps",
    "Patada de tríceps con banda elástica, 3x10, Tríceps",
    "Flexiones sobre los antebrazos, 4x10, Tríceps",
    "Extensión de tríceps acostado con mancuerna, 3x10, Tríceps",
    "Extensión mancuerna tras nuca con una mano (de pie), 3x10, Tríceps",
    "Fondos entre bancos, 3x12, Tríceps",
    "Extensión en polea alta con cuerda, 4x12, Tríceps",
    "Press cerrado en máquina Smith, 3x10, Tríceps",
    "Patada de tríceps con mancuerna, 3x12, Tríceps",
    "Extensión con barra V en polea, 4x10, Tríceps",

    # Hombro
    "Press militar con barra (agarre abierto), 4x10, Hombro",
    "Press de hombros sentado con mancuernas (agarre neutro), 4x10, Hombro",
    "Press Arnold con mancuernas, 4x10, Hombro",
    "Elevaciones frontales con barra, 4x10, Hombro",
    "Elevaciones laterales con mancuernas, 4x10, Hombro",
    "Pájaros con mancuernas (inclinación), 3x12, Hombro",
    "Remo al mentón con barra, 4x10, Hombro",
    "Elevaciones posteriores con mancuernas, 3x12, Hombro",
    "Face pull con banda elástica, 4x12, Hombro",
    "Encogimientos de hombros con mancuernas, 4x12, Hombro",]

def extractExercise():
    localMap = {k: [] for k in mapExercise}

    for exercise in listExercise:
        # Separamos y eliminamos espacios extra
        name, reps, muscle = [part.strip() for part in exercise.split(",")]

        info = dataExercise.copy()
        info["name"] = name
        info["repetitions"] = reps
        info["muscle"] = muscle

        localMap[muscle].append(info)
    return localMap

