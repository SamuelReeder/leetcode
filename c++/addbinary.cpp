class Solution {
public:
    string addBinary(string a, string b) {
        
        int n = max(a.length(), b.length());

        string tmp = "";
        tmp.append(n - min(a.length(), b.length()), '0');

        if (a.length() != n) {
            a = tmp + a; 
        } else {
            b = tmp + b;
        }

        string res = "";
        bool remainder = false;
        for (int i = n - 1; i >= 0; i--) {
            char ac = a[i], bc = b[i];

            if (remainder && ac == '1' && bc == '1') {
                res.append("1");
                remainder = true;
            }  else if (ac == '1' && bc == '1') {
                res.append("0");
                remainder = true;
            } else if (remainder && (ac == '1' || bc == '1')) {
                res.append("0");
            } else if (ac == '1' || bc == '1') {
                res.append("1");
            } else if (remainder) {
                res.append("1");
                remainder = false;
            } else {
                res.append("0");
            }
        }

        if (remainder)
            res.append("1");

        reverse(res.begin(), res.end());

        return res;

    }
};
