# data_analysis.py
import sys

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    if length % 2 == 0:
        return (sorted_numbers[length // 2 - 1] + sorted_numbers[length // 2]) / 2
    else:
        return sorted_numbers[length // 2]

if __name__ == "__main__":
    data = [float(arg) for arg in sys.argv[1:]]
    print('Mean:', calculate_mean(data))
    print('Median:', calculate_median(data))

# if __name__ == "__main__":
#     data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
#     print('Mean:', calculate_mean(data))  # Output: Mean: 4.0
#     print('Median:', calculate_median(data))  # Output: Median: 4
