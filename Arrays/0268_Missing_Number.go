/*
Problem:
268. Missing Number

Difficulty:
Easy

Topics:
Array, Math

Approach:
Find the expected sum of numbers from 0 to n and subtract
the sum of the given array elements.

Time Complexity:
O(n)

Space Complexity:
O(1)
*/

func missingNumber(nums []int) int {
    n := len(nums)
    sum := 0
    total := 0

    for i := 0; i < n; i++ {
        sum += nums[i]
        total += i
    }

    total += n

    return total - sum
}