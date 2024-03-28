import random
import statistics

# Generate random data
data = [random.randint(1, 100) for _ in range(10)]

# Calculate mean
mean = statistics.mean(data)

# Calculate median
median = statistics.median(data)

# Calculate mode
mode = statistics.mode(data)

# Calculate variance
variance = statistics.variance(data)

# Calculate standard deviation
std_dev = statistics.stdev(data)

# Print the results
print(f"Generated Data: {data}")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev}")

