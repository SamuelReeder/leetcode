type CacheEntry = {
    value: number;
    timerId: ReturnType<typeof setTimeout>;
};

class TimeLimitedCache {
    private cache: Map<number, CacheEntry>;

    constructor() {
        this.cache = new Map();
    }
    
    set(key: number, value: number, duration: number): boolean {
        const existingEntry = this.cache.get(key);
        const hasUnexpired = existingEntry !== undefined;

        if (hasUnexpired) {
            clearTimeout(existingEntry.timerId);
        }

        const timerId = setTimeout(() => {
            this.cache.delete(key);
        }, duration);

        this.cache.set(key, { value, timerId });
        return hasUnexpired;
    }
    
    get(key: number): number {
        const entry = this.cache.get(key);
        return entry ? entry.value : -1;
    }
    
    count(): number {
        return this.cache.size;
    }
}

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */
