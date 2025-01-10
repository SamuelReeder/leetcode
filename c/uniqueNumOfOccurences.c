bool uniqueOccurrences(int* arr, int arrSize) {
    int newArr[4001] = { 0 };
    int nums[arrSize + 1];
    memset(nums, 0, (arrSize + 1) * sizeof(int));

    for (int i = 0; i < arrSize; i++) {
        newArr[arr[i] + 1000] += 1;
        nums[newArr[arr[i] + 1000]] += 1;
        nums[newArr[arr[i] + 1000] - 1] -= 1;
    }

    for (int i = 1; i < arrSize + 1; i++) {
        if (nums[i] > 1) {
            return false;
        } 
    }
    return true;
}
