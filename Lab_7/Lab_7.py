# (Скоріше всього не правильний код)
from voting.profile import Profile
from voting.voting_methods import AbsoluteMajority, RelativeMajority, Borda, Condorcet, Copeland, Simpson

# Заданий профіль голосування
votes = [
    (5, ['B', 'C', 'D', 'A']),
    (6, ['C', 'A', 'B', 'D']),
    (7, ['D', 'B', 'C', 'A']),
    (2, ['A', 'B', 'C', 'D']),
]

# Створення профілю
profile = Profile(votes)

# Створення об'єктів для різних методів(Правил) голосування
absolute_majority = AbsoluteMajority()
relative_majority = RelativeMajority()
borda = Borda()
condorcet = Condorcet()
copeland = Copeland()
simpson = Simpson()

# Визначення переможців за різними методами(правилами)
winners = {
    "Absolute Majority": absolute_majority.get_winner(profile),
    "Relative Majority": relative_majority.get_winner(profile),
    "Borda": borda.get_winner(profile),
    "Condorcet": condorcet.get_winner(profile),
    "Copeland": copeland.get_winner(profile),
    "Simpson": simpson.get_winner(profile),
}

# Виведення переможців
for method, winner in winners.items():
    print(f"{method}: {winner}")

# Створення колективного ранжування
ranking = []

for _ in range(len(votes[0][1])):
    winner = absolute_majority.get_winner(profile)
    ranking.append(winner)
    profile.remove_candidate(winner)

# Виведення колективного ранжування
print("\nCollective Ranking:")
for i, candidate in enumerate(ranking):
    print(f"{i+1}. {candidate}")