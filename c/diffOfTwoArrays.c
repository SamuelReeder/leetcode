
int** findDifference(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize, int** returnColumnSizes) {
    int hashset1[2001] = {0};
    int hashset2[2001] = {0};
    int *diff1 = (int*)malloc(nums1Size * sizeof(int));

    int d = 0;
    for  (int i = 0; i < nums1Size; i++) {
        if (hashset1[nums1[i] + 1000] == 0){
            hashset1[nums1[i] + 1000] = 1;
            diff1[d] = nums1[i];
            d++;
        }
       
    }

    int *diff2 = (int*)malloc(nums2Size * sizeof(int));

    int j = 0;
    for  (int i = 0; i < nums2Size; i++) {
        if (hashset1[nums2[i] + 1000] == 0 && hashset2[nums2[i] + 1000] == 0) {
            hashset2[nums2[i] + 1000] = 1;
            diff2[j] = nums2[i];
            j++;
        } else {
            hashset1[nums2[i] + 1000] = -1;
        }
    }

    int *difffinal = (int*)malloc(nums1Size * sizeof(int));

    int x = 0;
    for (int i = 0; i < d; i++) {
        if (hashset1[diff1[i] + 1000] == 1) {
            difffinal[x] = diff1[i];
            x++;
        }
    }


    difffinal = (int*)realloc(difffinal, x * sizeof(int));
    diff2 = (int*)realloc(diff2, j * sizeof(int));

    int** result = (int**)malloc(sizeof(int*) * 2);

    result[0] = difffinal;
    result[1] = diff2;

    *returnSize = 2;

    *returnColumnSizes = (int*)malloc(2 * sizeof(int));
    (*returnColumnSizes)[0] = x; // Number of elements in difffinal
    (*returnColumnSizes)[1] = j;

    free(diff1);

    return result;
    

}

