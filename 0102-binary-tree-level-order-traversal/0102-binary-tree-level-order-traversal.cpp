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
    vector<vector<int>> levelOrder(TreeNode* root) {
      queue<TreeNode*> q;
        vector<vector<int>> ans;
        vector<int> sol;
        q.push(root);
        q.push(NULL);
        while(!q.empty() && q.front()!=NULL )
        {
            TreeNode* front= q.front();
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
                ans.push_back(sol);
                sol.clear();
                
            }    
            
        }  
        return ans;

    }
};