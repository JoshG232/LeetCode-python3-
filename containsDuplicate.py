def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    newNums = []
    for x in nums:
        
        if x in newNums:
            print("True")
            return True
        newNums.append(x)
    print("False")
    return False


containsDuplicate([1,2,3])