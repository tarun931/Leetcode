class Solution {
public:
    unordered_map<int, vector<pair<int, int>>> g;
int maxLen, maxTime;
unordered_map<long, int> dp;
int helper(int node, int len, int time) {
    if(time >= maxTime) return INT_MIN;
    if(len == maxLen) return time;
    
    int result = INT_MIN;
    long long key = (long)node << 48 | (long)len << 32 | time;
    if(dp.count(key)) return dp[key];
    
    for(auto& nxt : g[node]) {
        result = max(result, helper(nxt.first, len + 1, time + nxt.second));
    }
    return dp[key] = result;
}
int maxWeight(int n, vector<vector<int>>& edges, int k, int t) {
    maxLen = k;
    maxTime = t;
    for(auto& e : edges) {
        g[e[0]].push_back({ e[1], e[2] });
    }
    int mini = INT_MIN;
    for(int i = 0; i < n; i++) {
        mini = max(mini, helper(i, 0, 0));
    }
    return mini == INT_MIN ? -1 : mini;
}
    
};