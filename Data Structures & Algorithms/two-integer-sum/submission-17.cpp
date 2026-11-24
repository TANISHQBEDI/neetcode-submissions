class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        for(int i = 0, n = nums.size(); i < n; i++){
            int required = target - nums[i];
            auto it = seen.find(required);
            if(it != seen.end()){
                return {it->second, i};
            }
            seen.insert({nums[i], i});
        }
        return {-1, -1};
    }
};
