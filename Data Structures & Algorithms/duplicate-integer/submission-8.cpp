class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> seen;
        for(int& num: nums){
            auto it = seen.find(num);
            if(it != seen.end()){
                return true;
            }
            seen.insert(num);
        }
        return false;
    }
};