void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    
    int arr[m + 1];
    for (int i = 0; i < m; i++) {
        arr[i] = nums1[i];
    }

    int i = 0;
    int j = 0;

    int count = 0;
    while (i < m && j < n) {
        if (arr[i] <= nums2[j]) {
            nums1[count] = arr[i];
            i++;
        } else {
            nums1[count] = nums2[j];
            j++;
        }
        count++;
    }

    if (i < m) {
        while (i < m) {
            nums1[count] = arr[i];
            i++;
            count++;
        }
    } else if (j < n) {
        while (j < n) {
            nums1[count] = nums2[j];
            j++;
            count++;
        }
    }
}
