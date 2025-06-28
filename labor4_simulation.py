import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Datei laden
with open("data/labor3_ohneC3.txt", encoding="latin1") as f:
    lines = f.readlines()

# Daten parsen
data = []
for line in lines[1:]:
    parts = line.strip().split('\t')
    if len(parts) < 3:
        continue
    freq = float(parts[0])

    gain_vout = float(parts[1].split('dB')[0].replace('(', ''))
    phase_vout = float(parts[1].split(',')[1].replace('°)', ''))

    gain_ratio = float(parts[2].split('dB')[0].replace('(', ''))
    phase_ratio = float(parts[2].split(',')[1].replace('°)', ''))

    data.append((freq, gain_vout, phase_vout, gain_ratio, phase_ratio))

df = pd.DataFrame(data, columns=['Frequenz (Hz)', 'Gain_vout (dB)', 'Phase_vout (°)', 'Gain_ratio (dB)', 'Phase_ratio (°)'])

# Phase entpacken
phase_vout_unwrapped = np.degrees(np.unwrap(np.radians(df['Phase_vout (°)'])))
phase_ratio_unwrapped = np.degrees(np.unwrap(np.radians(df['Phase_ratio (°)'])))

# Plot mit 2 y-Achsen
fig, ax1 = plt.subplots(figsize=(10, 6))

# Farben
color_vout = 'blue'
color_ratio = 'red'

# Linke Achse: Gain
ax1.set_xscale('log')
ax1.plot(df['Frequenz (Hz)'], df['Gain_vout (dB)'], color=color_vout, label='|V(vout)|', linewidth=1.5)
ax1.plot(df['Frequenz (Hz)'], df['Gain_ratio (dB)'], color=color_ratio, linestyle='--', label='|V(vout)/V(vin)|', linewidth=1.5)
ax1.set_xlabel('Frequenz [Hz]')
ax1.set_ylabel('Gain [dB]')
ax1.set_ylim(-6, 21)

# Rechte Achse: Phase
ax2 = ax1.twinx()
ax2.plot(df['Frequenz (Hz)'], phase_vout_unwrapped, color=color_vout, linestyle='-.', label='∠V(vout)', linewidth=1.2)
ax2.plot(df['Frequenz (Hz)'], phase_ratio_unwrapped, color=color_ratio, linestyle='dotted', label='∠V(vout)/V(vin)', linewidth=1.2)
ax2.set_ylabel('Phase [°]')
ax2.set_ylim(-280, 200)

# Gemeinsame Legende (in der Mitte rechts im Plotbereich)
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='center right')

# Gitter & Layout
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.savefig('plot_jpg/labor3_ohneC3_simulation.jpg', dpi=300)  # Speichern des Plots als JPEG
plt.show()
