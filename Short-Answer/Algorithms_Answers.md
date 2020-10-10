#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime of this would be O(n) or linear time. This code has a while loop that would take n steps to finish running. So as n gets larger, the runtime would increase in a linear manner.


b) The runtime of this code would be O(n^2) or quadratic. There is a for loop that runs through every number of n. And for every number of n there is a while loop running. With a loop running for every number of n, the runtime while increase quadratically for larger inputs.


c) The runtime of this function is linear time. The body of the function itself is constant time, just checking if the value passed in is 0 or not. The recursive portion in the return statement will do the same thing for every number of n, decremnting by 1 until it reaches 0.

## Exercise II

There are a number of ways we could do this. The easiest would be like a linear search algorithm. We could start from the bottom or the top floor and drop an egg and see if it breaks or not. And then go one floor at a time until that result changes. This, of course, would not minimize the number of eggs dropped or broken. Starting from the bottom would be the better solution because the number of broken eggs would only be 1 but the number of eggs dropped would still not be minimized.

I think a binary search solution would be best. We should first drop an egg from the middle floor. If it breaks, we would go down to the floor halfway between the bottom and the middle floor and do the same thing. If the egg didn't break we would go to the floor halfway between the top and middle floor and drop an egg from there. We would repeat these steps until we found the correct value for f.

The linear search would have a linear time complexity but the binary search would have a logarithmic time complexity making it better, it would also minimize the number of dropped and broken eggs most of the time over the linear search.
