class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;
        for(string& str: strs){
            vector<int> freq(26);
            for(char ch: str){
                ++freq[ch - 'a'];
            }
            string copy = str;
            sort(copy.begin(), copy.end());
            groups[copy].push_back(str);
        }
        vector<vector<string>> res;
        for(auto group: groups){
            res.push_back(group.second);
        }
        return res;
    }
};