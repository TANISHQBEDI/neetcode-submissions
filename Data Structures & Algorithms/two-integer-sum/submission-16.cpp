class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> seen;
        for(int i = 0; i < nums.size(); i++){
            int required = target - nums[i];
            auto it = seen.find(required);
            if(it != seen.end()){
                return {it->second, i};
            }
            else{
                seen.insert({{nums[i], i}});
            }
        }
    }
};
