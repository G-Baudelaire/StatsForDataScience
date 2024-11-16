from distributions import multinomial_dist

if __name__ == '__main__':
    occurrences = [1, 2, 3]
    probabilities = [0.2, 0.3, 0.5]
    print(f"Solution to 2a: {multinomial_dist(occurrences, probabilities)}")
    occurrences = [2, 2, 2]
    print(f"Solution to 2b: {multinomial_dist(occurrences, probabilities)}")
