spells = [3,1,2]
potions = [8,5,8]
success = 16

potions = sorted(potions)
pairs = [0]*len(spells)

for i in range(len(spells)):
    left = 0
    right = len(potions) - 1

    while left <= right:
        mid = left + ((right - left)//2)

        print("Current product: ",spells[i] * potions[mid])

        if spells[i] * potions[mid] >= success:
            right = mid - 1
        
        else:
            left = mid + 1

    print("Mid element: ",mid)
    while mid< len(potions) and spells[i] * potions[mid] < success:
        mid += 1
    remaining_potions = len(potions) - mid
    pairs[i] = remaining_potions

print(pairs)