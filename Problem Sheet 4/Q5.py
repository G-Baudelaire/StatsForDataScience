from distributions import hypergeometric_dist
if __name__ == '__main__':
    print(f"Chance of 3 red cards is: {hypergeometric_dist(3, 20, 6 ,5)}")