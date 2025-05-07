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
    TreeNode* searchBST(TreeNode* root, int val) {
       if(val == root->val)
          return root;
       TreeNode* lefty = NULL; 
       TreeNode* righty = NULL ;
        if (root->left)
             lefty = searchBST(root->left,val);
        if(lefty)
             return lefty;     
        if(root->right)
             righty= searchBST(root->right,val) ;
        if(righty)
             return righty;
       return NULL;           
                 
    }
};