# Multiple Choice Quiz von VirusMc

## Spielanleitung

1. Eingeben wie viel Fragen man beantworten will
2. Fragen beantworten
3. Spaß haben

## Wie erweitere ich die Fragen?

1. `questions`-Ordner öffnen
2. Kopie von `questions.json` erstellen
3. Die Kopie nach Belieben anpassen
4. Die Datei umbenennen und den Dateinamen in die `valid_questions.valid`-Datei als neue Zeile einfügen !!!

### Anpassungsmöglichkeiten

- `name`: Titel der Frage
- `question`: Die eigentliche Frage
- `answers`: Alle Antwortmöglichkeiten
- `correctAnswer`: Die richtige Antwort (Wichtig: muss in `answers` vorhanden sein!)
- `category`: Die richtige Zahl entsprechend der Kategorie
    - Keine = 0
    - Allgemein Wissen = 1
    - Geschichte = 2
    - Wissenschaft = 3