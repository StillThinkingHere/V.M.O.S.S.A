
def write(pit, data):
    if pit == "0":
        pit = open("Pits\\Pit - a1\\Pit-000.avo", "w")
        pit.write(data)
    if pit == "1":
        pit = open("Pits\\Pit - a1\\Pit-001.avo", "w")
        pit.write(data)
    if pit == "2":
        pit = open("Pits\\Pit - a1\\Pit-002.avo", "w")
        pit.write(data)
    if pit == "3":
        pit = open("Pits\\Pit - a1\\Pit-003.avo", "w")
        pit.write(data)
    if pit == "4":
        pit = open("Pits\\Pit - a1\\Pit-004.avo", "w")
        pit.write(data)
    if pit == "5":
        pit = open("Pits\\Pit - a1\\Pit-005.avo", "w")
        pit.write(data)
    if pit == "6":
        pit = open("Pits\\Pit - a1\\Pit-006.avo", "w")
        pit.write(data)
    if pit == "7":
        pit == open("Pits\\Pit - a1\\Pit-007.avo", "w")
        pit.write(data)
    if pit == "8":
        pit = open("Pits\\Pit - a1\\Pit-008.avo", "w")
        pit.write(data)
    if pit == "9":
        pit = open("Pits\\Pit - a1\\Pit-009.avo", "w")
        pit.write(data)
    if pit == "10":
        pit = open("Pits\\Pit - a1\\Pit-010.avo", "w")
        pit.write(data)
    if pit == "11":
        pit = open("Pits\\Pit - a1\\Pit-011.avo", "w")
        pit.write(data)
    if pit == "12":
        pit = open("Pits\\Pit - a1\\Pit-012.avo", "w")
        pit.write(data)
    if pit == "13":
        pit = open("Pits\\Pit - a1\\Pit-013.avo", "w")
        pit.write(data)
    if pit == "14":
        pit = open("Pits\\Pit - a1\\Pit-014.avo", "w")
        pit.write(data)
    if pit == "15":
        pit = open("Pits\\Pit - a1\\Pit-015.avo", "w")
        pit.write(data)
    if pit == "16":
        pit = open("Pits\\Pit - a1\\Pit-016.avo", "w")
        pit.write(data)
    if pit == "17":
        pit = open("Pits\\Pit - a1\\Pit-017.avo", "w")
        pit.write(data)
    if pit == "18":
        pit = open("Pits\\Pit - a1\\Pit-018.avo", "w")
        pit.write(data)
    if pit == "19":
        pit = open("Pits\\Pit - a1\\Pit-019.avo", "w")
        pit.write(data)
    if pit == "20":
        pit = open("Pits\\Pit - a1\\Pit-020.avo", "w")
        pit.write(data)
    if pit == "21":
        pit = open("Pits\\Pit - a1\\Pit-021.avo", "w")
        pit.write(data)
    if pit == "22":
        pit = open("Pits\\Pit - a1\\Pit-022.avo", "w")
        pit.write(data)
    if pit == "23":
        pit = open("Pits\\Pit - a1\\Pit-023.avo", "w")
        pit.write(data)
    if pit == "24":
        pit = open("Pits\\Pit - a1\\Pit-024.avo", "w")
        pit.write(data)
    if pit == "25":
        pit = open("Pits\\Pit - a1\\Pit-025.avo", "w")
        pit.write(data)
    if pit == "26":
        pit = open("Pits\\Pit - a1\\Pit-026.avo", "w")
        pit.write(data)
def read(pit):
    if pit in range(0, 27):
        file_path = f"Pits\\Pit - a1\\pit-{pit:03}.avo"
        with open(file_path, "r") as file:
            return file.read()
    else:
        return None
