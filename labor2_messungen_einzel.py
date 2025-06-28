import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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


bode_daten = [
    (df_RC_LP,     'RC LP 1. Ordnung',    'bode_rc_lp.png'),
    (df_RC_LP2,    'RC LP (2× R&C)',      'bode_rcx2_lp.png'),
    (df_RLC_LP,    'RLC LP 2. Ordnung',   'bode_rlc_lp2.png')
]


# 3 Diagramme mit je zwei y-Achsen
for df, titel, dateiname in bode_daten:
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Amplituden-Achse (links)
    ax1.set_xlabel('Frequenz [Hz]')
    ax1.set_ylabel('Amplitude [dB]', color='blue')
    ax1.semilogx(df['Frequenz [Hz]'], df['Amplitude [dB]'],
                 color='blue', marker='o', label='Amplitude [dB]')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.grid(True, which='both', ls=':')

    # Phasen-Achse (rechts)
    ax2 = ax1.twinx()
    ax2.set_ylabel('Phase [°]', color='red')
    ax2.semilogx(df['Frequenz [Hz]'], df['Phase [°]'],
                 color='red', linestyle='--', marker='x', label='Phase [°]')
    ax2.tick_params(axis='y', labelcolor='red')

    # Gemeinsame Legende
    lines = ax1.get_lines() + ax2.get_lines()
    labels = [line.get_label() for line in lines]
    ax1.legend(lines, labels, loc='best')

    plt.tight_layout()
    plt.savefig(dateiname, dpi=300)
    plt.show()
