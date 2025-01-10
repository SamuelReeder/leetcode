int maxProfit(int* prices, int pricesSize) {

    int profit = 0;
    int total = 0;
    // when there is higher value, hold right before
    // when there is lower value, sell right before

    for (int i = 1; i < pricesSize; i++) {
        if (prices[i] >= prices[i-1]) {
            profit += prices[i] - prices[i-1];
        } else {
            total += profit;
            profit = 0;
        }

    }

    return total + profit;
}
