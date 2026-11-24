class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> s_freq(26);
        vector<int> t_freq(26);
        for(int i = 0, n = s.size(); i < n; i++){
            s_freq[s[i] - 'a']++;
        }
        for(int i = 0, n = t.size(); i < n; i++){
            t_freq[t[i] - 'a']++;
        }
        return s_freq == t_freq;
    }
};
