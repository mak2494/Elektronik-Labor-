import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('scope_4.csv', skiprows=1, dtype=str)
df.columns = ['time', 'ch1', 'ch2']
df['time'] = df['time'].str.replace('+', '', regex=False).astype(float)
df['1'] = df['ch1'].str.replace('+', '', regex=False).astype(float)
df['2'] = df['ch2'].str.replace('+', '', regex=False).astype(float)

df = df.iloc[::20]

df['time'] = (df['time'] - df['time'].min())   # µs

plt.figure(figsize=(10, 6))
plt.plot(df['time'] * 1e6, df['1'] * 1000, linewidth=1, color='blue', label='Funktionsgenerator (mV)', linestyle='--')
plt.plot(df['time'] * 1e6, df['2'] * 1000, linewidth=1, color='red', label='Messung an C (mV)', linestyle='-')    

plt.xlabel('Zeit (µs)')
plt.ylabel('Spannung (mV)')
plt.title('Oszilloskop-Plot')
plt.legend()

plt.xlim(0, df['time'].max() * 1e6)  # Hier wird die x-Achse fixiert

plt.savefig('labor1_sinusplot_MessungC.jpg', dpi=300, bbox_inches='tight')
plt.show()
