Note that a pair of tasks (a,b),(c,d) (done in reverse order)
requires total energy
max(d, b+c).

So, this pair is in minimum energy order iff max(b,a+d) > max(d, b+c).
As written, there are a few ways this can happen:
- d > b + c implies:
    - b > d > b + c (which is impossible, since c > 0), or
    - a + d > d > b + c (which is trivial, since a > 0)
- b + c > d implies:
    - b > b + c > d (which is impossible, since c > 0), or
    - a + d > b + c > d

So really, (a,b),(c,d) is in sorted order iff a + d > b + c,
which can be rearranged to a - b > c - d, or b - a < c - d.


Swapping any pair to satisfy this will minimize the overall
energy required*, so we can just put all the pairs in sorted
order based on this.


*This is because swapping into order decreases the energy required for a pair, so it can't
possibly increase the total energy required. Suppose Alice has the tasks in some non-sorted order,
and that she has exactly enough energy to complete the tasks in that order.
Give Bob the same tasks, but swap some pair of the tasks so that they are now in sorted order.
Also, give Bob the same amount of energy as Alice.
1. Alice and Bob complete all tasks up to, and not including, the swapped pair. They still have the same amount of energy
2. Alice and Bob complete the swapped pair. The amount of energy Bob has remaining is no less than what Alice has. Let's call Bob's remaining energy B, and Alice's A. We can say B>=A.
3. Alice and Bob complete all subsequent tasks. This uses up E energy for both.

Bob is left with B-E energy, and Alice is left with A-E=0.
So, we know that making the swap could not have caused the total required energy to increase.


Any out-of-order sequence can be eventually
converted to the fully sorted sequence via these swaps, which cannot increase total energy
required. So, any out-of-order sequence must require at least as much energy as the perfectly
sorted sequence. Which means that the minimum energy required is achieved by the fully sorted
sequence.


So, our algorithm can simply sort the tasks, and then compute the total energy required to do
them all in reverse sorted order.