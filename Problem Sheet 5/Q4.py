
from scipy.stats import norm
import numpy as np
counts = np.array([3, 6, 5, 8, 7, 1])
midpoints = np.array([127, 132, 137, 142, 147, 152])


def calculate_sample_mean(counts, midpoints):
    return np.divide(np.sum(counts * midpoints), np.sum(counts))


def calculate_sample_variance(counts, midpoints, mean):
    return np.divide(np.sum(counts * np.square(midpoints - mean)), np.sum(counts) - 1)


def calculate_sample_standard_deviation(variance):
    return np.sqrt(variance)


def calculate_sample_median(counts, midpoints):
    return midpoints[np.argmax(counts)]

sample_mean = round(calculate_sample_mean(counts, midpoints))
sample_variance = calculate_sample_variance(counts, midpoints, sample_mean)
sample_standard_deviation = calculate_sample_standard_deviation(sample_variance)
sample_median = calculate_sample_median(counts, midpoints)

print(f"Part a:")
print(f"sample_mean: {sample_mean}")
print(f"sample_variance: {sample_variance}")
print(f"sample_standard_deviation: {sample_standard_deviation}")
print(f"sample_median: {sample_median}")
print()
data_points = [
    sample_mean - 2 * sample_standard_deviation,
    sample_mean - 1 * sample_standard_deviation,
    sample_mean,
    sample_mean + 1 * sample_standard_deviation,
    sample_mean + 2 * sample_standard_deviation
]
pdf_at_mean = norm.pdf(data_points, loc=sample_mean, scale = sample_standard_deviation)
print(f"Part b:")
print(f"-2sd, -1sd, mean, +1sd, +2sd: {data_points}")
print(f"pdfs at -2sd, -1sd, mean, +1sd, +2sd: {pdf_at_mean}")