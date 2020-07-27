class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # This is an O(N) time solution to finding the if there are exactly
        # two indices of numbers that add to a specific target
        # example: nums = [2, 7, 11, 15]; target = 9
        # twoSum will return [0, 1] because nums[0] + nums[1] = 9
        
        # The track dictionary keeps track of the index that matches
        # to the expected number that will sum to the target
        track = {}
        
        for i in range(len(nums)):
            if nums[i] in track: 
                return [track[nums[i]], i]
            else: 
                # track[wanted matching value] = current index
                track[target - nums[i]] = i
        return None
