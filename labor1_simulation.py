import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  # Sicherstellen, dass TkAgg Backend verwendet wird
import matplotlib.pyplot as plt

# 1. Daten einlesen
df = pd.read_csv(
    'Labor_15_5_25.txt',
    delim_whitespace=True,
    comment='#',
    header=0
)

# 2. Spalten umbenennen (optional, macht den Code lesbarer)
df = df.rename(columns={
    'V(vin)':       'Vin',
    'V(N001,Vin)':  'V_C',   # Spannung über C
    'V(N001,N002)': 'V_R',   # Spannung über R
    'V(n002)':      'V_L'    # Spannung über L
})

# 3. Plot
plt.figure(figsize=(10, 5))

# Eingangsspannung
plt.plot(df['time'], df['Vin'], linestyle='-',  label='Eingangsspannung')

# Spannung über C
plt.plot(df['time'], df['V_C'], linestyle='--', label='Spannung über C')

# Spannung über R
plt.plot(df['time'], df['V_R'], linestyle='-.', label='Spannung über R')

# Spannung über L
plt.plot(df['time'], df['V_L'], linestyle=':',  label='Spannung über L')

# Achsen und Titel
plt.xlabel('Zeit (s)')
plt.ylabel('Spannung (V)')
plt.title('LTspice-Simulation: RC-L-Schaltung')

# Gitternetz und Legende
plt.grid(True)
plt.legend(loc='upper right')

plt.tight_layout()
plt.savefig('labor1_simulation_plot.jpg', dpi=300, bbox_inches='tight')  # Optional: Speichern des Plots
plt.show()