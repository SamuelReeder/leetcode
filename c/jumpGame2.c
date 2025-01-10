int min(int a, int b) {
    if (a < b) return a;
    return b;
}

int jump(int* nums, int numsSize) {


    // d[i] = minimum jumps to reach i
    // if d[]
    
    if (numsSize == 1) return 0;

    int d[numsSize];
    d[numsSize - 1] = 0;

    for (int i = 0; i < numsSize - 1; i++) {
        d[i] = 10000;
    }


    int curr = numsSize - 1;
    for (int i = numsSize - 2; i >= 0; i--) {
        if (nums[i] >= numsSize - 1 - i) {
            d[i] = 1;
        } else {
            for (int j = i + 1; j < min(nums[i] + i + 1, numsSize); j++) {
                d[i] = min(d[i], d[j] + 1);
            }
        }
    }

    return d[0];
}
