/*
Problem:
231. Power of Two

Difficulty:
Easy

Topics:
Math

Approach:
Start with 1 and repeatedly multiply by 2.
If the value reaches n, then n is a power of two.

Time Complexity:
O(log n)

Space Complexity:
O(1)
*/

func isPowerOfTwo(n int) bool {
	if n == 1 {
		return true
	} else {
		i := 1

		for i < n {
			i *= 2
		}

		if i == n {
			return true
		} else {
			return false
		}
	}
}