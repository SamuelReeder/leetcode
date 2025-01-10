void reverse(int* nums, int start, int end) {
    while (start < end) {
        int temp = nums[start];
        nums[start] = nums[end];
        nums[end] = temp;
        start++;
        end--;
    }
}

void rotate(int* nums, int numsSize, int k) {

    if (numsSize <= 1) {
        return;
    }

    k = k % numsSize;
    
    // reverse whole array
    reverse(nums, 0, numsSize - 1);

    // part that wouldve been moved to front
    reverse(nums, 0, k - 1);

    reverse(nums, k, numsSize - 1);
}
