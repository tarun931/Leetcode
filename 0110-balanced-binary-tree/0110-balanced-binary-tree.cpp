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
    int height(TreeNode* root)
    {
         if(root==NULL)
            return 0;   
         int lefty = height(root->left);
         if(lefty == -1)
            return -1;
         int righty = height(root->right);
         if(righty == -1)
            return -1;
         if(abs(lefty-righty)>1)
             return -1;   
         return 1+max(lefty,righty) ;      
    }
    bool isBalanced(TreeNode* root) {
        return (height(root) != -1);           
    }
};