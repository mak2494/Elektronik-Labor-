import shutil

# kopiert die Datei ins aktuelle Verzeichnis (dort, wo dein Notebook-/Skript läuft)
shutil.copy('/mnt/data/realistic_C_measurement.csv', './realistic_C_measurement.csv')
print("Datei kopiert nach:", './realistic_C_measurement.csv')