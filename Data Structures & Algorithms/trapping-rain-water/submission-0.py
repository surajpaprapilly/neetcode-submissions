class Solution:
    def trap(self, height: List[int]) -> int:
        max_left_arr = []
        max_right_arr = [0] * len(height)
        min_left_right_arr = []

        max_left = 0
        max_right = 0
        res = 0
        
        for i in range(0,len(height)):
            if i == 0:
                max_left = 0
                max_left_arr.append(max_left)
            else:
                max_left = max(max_left,height[i-1])
                max_left_arr.append(max_left)
        for i in range(len(height)-1,-1,-1):
            if i == len(height)-1:
                max_right = 0
                max_right_arr.append(max_right)
            else:
                max_right = max(max_right,height[i+1])
                max_right_arr[i] = max_right

        for j in range(0,len(height)):
            min_left_right_arr.append(min(max_left_arr[j],max_right_arr[j]))

        for k in range(0,len(height)):
            res += max(0,min_left_right_arr[k]-height[k])
        return res

















