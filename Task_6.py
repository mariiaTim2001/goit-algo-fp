items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True
    )

    total_cost = 0
    total_calories = 0
    chosen = []

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            chosen.append(name)
            total_cost += data["cost"]
            total_calories += data["calories"]

    return chosen, total_cost, total_calories


def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = names[i - 1]
        cost = items[name]["cost"]
        cal = items[name]["calories"]

        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + cal)
            else:
                dp[i][w] = dp[i - 1][w]

    chosen = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen.append(names[i - 1])
            w -= items[names[i - 1]]["cost"]

    chosen.reverse()
    return chosen, sum(items[i]["cost"] for i in chosen), dp[n][budget]


if __name__ == "__main__":
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    print("Жадібний алгоритм:")
    print("Вибрані страви:", greedy_result[0])
    print("Витрати:", greedy_result[1])
    print("Калорії:", greedy_result[2])

    dp_result = dynamic_programming(items, budget)
    print("\nДинамічне програмування:")
    print("Вибрані страви:", dp_result[0])
    print("Витрати:", dp_result[1])
    print("Калорії:", dp_result[2])
