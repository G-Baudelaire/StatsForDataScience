from distributions import negative_binomial_dist
if __name__ == '__main__':
    print(f"Probability of 5 free throws for 3rd basket: {negative_binomial_dist(5, 3, 0.7)}")
    chance = sum(negative_binomial_dist(x, 3, 0.7) for x in range(3,6))
    print(f"Probability of baskets in 5 free throws: {chance}")
    print(f"1st free throw on 5th throw: {negative_binomial_dist(5,1, 0.7)} = {(0.3 ** 4) * 0.7}")
