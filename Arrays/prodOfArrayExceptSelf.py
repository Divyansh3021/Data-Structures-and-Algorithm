nums = [1,2,3,4]
answer = []

length=len(nums)
sol=[1]*length
pre = 1
post = 1
for i in range(length):
    sol[i] *= pre
    pre = pre*nums[i]
    sol[length-i-1] *= post
    post = post*nums[length-i-1]
    print("Sol[i] for i = ",i," is: ", sol[i])
    print("pre for i = ",i," is: ", pre)
    print("post for i = ",i," is: ", post,"\n\n\n")

print(sol)