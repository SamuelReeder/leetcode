int min(int a, int b) {
    if (a < b) return a;
    return b;
}

int max(int a, int b) {
    if (a > b) return a;
    return b;
}


int maxProfit(int* prices, int pricesSize) {

    int minimum = prices[0];

    int max_profit = 0;


    for (int i = 1; i < pricesSize; i++) {
        max_profit = max(max_profit, prices[i] - minimum);
        minimum = min(prices[i], minimum);
    }

    return max_profit;
}
