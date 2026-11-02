class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        array<int, 2001> freq = {0};
        for(int& num: nums){
            freq[num + 1000]++;
        }
        vector<pair<int, int>> pairs;
        for(int i = 0; i < 2001; i++){
            pair<int, int> item= {freq[i], i - 1000};
            pairs.push_back(item);
        }
        sort(pairs.rbegin(), pairs.rend());
        vector<int> res;
        for(int i = 0; i < k; i++){
            res.push_back(pairs[i].second);
        }
        return res;
    }
};
