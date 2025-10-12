class Solution {
public:
    pair<int, int> parseDate(string date) {
        return {stoi(date.substr(0, 2)), stoi(date.substr(3))};
    }

    pair<int, int> findOp(string one, string two, std::function<int(int, int)> operation) {

        auto oneMap = parseDate(one), twoMap = parseDate(two);

        int maxMonth = operation(oneMap.first, twoMap.first);

        if (maxMonth == oneMap.first && maxMonth == twoMap.first) {
            return {maxMonth, operation(oneMap.second, twoMap.second)};
        } else if (maxMonth == oneMap.first) {
            return oneMap;
        } else {
            return twoMap;
        }
    }   



    int countDaysTogether(string arriveAlice, string leaveAlice, string arriveBob, string leaveBob) {
        
        vector<int> dates = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        // const auto aliceStart = parseDate(arriveAlice), aliceEnd = parseDate(leaveAlice);
        // const auto bobStart = parseDate(arriveBob), bobEnd = parseDate(leaveBob);

        // find number of days 
        // days = min(bobEnd, aliceEnd) - max(bobStart, aliceStart)
        // if days < 0 then return 0


        auto maxDate = findOp(arriveAlice, arriveBob, [&](int a, int b) {
            return max(a, b);
        });

        auto minDate = findOp(leaveAlice, leaveBob, [&](int a, int b) {
            return min(a, b);
        });

        if (maxDate.first > minDate.first)
            return 0; 
            
        if (maxDate.first == minDate.first) {
            int tmp = minDate.second - maxDate.second + 1;
            return tmp > 0 ? tmp : 0;
        }

        int tally = minDate.second + (dates[maxDate.first - 1] - maxDate.second + 1);

        for (int i = maxDate.first + 1; i < minDate.first; i++) {
            tally += dates[i - 1];
        }

        return tally > 0 ? tally : 0;
    }
};
