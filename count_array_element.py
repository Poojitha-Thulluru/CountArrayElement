# The below brute force approach has Time complexity as O(N^2)
# def has_greater(element: int, nums_array: list) -> bool:
#     for value in nums_array:
#         if value > element:
#             return True
#     return False
#
#
# def get_element_count(nums_array):
#     count = 0
#     for element in nums_array:
#         if has_greater(element, nums_array):
#             count += 1
#     return count
#
#
# try:
#     num_array = list(map(int, input("Enter integers separated by space : ").split()))
#     print(get_element_count(num_array))
# except ValueError:
#     print("Invalid input. Please enter only integers")

# Optimized Approach with Time Complexity O(N)

def get_element_count(nums_array: list) -> int:
    max_element = max(nums_array)  # O(N)
    max_element_count: int = 0
    for element in nums_array:
        if element == max_element:
            max_element_count += 1
    return len(nums_array) - max_element_count


try:
    num_array = list(map(int, input("Enter Integers separated by space : ").split()))
    print("The count is : ", get_element_count(num_array))
except ValueError:
    print("Invalid input. Please enter only integers")
