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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ans;
        map<int,int> mp;
        queue<TreeNode*> q ;
        q.push(root);
        int lvl = 0;
        q.push(NULL);
        while(!q.empty() && q.front()!=NULL)
        {
          TreeNode* front = q.front();
          q.pop();
          if(front->left)
             q.push(front->left);
          if(front->right)
             q.push(front->right);
          mp[lvl] = front->val;
          if(q.front()==NULL)
          {
             lvl++;
             q.pop();
             q.push(NULL);
          }     
        } 
        for(auto it : mp)
        {
            ans.push_back(it.second);
        }
        return ans;
    }
};