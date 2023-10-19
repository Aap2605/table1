def sum_and_average(numbers):
    if not numbers:
        return None, None
    total = sum(numbers)
    average = total / len(numbers)
    return total, average
numbers_list = [10, 20, 30, 40, 50]
total_sum, avg = sum_and_average(numbers_list)
if total_sum is not None and avg is not None:
    print(f"Sum: {total_sum}")
    print(f"Average: {avg}")
else:
    print("The list is empty.")
