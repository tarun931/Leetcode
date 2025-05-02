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
    int height(TreeNode* root , int& h)
    {
        if(root==NULL)
           return 0;
        int lefty = 0, righty=0;
        lefty = height(root->left,h);
        righty = height(root->right,h);
        h = max(h,lefty+righty);
        return 1+max(lefty,righty);   
    }
    int diameterOfBinaryTree(TreeNode* root) {
        int maxi = 0;
        height(root,maxi);
        return maxi;
    }
};