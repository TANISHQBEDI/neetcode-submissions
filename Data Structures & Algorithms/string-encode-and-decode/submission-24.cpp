class Solution {
public:

/**
I/P = ["hello", "world"]
encoded = 5#hello5#world
*/

    string encode(vector<string>& strs) {
        string res;
        for(string str: strs){
            res += (to_string(str.size()) + "#" + str);
        }
        return res;
    }

    vector<string> decode(string s) {
        vector<string> res;
        for(int i = 0, n = s.size(); i < n; i++){
            // len of word in string
            string ws = "";
            // len of word in int
            int wsn = 0;
            // variable to track start of each word
            int l = i;

            while(s[i] != '#' && i < n){
                ws.push_back(s[i]);
                i++;
            }
            // initialize l to the next char after '#' just after the length of the number
            l = i + 1;
            // convert the recorded length to integer
            wsn = stoi(ws);
            // store the word in result
            res.push_back(s.substr(l, wsn));
            // increment i by the length of the word
            i += wsn;
        }
        return res;
    }
};
