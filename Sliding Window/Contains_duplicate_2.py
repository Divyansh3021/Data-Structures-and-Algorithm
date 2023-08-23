nums = [1, 2, 3, 1]
k = 3

current_window = set()

for i in range(len(nums)):
    if len(current_window) > k:
        current_window.pop(0)
    if nums[i] in current_window:
        print(True)
        break  # Exit the loop when a duplicate is found
    current_window.add(nums[i])
else:
    print(False)
