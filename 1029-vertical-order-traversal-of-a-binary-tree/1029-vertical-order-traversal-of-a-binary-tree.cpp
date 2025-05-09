/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        vector<vector<int>> ans ;
        vector<int> sol;
        queue<pair<int,pair<int,TreeNode*>>> q;   //lvl , vert , node
        map<int,map<int,multiset<int>>> mp ; //vert , lvl ,node->val
        q.push({0,{0,root}});
        while(!q.empty())
        {
            auto front = q.front();
            q.pop();
            TreeNode* temp = front.second.second;
            int lvl = front.first;
            int vert = front.second.first ;
            mp[vert][lvl].insert(temp->val);
            if(temp->left)
                q.push({lvl+1,{vert-1,temp->left}});
            if(temp->right)
                q.push({lvl+1,{vert+1,temp->right}});        
        }
        for(auto p:mp)
        {
            vector<int>sol;
          for(auto q: p.second)
          {
             sol.insert(sol.end(),q.second.begin(),q.second.end());
          }
            ans.push_back(sol);
        }
        return ans;
    }
};

