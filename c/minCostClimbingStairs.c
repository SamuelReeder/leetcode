int min(int a, int b) {
    if (a < b) {
        return a;
    }
    return b;
}

int minCostClimbingStairs(int* cost, int costSize) {
    if (costSize == 2) {
        return min(cost[0], cost[1]);
    }

    int *dp = (int*)malloc(costSize * sizeof(int));

    dp[costSize - 1] = cost[costSize - 1];
    dp[costSize - 2] = cost[costSize - 2];
    for (int i = costSize - 3; i >= 0; i--) {
        dp[i] = cost[i] + min(dp[i + 1], dp[i + 2]);
    }

    int ans = min(dp[0], dp[1]);
    free(dp);

    return ans;
}
