> Notice the size of restriction is way less than size of the N

> Considering only +1 restriction

```
-> h[i] <= h[i-1]+p[i]-p[i-1]
```

> Considering limit from left

```
-> h[i]=min(limit[i], h[i-1]+p[i]-p[i-1])
```

> Considering limit from right

```
-> h[i]
```

> How to find the peak btn two restrictions

```
-> h[i-1]+x = h[i] + y
-> p[i-1]+x = p[i] - y
```
