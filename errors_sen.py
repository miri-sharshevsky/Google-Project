import changes


class ErrorsSentence:
    def __init__(self):
        self.__swap = changes.Swap()
        self.__delete = changes.Delete()
        self.__add = changes.Add()

    def search(self, sentence, size):
        changes_arr = self.__swap.search(sentence, size)
        deletes_arr = self.__delete.search(sentence, size)
        add_arr = self.__add.search(sentence, size)
        
        merge_arr = self.sort(changes_arr + deletes_arr + add_arr)[::-1]
        return merge_arr[0:min(size, len(merge_arr))]

    def sort(self, array):
        for i,obj in enumerate(array):
            temp_score = obj.get_score()
            array[i] = (obj, temp_score)
        array.sort(key=lambda tup: tup[1])
        # array = self.removeDuplicates(array)
        return [arr[0] for arr in array]

    #
    # def removeDuplicates(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     if len(nums) == 0:
    #         return 0
    #     length = 1
    #     previous = nums[0]
    #     index = 1
    #     for i in range(1, len(nums)):
    #         if nums[i] != previous:
    #             length += 1
    #             previous = nums[i]
    #             nums[index] = nums[i]
    #             index += 1
    #     return nums
