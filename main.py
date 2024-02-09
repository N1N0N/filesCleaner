import os
import shutil

#Weisst verschiedenen Extensions den entsprechenden Dateitypen zu

extension_assignment = {
    'txt': 'Text Dokumente',
    'pdf': 'Text Dokumente',
    'docx': 'Text Dokumente',
    'doc': 'Text Dokumente',
    'png': 'Bilder',
    'jpg': 'Bilder',
    'jpeg': 'Bilder',
    'gif': 'Bilder',
    'tiff': 'Bilder',
    'mp4': 'Videos',
    'mov': 'Videos',
    'avi': 'Videos',
    'mkv': 'Videos',
    'zip': 'Komprimierte Archive',
    'rar': 'Komprimierte Archive',
    'exe': 'Programme',
    'mp3': 'Audiodateien',
    'wav': 'Audiodateien',
    #... mehr in Zukunft
}

def sort_files():
    folder_path = ''
    if not os.path.exists('standartFolder.txt'): #Falls kein Standartordner existiert mit normalen Abfrage starten
        folder_path = input("Ordner, der aufgeraeumt werden soll: ")
        if not os.path.exists(folder_path):
            print("Dieser Ordner existiert nicht!")
            return
        saveDecision = input("Willst du diesen Ordner fuer das naechste mal Speichern?: (Y/n)") #Speichern von Standartordner
        if saveDecision == 'Y' and not os.path.exists('standartFolder.txt'):
            with open('standartFolder.txt', 'w') as standartFolder:
                standartFolder.write(folder_path)

    else:
        with open('standartFolder.txt', 'r') as standartFolder:
            folder_path = standartFolder.read().strip() #Liesst Standartordner.txt und weisst folder_path den Inhalt zu
            shouldContinue = input(f"Willst du mit dem Standart Ordner '{folder_path}' fortfahren? (Y/n)")
            if shouldContinue.lower() != 'y':
                newStandart = input("Willst du einen neuen Standart Ordner anlegen? (Y/n)")
                if newStandart.lower() != 'y':
                    folder_path = input("Ordner, der aufgeraeumt werden soll: ")
                    if not os.path.exists(folder_path):
                        print("Dieser Ordner existiert nicht!")
                        return
                else:
                    standartFolder.close()
                    os.remove('standartFolder.txt')
                    folder_path = input("Neuer Standart-Ordner: ")
                    with open('standartFolder.txt', 'w') as standartFolder:
                        standartFolder.write(folder_path)

    counter = 0

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item) #Kombiniert file path und Dateiname
        if os.path.isfile(item_path):
            _, ext = os.path.splitext(item) #Extension extrahieren
            ext = ext[1:].lower() #Punkt entfernen und in Kleinbuchstaben umwandeln
            if ext in extension_assignment:
                folder_name = extension_assignment[ext] #Entscheidet wohin Datei kommt anhand von Extension
                destination_folder_path = os.path.join(folder_path, folder_name)
                if not os.path.exists(destination_folder_path): #Erstellt Ordner falls er nicht existiert
                    os.makedirs(destination_folder_path)
                shutil.move(item_path, destination_folder_path) #Bewegt Files in die Ordner
                counter = counter + 1
                print(f"{item} in {folder_name} verschoben")
            else:
                print(f"Keine Zuordung fuer {item} gefunden, uebersprungen.")
    print(f"Es wurden {counter} Dokumente verschoben")

if __name__ == "__main__":
    sort_files()
