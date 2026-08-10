func twoSum(numbers []int, target int) []int {
    index1 := 0 
    index2 := len(numbers) - 1

    for index1 < index2 {
        sum := numbers[index1] + numbers[index2]
        
        if sum == target {
            return []int{index1 + 1, index2 + 1}
        } else if sum < target {
            index1++
        } else {
            index2--
        }
    }
    
    return []int{} 
}