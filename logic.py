#def numbers():
	#nums = [45, 55, 60, 37, 100, 105, 220]
	#if nums / n:
	#	print (nums)
def kil(n):


    u=0
    nums = [45, 55, 60, 37, 100, 105, 220]


    for i in range(len(nums)-1):
        if ((n != 0) and ((nums[i] % int(n)) == 0)) :
            	print(nums[i])
            	u=1
            
    if u == 0 :
        print ("Zbs...")