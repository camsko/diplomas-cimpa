import csv as csv
import re
from participant import Participant


medals = {"ORO", "PLATA", "BRONCE"}
areas = {"Ingeniería y Arquitectura", "Ciencias Básicas", "No soy estudiante UCR", "Salud", "Ciencias Sociales", "Docente UCR"}
    

def find_info(line_array):
    global medals
    global areas
    participant_info = ["", "", "", ""]

    for area in areas:
        if area in line_array:
            participant_info[3] = area
            line_array = line_array.replace(area, '')
            break

    for medal in medals:
        if medal in line_array:
            participant_info[2] = medal
            line_array = line_array.replace(medal, '')

            points = re.findall("\d+", line_array)[0]
            line_array = line_array.replace(points, '')
            participant_info[1] = points
            break

    participant_info[0] = re.sub("\s+$", "", line_array)
    return participant_info


def create_person(line):
    participant = Participant()
    participant_info = find_info(line)
    participant.create_from_parsed_text(participant_info[0], 
                                        participant_info[1], 
                                        participant_info[2], 
                                        participant_info[3])
    return participant


def txt_to_participants(filename):
    participants = []
    with open(filename, "r") as file:
        for line in file:
            participants.append(create_person(line))
    return participants

def participants_to_csv(filename, participants):
    with open(filename, "w") as file:
        writer = csv.DictWriter(file, fieldnames = ["Nombre", "Puntaje", "Medalla", "Área"])
        writer.writeheader()
        string = "\n".join(f"{p.name},{p.points},{p.medal},{p.area}" for p in participants)
        file.write(string)
        
def main():
    participants2024 = txt_to_participants("2024.txt")
    participants_to_csv("2024.csv", participants2024)    
    
    participants2025 = txt_to_participants("2025.txt")
    participants_to_csv("2025.csv", participants2025)

    return 0

main()