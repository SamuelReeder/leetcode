int majorityElement(int* nums, int numsSize) {
    
    int candidate;
    int count = 0;

    for (int i = 0; i < numsSize; i++) {
        if (count == 0) {
            candidate = nums[i];
            count++;
        } else if (candidate == nums[i]) {
            count++;
        } else {
            count--;
        }
    }

    return candidate;
}
