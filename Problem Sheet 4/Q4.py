from distributions import hypergeometric_dist


def calculate_mean(counts, wattages):
    total = 0
    for count, wattage in zip(counts, wattages):
        total += count * wattage
    return total / sum(counts)


def calculate_variance(counts, wattages, expected_wattage):
    summation = 0
    for count, wattage in zip(counts, wattages):
        summation += ((wattage - expected_wattage) ** 2) * count
    return summation / sum(counts)


if __name__ == '__main__':
    counts = [17, 20, 10, 3]
    wattages = [40, 60, 75, 100]
    mean = calculate_mean(counts, wattages)
    variance = calculate_variance(counts, wattages, mean)
    chance_of_40_watt = counts[0] / sum(counts)
    print(f"Mean: {mean}")
    print(f"Variance: {variance}")
    print(f"Chance of 2 40W bulbs in 5: {hypergeometric_dist(2, 50, 17, 5)}")
