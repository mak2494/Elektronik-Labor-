import pandas as pd
import matplotlib.pyplot as plt

# 1. CSV einlesen (zwei Header-Zeilen überspringen)
df = pd.read_csv('data/C_Messung_Positive_Puls_1kHz_realistisch.csv', skiprows=2, names=['time_s', 'Vin_V', 'Vc_V'])

# 2. Zeit in Millisekunden umrechnen
df['time_ms'] = df['time_s'] * 1e3

# 3. Filter: Nur Daten von 0 bis 2 ms
df = df[df['time_ms'] <= 2.0]

# 4. Optional: jeden 20. Punkt für bessere Lesbarkeit
df = df.iloc[::20]

# 5. Plot erstellen
plt.figure(figsize=(10, 6))

plt.plot(df['time_ms'], df['Vin_V'], linestyle='-', linewidth=1.5, label='Vin (1 Vpp, 1 kHz)')
plt.plot(df['time_ms'], df['Vc_V'], linestyle='--', linewidth=1.5, label='VC (über C)')

plt.xlabel('Zeit (ms)')
plt.ylabel('Spannung (V)')
plt.grid(True)
plt.legend(loc='upper right')
plt.tight_layout()

# 6. Plot speichern und anzeigen
plt.savefig('plot_jpg/PositiverPuls_MessungC__1Vpp_1kHz_DCoffset0.5.jpg', dpi=300)
plt.show()