obool canJump(int* nums, int numsSize) {

    // if end is reachable, every index is reachable

    if (numsSize == 1) return true;

    int curr = numsSize - 1;
    for (int i = numsSize - 2; i >= 0; i--) {
        if (nums[i] >= curr - i) {
            curr = i;
        }
    }

    return curr == 0;

}
