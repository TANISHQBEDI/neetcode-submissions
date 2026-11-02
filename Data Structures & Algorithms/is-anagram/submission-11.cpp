class Solution {
public:
    bool isAnagram(string s, string t) {
        array<int, 26> s_counter = {0};
        array<int, 26> t_counter = {0};
        for(char ch: s){
            s_counter[ch - 'a']++;
        }
        for(char ch: t){
            t_counter[ch - 'a']++;
        }
        for(int i = 0; i < 26; i++){
            if(s_counter[i] != t_counter[i]){
                return false;
            }
        }
        return true;
    }
};
