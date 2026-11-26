class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n = nums.size();
        unordered_map<int, int> freq;
        vector<vector<int>> buckets(n + 1, vector<int>());
        vector<int> res;

        for(int num: nums){
            freq[num]++;
        }
        for(auto it: freq){
            buckets[it.second].push_back(it.first);
        }
        for(int i = n; i >= 0; i--){
            for(int num: buckets[i]){
                cout << num << endl;
                res.push_back(num);
                if(res.size() == k){
                    return res;
                }
            }
        }
    }
};
