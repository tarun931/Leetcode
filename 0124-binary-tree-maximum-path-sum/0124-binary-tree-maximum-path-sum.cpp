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
    int maxi(TreeNode* root, int& sum)
    {
        if(root == NULL)
           return 0;
        int lefty = max(0,maxi(root->left,sum));
        int righty = max(0,maxi(root->right,sum));
        sum = max(sum,lefty+righty+root->val);
        return root->val + max(lefty,righty);   
    }
    int maxPathSum(TreeNode* root) {
        int sum = INT_MIN;
        maxi(root,sum);
        return sum ;
    }
};