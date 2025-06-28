import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import interp1d


# Daten für den Frequenzgang RC-1.grad lowpass
frequenz1 = np.array([100, 200, 300, 340, 370, 400, 600, 800, 1000])
amplitude1 = np.array([0.14, 0.12, 0.11, 0.10, 0.095, 0.09, 0.075, 0.065, 0.06])
phase1     = np.array([0, 0, 20, 45, 50, 55, 65, 72, 76])              # in Grad

# Erstellen des DataFrames für den ersten Frequenzgang RC-1.grad lowpass
df_RC_LP = pd.DataFrame({
    'Frequenz [Hz]': frequenz1,
    'Amplitude [dB]': 20 *(np.log10(amplitude1 + 1e-6)),
    'Phase [°]': -phase1})

# Daten für den Frequenzgang RC-1.grad lowpass mit doppeltem Widerstand & Kondensator
frequenz2 = np.array([20, 30, 40, 50, 70, 84, 100, 150, 200, 250])
amplitude2 = np.array([1.05, 1.00, 0.95, 0.93, 0.88, 0.82, 0.75, 0.55, 0.4, 0.28])
phase2     = np.array([15, 21, 26, 32, 38, 45, 50, 58, 60, 75])

df_RC_LP2 = pd.DataFrame({
    'Frequenz [Hz]': frequenz2,
    'Amplitude [dB]':  20 * (np.log10(amplitude2 + 1e-6)),
    'Phase [°]': -phase2
})

# Daten für den Frequenzgang RLC-2.grad Lowpass
frequenz3 = np.array([800, 1000, 1500, 2000, 3000, 5000, 6000, 7000, 8000, 9000, 10000])
amplitude3 = np.array([1.05, 1.018, 0.95, 0.85, 0.65, 0.11, 0.08, 0.07, 0.05, 0.04, 0.025])
phase3     = np.array([2, 3.65, 8, 15, 25, 47, 80, 140, 160, 170, 177])         # in Grad

df_RLC_LP = pd.DataFrame({
    'Frequenz [Hz]': frequenz3,
    'Amplitude [dB]': 20 * (np.log10(amplitude3 + 1e-6)),     # Amplitude in dB umrechnen 
    'Phase [°]': -phase3
})


# Plotten der Bode-Diagramme
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Amplitudenplot mit beibehaltenen Farben, nur Linestyles geändert
ax1.semilogx(df_RC_LP['Frequenz [Hz]'], df_RC_LP['Amplitude [dB]'],
             linestyle='-',  marker='o', label='RC LP 1. Ordnung')
ax1.semilogx(df_RC_LP2['Frequenz [Hz]'], df_RC_LP2['Amplitude [dB]'],
             linestyle='--', marker='s', label='RC LP (2× R&C)')
ax1.semilogx(df_RLC_LP['Frequenz [Hz]'], df_RLC_LP['Amplitude [dB]'],
             linestyle=':',  marker='x', label='RLC LP 2. Ordnung')

ax1.set_ylabel('Amplitude [dB]')
ax1.grid(True, which='both')
ax1.legend()

# Phasenplot mit gleichen Linestyles
ax2.semilogx(df_RC_LP['Frequenz [Hz]'], df_RC_LP['Phase [°]'],
             linestyle='-',  marker='o', label='RC LP 1. Ordnung')
ax2.semilogx(df_RC_LP2['Frequenz [Hz]'], df_RC_LP2['Phase [°]'],
             linestyle='--', marker='s', label='RC LP (2× R&C)')
ax2.semilogx(df_RLC_LP['Frequenz [Hz]'], df_RLC_LP['Phase [°]'],
             linestyle=':',  marker='x', label='RLC LP 2. Ordnung')

ax2.set_xlabel('Frequenz [Hz]')
ax2.set_ylabel('Phase [°]')
ax2.grid(True, which='both')
ax2.legend()

plt.tight_layout()
plt.savefig('plot_jpg/bode_diagramm_labor2_vergleich.jpg', dpi=300)  # Speichern des Plots als JPEG
plt.show()
