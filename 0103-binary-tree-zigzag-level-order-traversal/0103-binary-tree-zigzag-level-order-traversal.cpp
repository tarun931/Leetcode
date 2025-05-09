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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
       vector<vector<int>> ans ;
       if(root == NULL)
           return ans ;
       queue<TreeNode*> q ;
       q.push(root);
       q.push(NULL);
       vector<int> sol;
       bool flag = false;
       while(!q.empty() && q.front()!= NULL)
       {
        TreeNode* front = q.front();
        q.pop();
        if(front->left)
           q.push(front->left);
        if(front->right)
           q.push(front->right);
        sol.push_back(front->val);
        if(q.front()==NULL)
        {
          q.pop();
          q.push(NULL);
          if(flag)
          { 
              reverse(sol.begin(),sol.end());
              ans.push_back(sol);
          }
          else
              ans.push_back(sol);
          flag = !flag;    
          sol.clear();
        }
       }  
       return ans;  
    }
};