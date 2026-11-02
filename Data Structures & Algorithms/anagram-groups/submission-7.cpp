class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;
        map<string, vector<string>> collector;
        for(string str: strs){
            string key = str;
            sort(key.begin(), key.end());
            auto it = collector.find(key);
            collector[key].push_back(str);
        }
        for(auto& group: collector){
            res.push_back(group.second);
        }
        return res;
    }
};
