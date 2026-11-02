class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        array<int, 2001> freq = {0};
        for(int& num: nums){
            freq[num + 1000]++;
        }
        vector<vector<int>> bucket(nums.size() + 1);
        for(int i = 0; i < 2001; i++){
            if(freq[i]){
                bucket[freq[i]].push_back(i - 1000);
            }
        }
        
        vector<int> res;
        for(int i = bucket.size() - 1; i >= 0; i--){
            for(int j = bucket[i].size() - 1; j >= 0; j--){
                if(res.size() < k){
                    res.push_back(bucket[i][j]);
                }
            }
        }
        return res;
    }
};
