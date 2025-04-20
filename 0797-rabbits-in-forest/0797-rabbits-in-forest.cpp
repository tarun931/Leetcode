class Solution {
public:
    int numRabbits(vector<int>& answers) {
        unordered_map<int,int> mp ;
        for(int i=0;i< answers.size();i++)
        {
            mp[answers[i]] += 1;
        }
        int cnt = 0 ;
        for(auto it : mp)
        {
            cnt += ceil((double)it.second / (it.first+1)) * (it.first+1) ; 
        }
        return cnt;
    }
};

/*
    logic : ceil((double)it.second / (it.first+1)) * (it.first+1)

    Divide the number of rabbits that gave answer x (i.e., it.second) by x + 1 — this gives us how many full groups we can form.

But since we can't leave a group partially formed (e.g., if 5 rabbits say 2, but 3 rabbits fit in a group, we need 2 groups), we take the ceiling.

Then, multiply by x + 1 to get the total rabbits accounted for (some might be theoretical rabbits not present in the array but implied by the answer).

*/