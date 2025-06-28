import matplotlib.pyplot as plt
import numpy as np

# Frequenzen in Hz
frequencies = np.array([100, 1000, 2275, 10_000, 100_000, 1_000_000, 5_000_000, 10_000_000])

# Ausgangsamplitude in mV
output_amplitudes_mv = np.array([60, 500, 740, 880, 920, 920, 640, 400])

# Eingangsamplitude in mV (0.1 Vpp = 100 mVpp)
input_amplitude_mv = 100

# Verstärkung in dB
gain_db = 20 * np.log10(output_amplitudes_mv / input_amplitude_mv)

# Phasenwinkel in Grad (angepasst: erste zwei Werte auf 0° gesetzt)
phases_deg = np.array([0, 0, -140, -170, -180, 170, 130, 91])

# Plot mit zwei Y-Achsen
fig, ax1 = plt.subplots(figsize=(10, 6))

# Verstärkung (linke Y-Achse)
ax1.set_xscale('log')
ax1.plot(frequencies, gain_db, 'o-', label='Verstärkung [dB]', color='blue')
ax1.set_xlabel('Frequenz [Hz]')
ax1.set_ylabel('Verstärkung [dB]', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.grid(True, which="both", ls="--")

# Phase (rechte Y-Achse)
ax2 = ax1.twinx()
ax2.plot(frequencies, phases_deg, 's--', label='Phase [°]', color='red')
ax2.set_ylabel('Phase [°]', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Gemeinsame Legende
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='best')


plt.tight_layout()
plt.savefig('plot_jpg/labor3_messungen_ohneC3.jpg', dpi=300)
plt.show()
