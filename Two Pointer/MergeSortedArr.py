nums1 = [1,2,3,0,0,0]
m,n = 3,3
nums2 = [2,5,6]

for j in range(n):
    nums1[m+j] = nums2[j]

nums1 = sorted(nums1)

print(nums1)