# LeetCode 857 — How to discover the solution in an interview

## Step 1 of 5 — Start with one team

If I have no idea how to choose the workers, I’ll make the problem smaller: **suppose someone already picked the `k` workers. How do I find the cheapest way to pay them?**

Pay must be proportional to quality, so everyone on the team gets the same pay per unit of quality. Call it `rate`.

For each worker:

    quality[i] × rate >= wage[i]

Divide by `quality[i]`:

    rate >= wage[i] / quality[i]

The cheapest rate that satisfies everyone is the **largest `wage / quality` ratio on the team**. That gives me a formula for any team:

    team cost = max(wage / quality on the team) × sum(quality on the team)

I could try every team of size `k` now. That’s too expensive, but the formula tells me what to look at next.

## Step 2 of 5 — Guess which worker sets the rate

The first factor, `max(wage / quality)`, must come from one of the workers I hire. There are only `n` possible rate-setters.

So I can ask a smaller question for each worker: **If I hire this worker at their minimum rate, who should fill the other `k - 1` spots?**

A teammate is eligible if their own minimum rate is at most the current worker’s rate.

## Step 3 of 5 — Once the rate is fixed, minimize total quality

At a fixed rate, every extra unit of quality costs the same amount. So I want the **`k - 1` smallest qualities** among eligible teammates.

For example, suppose the current worker sets the rate at `$8` and I need one teammate. Two eligible workers have qualities `10` and `20`. At `$8` per unit, they cost `$80` and `$160`, respectively. I choose the worker with quality `10`.

This is why I look at **quality** when choosing teammates. Their `wage / quality` ratio tells me whether they’re eligible. Their quality tells me how much they’ll cost at the rate I’ve already chosen.

## Step 4 of 5 — Sort for eligibility, use a heap for selection

If I sort by `wage / quality` in ascending order, everyone I’ve already seen is eligible at the current rate. As I move forward, the eligible pool only grows.

I need the smallest `k - 1` qualities from that pool. When I have too many candidates, I want to remove the **largest** quality, so I use a **max-heap**. A running sum lets me compute the cost without summing the heap each time.

In my C++ loop, I add the current worker’s quality to the sum, trim the heap to `k - 1` earlier workers, and calculate the cost if I have enough workers. Then I push the current worker onto the heap so they can be a teammate in future rounds.

## Step 5 of 5 — Check why the best team gets considered

Imagine the optimal team. Find its **last worker in the sorted list**. When I reach that worker, every other member of the optimal team has already appeared, and the current rate equals the optimal team’s shared rate.

My heap picks the `k - 1` smallest eligible qualities, so the teammates I choose cost at most as much as the optimal team’s teammates at that same rate. That’s why taking the minimum across all rounds finds the answer.

**Interview takeaway:** Start by pricing one team. The worker with the highest required rate sets the price per unit. Try each worker as the rate-setter, sort to see who’s eligible, and use a max-heap to keep the cheapest teammates at that rate.

**Complexity:** `O(n log n)` time for sorting plus `O(n log(k + 1))` for the heap operations. The heap uses `O(k)` space, and the worker list uses `O(n)` space.