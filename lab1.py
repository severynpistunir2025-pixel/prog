def is_subarray(nums1, nums2):
    n1 = len(nums1)
    if n1 == 0: return True
    for i in range(len(nums2) - n1 + 1):
        if nums2[i : i + n1] == nums1:
            return True
    return False

if __name__ == "__main__":
    try:
        print("Введіть числа через пробіл:")
        nums1 = [int(x) for x in input("nums1: ").split()]
        nums2 = [int(x) for x in input("nums2: ").split()]
        
        print(f"Результат: {is_subarray(nums1, nums2)}")
    except ValueError:
        print("Помилка: потрібно вводити лише числа!")

    print("\n")
    input()
