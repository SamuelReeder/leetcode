void moveZeroes(int* nums, int numsSize) {
    
    int* arr = (int*)malloc(numsSize * sizeof(int));

    int end = numsSize - 1;
    int start = 0;

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == 0) {
            arr[end] = 0;
            end--;
        } else {
            arr[start] = nums[i];
            start++;
        }
    }

    for (int i = 0; i < numsSize; i++) {
        nums[i] = arr[i];
    }
}
