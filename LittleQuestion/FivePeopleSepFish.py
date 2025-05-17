"""
One night, five people — A, B, C, D, and E — went fishing together.
After a long and tiring day, they fell asleep.

The next morning, A woke up first.
He divided the fish into five parts, found one extra fish, threw it away, and took one part for himself.

Then B woke up.
He also divided the remaining fish into five parts, found one extra fish, threw it away,
and took one part for himself.

C, D, and E each woke up one after another and did the same:
divided the remaining fish into five parts, discarded one extra fish if there was any, and took one part.

What is the minimum number of fish they could have caught originally?
"""

fish = 6
while True:
    total = fish
    enough = True
    for _ in range(5):
        if (total - 1) % 5 == 0:
            total = (total - 1) // 5 * 4
        else:
            enough = False
            break
    if enough:
        break
    else:
        fish += 5
print(fish)

"""
fish = 6
for _ in range(4):
    fish = fish * 5 + 1
print(fish)

At first, I tried to calculate the problem using this method
but I realized that it was already incorrect from the first round
For example, if the initial value is 6 , then after going through the reverse calculate once,
you get 31

Assume the fourth person received 31 fish. He would throw away one, leaving 30
divide them into five parts(6 each),take one part for himself, and leave 24.
But according to the reverse method, we are going to back 6 fish, which doesn't make sense

The correct reverse calculate should be : 6/4*5, since 6 is what remained after take away 1/5 of the fish
But obviously,this doesn't result in integer, meaning the fifth person didn't receive exactly 6 fish.
So this approach is incorrect
"""