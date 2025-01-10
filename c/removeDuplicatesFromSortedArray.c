int removeDuplicates(int* nums, int numsSize) {
    
    int current;

    int count = 0;
    for (int i = 0; i < numsSize; i++) {
        if (current != nums[i]) {
            current = nums[i];
            nums[i - count] = nums[i];
        } else {
            count++;
        }
    }

    return numsSize - count;
}

