int removeDuplicates(int* nums, int numsSize) {
    int current;
    int currentCount;

    int count = 0;
    for (int i = 0; i < numsSize; i++) {
        if (current != nums[i]) {
            currentCount = 1;
            current = nums[i];
            nums[i - count] = nums[i];
        } else {
            if (currentCount > 1) {
                count++;
            } else {
                nums[i - count] = nums[i];
            }
            currentCount++;
            
        }
    }

    return numsSize - count;
}
