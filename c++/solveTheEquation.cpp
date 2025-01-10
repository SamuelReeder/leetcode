class Solution {
public:
    string solveEquation(string equation) {
        string current = "0";

        int pointer = 0;
        int nums[] = {0, 0, 0, 0};
        int multiplier = 1;

        for (int i = 0; i < equation.length(); i++) {

            if (std::isdigit(equation[i])) {
                current += equation[i];
                continue;
            }

            int add = 0;
            if (equation[i] == 'x') {
                if (current == "0") {
                    current = "1";
                }
                
                add = 1;
            }

            nums[pointer + add] += multiplier * std::stoi(current);
            current = "0";

            if (equation[i] == '+') {
                multiplier = 1;
            } else if (equation[i] == '-') {
                multiplier = -1;
            } else if (equation[i] == '=') {
                multiplier = 1;
                pointer = 2;
            }
        }

        nums[pointer] += multiplier * std::stoi(current);

        int constant = nums[0] - nums[2];
        int coefficient = nums[3] - nums[1];

        if (coefficient == 0 && constant == 0) {
            return "Infinite solutions";
        } else if (coefficient == 0) {
            return "No solution";
        }
        return "x=" + std::to_string(constant / coefficient);
    }
}
