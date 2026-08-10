func twoSum(numbers []int, target int) []int {
    index1 := 0 
    index2 := len(numbers) - 1


    for numbers[index1] + numbers[index2] != target  {

        if numbers[index1] + numbers[index2] < target {
            index1++
        } else {
            index2--
        }
    }

    return []int{index1 + 1,index2 + 1}


} 
