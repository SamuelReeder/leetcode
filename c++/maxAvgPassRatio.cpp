class Solution {
public:

    double calculate_delta(double pass, double total) {
        if (pass == total) {
            return 0.0;
        }
        return (total - pass) / (total * (total + 1.0));
    }

    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        // greedy approach
        // we need priority queue of increase in pass ratio by adding another student

        priority_queue<tuple<double, double, double>> pq;

        for (const auto& cl : classes) {
            double pass = (double)cl[0];
            double total = (double)cl[1];
            double delta = calculate_delta(pass, total);
            
            pq.push({delta, pass, total});
        }

        for (int i = 0; i < extraStudents; ++i) {
            auto [current_delta, pass, total] = pq.top();
            pq.pop();

            double new_pass = pass + 1.0;
            double new_total = total + 1.0;

            pq.push({ calculate_delta(new_pass, new_total), new_pass, new_total});
        }

        double total_ratio_sum = 0.0;
        while (!pq.empty()) {
            auto [delta, pass, total] = pq.top();
            pq.pop();
            
            total_ratio_sum += (pass / total);
        }

        return total_ratio_sum / (double)classes.size();
    }
};
