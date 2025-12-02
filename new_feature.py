def find_max(numbers):
    return max(numbers)

if __name__ == "__main__":
    nums = input("Enter numbers separated by spaces: ").split()
    nums = [float(n) for n in nums]
    print(find_max(nums))
