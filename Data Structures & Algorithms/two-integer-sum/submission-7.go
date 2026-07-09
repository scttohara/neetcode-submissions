func twoSum(nums []int, target int) []int {
	seen := make(map[int]int)
	for index, value := range nums {
		complement := target - value
		if _, ok := seen[value]; ok {
			return []int{seen[value], index}
		} else {
			seen[complement] = index
		}
	}
	return []int{}
}
