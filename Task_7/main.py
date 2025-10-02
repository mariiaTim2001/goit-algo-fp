import random
import matplotlib.pyplot as plt
from tabulate import tabulate

def monte_carlo(n_trials=1_000_000):
    sums_count = {i: 0 for i in range(2, 13)}

    # simulate dice rolls
    for _ in range(n_trials):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        sums_count[total] += 1

    probabilities = {s: count / n_trials for s, count in sums_count.items()}
    return probabilities, sums_count

# analytical probabilities for sums 2 to 12
analytical = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36,
    6: 5/36, 7: 6/36, 8: 5/36, 9: 4/36,
    10: 3/36, 11: 2/36, 12: 1/36
}

if __name__ == "__main__":
    n_trials = 1_000_000
    probabilities, counts = monte_carlo(n_trials)

    table = []
    for s in range(2, 13):
        table.append([
            s,
            counts[s],
            f"{probabilities[s]*100:.2f}%",
            f"{analytical[s]*100:.2f}%",
            f"{(probabilities[s]-analytical[s])*100:+.2f}%"
        ])

    print(tabulate(
        table,
        headers=["Сума", "Кількість випадків", "Монте-Карло (%)", "Аналітична (%)", "Різниця (%)"],
        tablefmt="fancy_grid"
    ))


    sums = list(probabilities.keys())
    monte_probs = [probabilities[s] for s in sums]
    analytical_probs = [analytical[s] for s in sums]

    plt.figure(figsize=(10, 6))
    plt.bar(sums, monte_probs, alpha=0.6, label="Монте-Карло")
    plt.plot(sums, analytical_probs, "ro-", label="Аналітичні", linewidth=2)
    plt.xlabel("Сума на кубиках")
    plt.ylabel("Ймовірність")
    plt.title("Ймовірності сум при киданні двох кубиків")
    plt.xticks(sums)
    plt.legend()
    plt.show()
