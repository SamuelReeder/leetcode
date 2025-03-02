class Solution {
public:
    vector<int> topStudents(vector<string>& positive_feedback, vector<string>& negative_feedback, vector<string>& report, vector<int>& student_id, int k) {
        
        unordered_map<string, int> feedback;
        for (string s : positive_feedback) {
            feedback[s] = 3;
        }

        for (string s : negative_feedback) {
            feedback[s] = -1;
        }

        unordered_map<int, int> m;
        for (int i = 0; i < report.size(); i++) {

            m[student_id[i]] = 0;
            
            stringstream ss(report[i]); // Convert string to stream
            string word;

            while (ss >> word) {  // Extract words separated by spaces
                if (feedback.find(word) != feedback.end()) {
                    m[student_id[i]] += feedback[word];
                }
            }
        }

        vector<int> k_students;
        while (k_students.size() < k) {
            int maximum = -10000;
            int max_index;
            for (auto &pair : m) {
                if (pair.second > maximum) {
                    maximum = pair.second;
                    max_index = pair.first;
                } else if (pair.second == maximum && pair.first < max_index) {
                    maximum = pair.second;
                    max_index = pair.first;
                }
            }
            k_students.push_back(max_index);
            m[max_index] = -10000;
        }

        return k_students;
    }
};
