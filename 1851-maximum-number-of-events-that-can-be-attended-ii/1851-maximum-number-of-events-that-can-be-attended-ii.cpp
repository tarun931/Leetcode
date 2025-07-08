class Solution {
public:
    int maxValue(vector<vector<int>>& events, int k) {
        sort(events.begin(), events.end());
        int n = events.size();
        vector<int> next(n);
        for (int i = 0; i < n; ++i) {
            int l = i + 1, r = n;
            while (l < r) {
                int m = l + (r - l) / 2;
                if (events[m][0] > events[i][1]) r = m;
                else l = m + 1;
            }
            next[i] = l;
        }

        vector<int> prev(n + 1);
        for (int j = 1; j <= k; ++j) {
            vector<int> curr(n + 1);
            for (int i = n - 1; i >= 0; --i) {
                curr[i] = max(curr[i + 1], events[i][2] + (next[i] < n ? prev[next[i]] : 0));
            }
            prev = curr;
        }

        return prev[0];
    }
};