# Rate Limiter

## Problem Statements
## Functional Requirements
> Accuracy
> Low Latency
> Distributed and Fault tolerant
> Exception Handling

## The Benefit of this control for our system

## Key takeaways

## Design Pattern we learned
> Token bucket
> Leaking bucket
> Fixed Window Counter
> Sliding Window Log
>  Sliding Window Counter

## How this could be tested?

## How to prevent DDoS?

## Challenges
> Storage
* counters need to be in memory (Redis). DB Access is too slow
  
> Handling Rejection


> Scaling
* race condition
* Synchronization issue
* Monitoring and optimization