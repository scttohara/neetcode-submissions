class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        integer_frequency = {}

        for number in nums:
            if number not in integer_frequency:
                integer_frequency[number] = 1
            else:
                integer_frequency[number] +=1

        real_numbers = []
        count_of_real_numbers = []
        for current_number, count_of_app in integer_frequency.items():
            real_numbers.append(current_number)
            count_of_real_numbers.append(count_of_app)
            
        
        n = len(count_of_real_numbers)
        #test = range(n)
        for i in range(n-1):
            for j in range(n-i-1):
                if count_of_real_numbers[j] > count_of_real_numbers[j+1]:
                    count_of_real_numbers[j], count_of_real_numbers[j+1] = count_of_real_numbers[j+1], count_of_real_numbers[j]
                    real_numbers[j], real_numbers[j + 1] = real_numbers[j + 1], real_numbers[j]
        
        list_to_return = []
        while k != 0:
            
            current = real_numbers.pop()
            list_to_return.append(current)

            k -= 1


        return list_to_return