import random
def quick_sort(nums): # Быстрая сортировка
    if len(nums) <= 1:
        return nums
    
    q = nums[random.randint(0, len(nums)-1)]
    low = [i for i in nums if i < q]
    eq = [i for i in nums if i == q]
    high = [i for i in nums if i > q]
    return quick_sort(low) + eq + quick_sort(high)


def comb(nums): # Сортировка расческой
    step, swap = int(len(nums)/1.247), 1
    while step > 1 or swap > 0:
        swap, i = 0, 0
        while i + step < len(nums):
            if nums[i] > nums[i+step]:
                nums[i], nums[i+step] = nums[i+step], nums[i]
                swap += 1
            i += 1
        if step > 1:
            step = int(step/1.247)
    return nums