## NOTE
The number of distinct ways to climb to the top of a staircase with `n` steps, where you can take either `1` or `2` steps at a time, is given by the `(n+1)-th Fibonacci number`. The Fibonacci sequence is defined as `F(0) = 0`, `F(1) = 1`, and `F(n) = F(n-1) + F(n-2)` for `n >= 2`.

So, for example, if `n = 2`, the number of distinct ways to climb to the top is `F(3) = F(2) + F(1) = 1 + 1 = 2`. If `n = 3`, the number of distinct ways to climb to the top is `F(4) = F(3) + F(2) = 2 + 1 = 3`.

* The problem asks for the number of distinct ways to climb to the top of a staircase with n steps, where you can take either `1` or `2` steps at a time.
* This problem can be solved using dynamic programming, which is a technique that can be used to solve problems by breaking them down into smaller subproblems and storing the solutions to these subproblems to avoid redundant calculations.
* The dynamic programming solution uses an array `dp` of length `n+1` to store the solutions to the subproblems.
* The base cases are `dp[1] = 1` and `dp[2] = 2`, which correspond to the number of ways to climb a staircase with `1` or `2` steps.
* The for loop iterates from `3` to `n` and calculates the solution for each subproblem using the formula `dp[i] = dp[i-1] + dp[i-2]`, which corresponds to the recurrence relation for the Fibonacci sequence.
* Finally, the solution to the original problem is returned as `dp[i]`.
* This dynamic programming approach has a time complexity of `O(n)` and a space complexity of `O(n)`, which makes it much more efficient than the recursive approach for large values of `n`.
