nums = [10, 20, 30, 20, 40]

def sum_numbers():
    return sum(nums)

def average_numbers():
    return sum(nums) / len(nums)

def mean_and_mode():
    mean = sum(nums) / len(nums)
    max_count = max(nums.count(n) for n in nums)
    # gets modes, watch out for ties
    modes = sorted(list(set([n for n in nums if nums.count(n) == max_count])))
    return mean, modes

print("NUMBER OPERATIONS")
print("1. Sum of numbers")
print("2. Average of numbers")
print("3. Mean and Mode")

choice = input("Choose a function (1-3): ")

if choice == "1":
    print("Sum:", sum_numbers())
elif choice == "2":
    print("Average:", average_numbers())
elif choice == "3":
    avg_val, m_val = mean_and_mode()
    print("Mean:", avg_val)
    print("Mode:", m_val)
else:
    print("Invalid choice")
