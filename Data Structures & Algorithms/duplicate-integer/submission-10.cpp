class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for(int num: nums){
            auto it = seen.find(num);
            if(!seen.insert(num).second){
                return true;
            }
        }
        return false;
    }
};