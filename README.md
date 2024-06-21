# Problem_Solving
## Grumpy Bookstore Owner (leetcode)

This problem revolves around a bookstore owner who is open for `n` minutes. During each minute, a certain number of customers enter the store. This is represented by the `customers` array, where `customers[i]` is the number of customers that enter the store at the start of the `i`th minute.

However, the bookstore owner can sometimes be grumpy. This is represented by the `grumpy` array, where `grumpy[i]` is `1` if the bookstore owner is grumpy during the `i`th minute, and `0` otherwise.

When the bookstore owner is grumpy, the customers of that minute are not satisfied. But when the owner is not grumpy, the customers are satisfied.

The bookstore owner has a secret technique that allows them to not be grumpy for `minutes` consecutive minutes, but they can only use this technique once.

The goal of the problem is to return the maximum number of customers that can be satisfied throughout the day. This involves figuring out the best time for the bookstore owner to use their technique to maximize customer satisfaction.

For example, if `customers = [1,0,1,2,1,1,7,5]`, `grumpy = [0,1,0,1,0,1,0,1]`, and `minutes = 3`, the bookstore owner should use their technique during the last 3 minutes to satisfy the maximum number of customers, which would be 16 in this case.

### Python Solution

The Python solution uses a sliding window approach. First, it calculates the total number of satisfied customers when the bookstore owner is not grumpy. Then, it subtracts these customers from the `customers` array. After that, it calculates the maximum number of customers that can be satisfied when the bookstore owner uses their technique. It uses a sliding window of size `minutes` to find the maximum sum in the `customers` array. The final result is the sum of the total number of satisfied customers when the bookstore owner is not grumpy and the maximum number of customers that can be satisfied when the bookstore owner uses their technique.
### Time and Space Complexity

The time complexity of the solution is O(n), where n is the length of the `customers` array. This is because we iterate over the `customers` array once.

The space complexity of the solution is O(1), as we only use a constant amount of space to store the total number of satisfied customers and the maximum number of customers that can be satisfied when the bookstore owner uses their technique.
![Space Complexity](space_com_leet_AI.png)