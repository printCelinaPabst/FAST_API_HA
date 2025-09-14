import json

# FUNCTION get_all_employees():
# # Daten aus Datenbank laden
# TRY:
# employees = LOAD all employees FROM database
# CATCH database_error:
# RETURN error("Fehler beim Laden der Mitarbeiter")

def lade_mitarbeiter():
    try:
        with open("./mitarbeiter_daten.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Die Datei wurde nicht gefunden.")
        return None

# # Vertrauliche Daten entfernen
# safe_employees = []
# FOR EACH employee IN employees:
# safe_employee = {
# id: employee.id,
# name: employee.name,
# email: employee.email,
# position: employee.position,
# start_date: employee.start_date
# # Gehalt bewusst NICHT zurückgeben!
# }
# ADD safe_employee TO safe_employees
# RETURN success("Mitarbeiter geladen", safe_employees)
