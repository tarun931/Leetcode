class Solution {
public:
   vector<int> assignEdgeWeights(vector<vector<int>>& edges, vector<vector<int>>& queries) {
    int n=edges.size()+1,m=17,mod=1e9+7;
    vector<vector<int>> sol(n+1);
    for(auto& x:edges){
        sol[x[0]].push_back(x[1]);
        sol[x[1]].push_back(x[0]);
    }
    vector<int> d(n+1,0);
    vector<vector<int>> up(n+1,vector<int>(m));
    function<void(int,int)> dfs=[&](int u,int p){
        d[u]=d[p]+1;
        up[u][0]=p;
        for(int i=1;i<m;i++)up[u][i]=up[up[u][i-1]][i-1];
        for(int v:sol[u])if(v!=p)dfs(v,u);
    };
    dfs(1,0);
    auto getlca=[&](int a,int b){
        if(d[a]<d[b])swap(a,b);
        for(int i=m-1;i>=0;i--)if(d[up[a][i]]>=d[b])a=up[a][i];
        if(a==b)return a;
        for(int i=m-1;i>=0;i--)if(up[a][i]!=up[b][i])a=up[a][i],b=up[b][i];
        return up[a][0];
    };
    vector<int> res;
    for(auto& q:queries){
        int u=q[0],v=q[1];
        if(u==v){res.push_back(0);continue;}
        int z=getlca(u,v),len=d[u]+d[v]-2*d[z];
        long long x=1;
        for(int i=0;i<len-1;i++)x=(x*2)%mod;
        res.push_back(x);
    }
    return res;
}
};