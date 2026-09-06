#similiar to consective elements 

nums = [1,1,0,2, 2, 2, 3, 3, 3, 3,3] 

ele = nums[0]
cnt = 1
mx_ele = ele
mx_cnt = 1

for i in range(0, len(nums)):
    
    if nums[i] == ele:
        cnt += 1 
    
    else:
        
        if cnt > mx_cnt:
            mx_cnt = cnt 
            mx_ele = ele 
        
        ele = nums[i] 
        cnt = 1
    

print(ele)
print(cnt)
