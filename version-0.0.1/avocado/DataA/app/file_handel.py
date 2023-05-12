
def write(pit, data):
    if pit == "0":
        pit = open("Pits\\Pit - a1\\Pit-000.txt", "w")
        pit.write(data)
    if pit == "1":
        pit = open("Pits\\Pit - a1\\Pit-001.txt", "w")
        pit.write(data)
    if pit == "2":
        pit = open("Pits\\Pit - a1\\Pit-002.txt", "w")
        pit.write(data)
    if pit == "3":
        pit = open("Pits\\Pit - a1\\Pit-003.txt", "w")
        pit.write(data)
    if pit == "4":
        pit = open("Pits\\Pit - a1\\Pit-004.txt", "w")
        pit.write(data)
    if pit == "5":
        pit = open("Pits\\Pit - a1\\Pit-005.txt", "w")
        pit.write(data)
    if pit == "6":
        pit = open("Pits\\Pit - a1\\Pit-006.txt", "w")
        pit.write(data)
    if pit == "7":
        pit == open("Pits\\Pit - a1\\Pit-007.txt", "w")
        pit.write(data)
    if pit == "8":
        pit = open("Pits\\Pit - a1\\Pit-008.txt", "w")
        pit.write(data)
    if pit == "9":
        pit = open("Pits\\Pit - a1\\Pit-009.txt", "w")
        pit.write(data)
    if pit == "10":
        pit = open("Pits\\Pit - a1\\Pit-010.txt", "w")
        pit.write(data)
    if pit == "11":
        pit = open("Pits\\Pit - a1\\Pit-011.txt", "w")
        pit.write(data)
    if pit == "12":
        pit = open("Pits\\Pit - a1\\Pit-012.txt", "w")
        pit.write(data)
    if pit == "13":
        pit = open("Pits\\Pit - a1\\Pit-013.txt", "w")
        pit.write(data)
    if pit == "14":
        pit = open("Pits\\Pit - a1\\Pit-014.txt", "w")
        pit.write(data)
    if pit == "15":
        pit = open("Pits\\Pit - a1\\Pit-015.txt", "w")
        pit.write(data)
    if pit == "16":
        pit = open("Pits\\Pit - a1\\Pit-016.txt", "w")
        pit.write(data)
    if pit == "17":
        pit = open("Pits\\Pit - a1\\Pit-017.txt", "w")
        pit.write(data)
    if pit == "18":
        pit = open("Pits\\Pit - a1\\Pit-018.txt", "w")
        pit.write(data)
    if pit == "19":
        pit = open("Pits\\Pit - a1\\Pit-019.txt", "w")
        pit.write(data)
    if pit == "20":
        pit = open("Pits\\Pit - a1\\Pit-020.txt", "w")
        pit.write(data)
    if pit == "21":
        pit = open("Pits\\Pit - a1\\Pit-021.txt", "w")
        pit.write(data)
    if pit == "22":
        pit = open("Pits\\Pit - a1\\Pit-022.txt", "w")
        pit.write(data)
    if pit == "23":
        pit = open("Pits\\Pit - a1\\Pit-023.txt", "w")
        pit.write(data)
    if pit == "24":
        pit = open("Pits\\Pit - a1\\Pit-024.txt", "w")
        pit.write(data)
    if pit == "25":
        pit = open("Pits\\Pit - a1\\Pit-025.txt", "w")
        pit.write(data)
    if pit == "26":
        pit = open("Pits\\Pit - a1\\Pit-026.txt", "w")
        pit.write(data)
def read(pit):
    if pit in range(0, 27):
        file_path = f"Pits\\Pit - a1\\Pit-{pit:03}.avo"
        with open(file_path, "r") as file:
            return file.read()
    else:
        return None
