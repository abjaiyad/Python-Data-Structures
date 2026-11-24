"""Age statistics and list operations."""


def calculate_median(values):
    """Return the median of a non-empty sequence of numbers."""
    if not values:
        raise ValueError("Cannot calculate the median of an empty sequence")

    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return float(ordered[middle])
    return (ordered[middle - 1] + ordered[middle]) / 2


def calculate_average(values):
    """Return the arithmetic mean of a non-empty sequence of numbers."""
    if not values:
        raise ValueError("Cannot calculate the average of an empty sequence")
    return sum(values) / len(values)


def main():
    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
    ages.sort()
    print("Sorted ages:", ages)

    minimum_age = min(ages)
    maximum_age = max(ages)
    print("Minimum age:", minimum_age)
    print("Maximum age:", maximum_age)

    ages.extend([minimum_age, maximum_age])
    ages.sort()
    print("Updated sorted ages:", ages)

    median_age = calculate_median(ages)
    average_age = calculate_average(ages)
    range_of_ages = maximum_age - minimum_age

    print("Median age:", median_age)
    print("Average age:", average_age)
    print("Range of ages:", range_of_ages)

    below_average = abs(minimum_age - average_age)
    above_average = abs(maximum_age - average_age)
    print("Distances from average:", below_average, above_average)


if __name__ == "__main__":
    main()
