import pandas as pd
import numpy as np

# Вхідні дані
data = {
    'Альтернатива': ['А1', 'А2', 'А3', 'А4', 'А5'],
    'К1': [540, 480, 390, 500, 350],
    'К2': [0.28, 0.22, 0.15, 0.24, 0.12],
    'К3': [22, 10, 5, 13, 7],
    'К4': [7, 6, 3, 8, 5],
    'Вага': [7, 8, 6, 5]
}

df = pd.DataFrame(data)

# Нормалізація ваг
weights = df['Вага'] / df['Вага'].sum()

# Розрахунок показників для кожної альтернативи
df['Песимізм'] = df[['К1', 'К2', 'К3', 'К4']].min(axis=1)
df['Оптимізм'] = df[['К1', 'К2', 'К3', 'К4']].max(axis=1)
df['Гурвіц'] = 0.5 * df['Песимізм'] + 0.5 * df['Оптимізм']
df['Лаплас'] = (1 / len(df.columns[1:])) * df[['К1', 'К2', 'К3', 'К4']].sum(axis=1)
df['Байєс-Лаплас'] = (df['К1'] * weights['К1'] +
                      df['К2'] * weights['К2'] +
                      df['К3'] * weights['К3'] +
                      df['К4'] * weights['К4'])
df['Ходжа-Леман'] = df['К1'] * weights['К1'] + df['К2'] * weights['К2']

# Знаходження альтернативи з максимальним значенням для кожного показника
max_pessimism = df.loc[df['Песимізм'].idxmax()]
max_optimism = df.loc[df['Оптимізм'].idxmax()]
max_gurwitz = df.loc[df['Гурвіц'].idxmax()]
max_laplace = df.loc[df['Лаплас'].idxmax()]
max_bayes_laplace = df.loc[df['Байєс-Лаплас'].idxmax()]
max_hodge_lehmann = df.loc[df['Ходжа-Леман'].idxmax()]

# Виведення результатів
print("За критерієм Песимізму обираємо альтернативу:", max_pessimism['Альтернатива'])
print("За критерієм Оптимізму обираємо альтернативу:", max_optimism['Альтернатива'])
print("За критерієм Гурвіца обираємо альтернативу:", max_gurwitz['Альтернатива'])
print("За критерієм Лапласа обираємо альтернативу:", max_laplace['Альтернатива'])
print("За критерієм Байєса-Лапласа обираємо альтернативу:", max_bayes_laplace['Альтернатива'])
print("За критерієм Ходжа-Лемана обираємо альтернативу:", max_hodge_lehmann['Альтернатива'])