import numpy as np
import matplotlib.pyplot as plt
import re

# Pfad zur Datei
dateipfad = 'data/lab2_RCL second order lowpass.txt'  # <- ändere das ggf. auf den richtigen Dateinamen

frequenzen = []
amplituden_db = []
phasen_grad = []

with open(dateipfad, 'r', encoding='cp1252') as file:
    lines = file.readlines()[1:]  # Header überspringen

    for line in lines:
        parts = line.strip().split('\t')
        if len(parts) != 2:
            continue

        freq_str = parts[0]
        val_str = parts[1].replace('°', '')  # Gradzeichen entfernen

        # Frequenz
        freq = float(freq_str)

        # Komplexwert extrahieren
        match = re.match(r'\(([-\deE.+]+)dB,([-\deE.+]+)', val_str)
        if match:
            db = float(match.group(1))
            phase = float(match.group(2))

            frequenzen.append(freq)
            amplituden_db.append(db)
            phasen_grad.append(phase)

# Plotten mit figsize
fig, ax1 = plt.subplots(figsize=(10, 6))

# Amplituden-Achse
ax1.set_xlabel('Frequenz [Hz]')
ax1.set_ylabel('Amplitude [dB]', color='blue')
line1, = ax1.semilogx(frequenzen, amplituden_db, color='blue', label='Amplitude [dB]')
ax1.tick_params(axis='y', labelcolor='blue')
# NEU: Ticks in 5er-Schritten setzen
min_db = int(min(amplituden_db)) - 5
max_db = int(max(amplituden_db)) + 5
ax1.set_yticks(np.arange(min_db, max_db + 1, 5))

# Phasen-Achse
ax2 = ax1.twinx()
ax2.set_ylabel('Phase [°]', color='red')
line2, = ax2.semilogx(frequenzen, phasen_grad, color='red', linestyle='--', label='Phase [°]')
ax2.tick_params(axis='y', labelcolor='red')

# Legende hinzufügen (kombiniert beide Achsen)
lines = [line1, line2]
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc='best')

plt.grid(True, which='both', ls=':')
plt.tight_layout()
#plt.savefig('plot_jpg/RCL_second_order_lowpass_simulation.jpg', dpi=300)
plt.show()