class Solution {
public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) {
        // long long int cnt = 0;
        // int fmin = 0;
        // int fmax = 0;
        // vector<int> mp(nums.size(), 0);
        // vector<int> mmin(nums.size(), 0);
        // vector<int> mmax(nums.size(), 0);
        // int ind = nums.size();
        // for (int i = (nums.size() - 1); i >= 0; i--) {
        //     if (nums[i] > maxK || nums[i] < minK) {
        //         mp[i] = i;
        //         ind = i;
        //     } else {
        //         mp[i] = ind;
        //     }
        // }
        // ind = nums.size();
        // for (int i = (nums.size() - 1); i >= 0; i--) {
        //     if (nums[i] == minK) {
        //         mmin[i] = i;
        //         ind = i;
        //     } else {
        //         mmin[i] = ind;
        //     }
        // }
        // ind = nums.size();
        // for (int i = (nums.size() - 1); i >= 0; i--) {
        //     if (nums[i] == maxK) {
        //         mmax[i] = i;
        //         ind = i;
        //     } else {
        //         mmax[i] = ind;
        //     }
        // }
        // for (int i = 0; i < nums.size(); i++) {
        //     if (nums[i] > maxK || nums[i] < minK)
        //         continue;
        //     int closeMaxi = mmax[i];
        //     int closeMini = mmin[i];
        //     if (closeMaxi == nums.size() || closeMini == nums.size())
        //         break;   
        //     int closeOut = mp[i];
        //     if (closeOut > min(closeMini, closeMaxi) &&
        //         closeOut < max(closeMini, closeMaxi))
        //         continue;
        //     int maxim = max(closeMaxi, closeMini);
        //     cnt += (closeOut - maxim);
        // }
        // return cnt;
        int n = nums.size();
        long long ans = 0;
        
        int lastMin = -1, lastMax = -1, lastInvalid = -1;
        
        for (int i = 0; i < n; i++) {
            if (nums[i] < minK || nums[i] > maxK) {
                lastInvalid = i;
            }
            if (nums[i] == minK) {
                lastMin = i;
            }
            if (nums[i] == maxK) {
                lastMax = i;
            }
            
            int validStart = min(lastMin, lastMax);
            if (validStart > lastInvalid) {
                ans += (validStart - lastInvalid);
            }
        }
        return ans;
    }
};