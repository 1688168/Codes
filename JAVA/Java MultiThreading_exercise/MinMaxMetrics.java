public class MinMaxMetrics {
 
    private volatile long minValue;
    private volatile long maxValue;
 
    /**
     * Initializes all member variables
     */
    public MinMaxMetrics() {
        this.maxValue = Long.MIN_VALUE;
        this.minValue = Long.MAX_VALUE;
    }
 
    /**
     * Adds a new sample to our metrics.
     */
    public void addSample(long newSample) {//the input is long, so both min and max need to be long
        synchronized (this) {//need to update both min/max atomically. so synchronized
            this.minValue = Math.min(newSample, this.minValue);
            this.maxValue = Math.max(newSample, this.maxValue);
        }
    }
 
    /**
     * Returns the smallest sample we've seen so far.
     */
    public long getMin() {
        return this.minValue;
    }
 
    /**
     * Returns the biggest sample we've seen so far.
     */
    public long getMax() {
        return this.maxValue;
    }
}
