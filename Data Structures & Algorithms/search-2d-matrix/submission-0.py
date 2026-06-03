class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        counter = 0
        while counter < len(matrix):

            if matrix[counter][-1] < target:
                counter += 1
                continue

            leftIndex = 0
            rightIndex = len(matrix[counter]) - 1
            while leftIndex <= rightIndex:

                mid = (leftIndex + rightIndex) // 2

                if matrix[counter][mid] == target:
                    return True
                elif matrix[counter][mid] < target:
                    leftIndex = mid + 1
                elif matrix[counter][mid] > target:
                    rightIndex = mid - 1
                
            counter += 1
            
        return False

        