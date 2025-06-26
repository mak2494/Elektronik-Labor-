import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import interp1d


# Daten für den Frequenzgang RC-1.grad lowpass
frequenz1 = np.array([200, 340, 400, 1000, 5000])          # in Hz
amplitude1 = np.array([0.12, 0.1, 0.09, 0.06, 0])             # linear 
phase1 = np.array([0, 45, 55, 76, 0])                # in Grad

# Erstellen des DataFrames für den ersten Frequenzgang RC-1.grad lowpass
df_RC_LP = pd.DataFrame({
    'Frequenz [Hz]': frequenz1,
    'Amplitude [dB]': 20 *(np.log10(amplitude1 + 1e-6)),
    'Phase [°]': phase1})

# Daten für den Frequenzgang RC-1.grad lowpass mit doppeltem Widerstand & Kondensator
frequenz2 = np.array([30, 50, 84, 200, 250])          # in Hz
amplitude2 = np.array([11.1/10.3, 11.1/9.6, 11.1/8, 11.1/5, 11.1/4.2])             # linear 
phase2 = np.array([21,32,45, 60,75])

df_RC_LP2 = pd.DataFrame({
    'Frequenz [Hz]': frequenz2,
    'Amplitude [dB]':  20 * (np.log10(amplitude2 + 1e-6)),
    'Phase [°]': phase2
})

# Daten für den Frequenzgang RLC-2.grad Lowpass
frequenz3 = np.array([1000, 2000, 5000, 7000, 10000])          # in Hz
amplitude3 = np.array([10.9/10.7, 9/10.5, 0.8/7.4, 3.62/4.6, 6.8/2.61])             # linear 
phase3 = np.array([3.65, 4.16, 47, 172, 177])           # in Grad

df_RLC_LP = pd.DataFrame({
    'Frequenz [Hz]': frequenz3,
    'Amplitude [dB]': 20 * (np.log10(amplitude3 + 1e-6)),     # Amplitude in dB umrechnen 
    'Phase [°]': phase3
})

# Logarithmische Interpolation vorbereiten
def log_interp(x, y, num=20):
    logx = np.log10(x)
    interp_func = interp1d(logx, y, kind='linear')
    logx_new = np.linspace(logx.min(), logx.max(), num)
    return 10**logx_new, interp_func(logx_new)

# Interpolieren für glattere Kurven
f1_new, a1_new = log_interp(frequenz1, amplitude1, 20)
_, p1_new = log_interp(frequenz1, phase1, 20)

f2_new, a2_new = log_interp(frequenz2, amplitude2, 20)
_, p2_new = log_interp(frequenz2, phase2, 20)

f3_new, a3_new = log_interp(frequenz3, amplitude3, 20)
_, p3_new = log_interp(frequenz3, phase3, 20)

# dB-Umrechnung
a1_db = 20 * np.log10(a1_new + 1e-6)
a2_db = 20 * np.log10(a2_new + 1e-6)
a3_db = 20 * np.log10(a3_new + 1e-6)

# Plotten der Bode-Diagramme
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Amplitude
ax1.semilogx(f1_new, a1_db, 'o-', label='RC LP 1. Ordnung')
ax1.semilogx(f2_new, a2_db, 's-', label='RC LP (2x R & C)')
ax1.semilogx(f3_new, a3_db, 'x-', label='RLC LP 2. Ordnung')
ax1.set_ylabel('Amplitude [dB]')
ax1.set_title('Bode-Diagramm: Amplitude')
ax1.grid(True, which='both')
ax1.legend()

# Phase
ax2.semilogx(f1_new, p1_new, 'o-', label='RC LP 1. Ordnung')
ax2.semilogx(f2_new, p2_new, 's-', label='RC LP (2x R & C)')
ax2.semilogx(f3_new, p3_new, 'x-', label='RLC LP 2. Ordnung')
ax2.set_xlabel('Frequenz [Hz]')
ax2.set_ylabel('Phase [°]')
ax2.set_title('Bode-Diagramm: Phase')
ax2.grid(True, which='both')
ax2.legend()

plt.tight_layout()
plt.show()

