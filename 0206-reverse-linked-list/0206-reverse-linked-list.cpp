/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(!head || !head->next)
            return head;
        ListNode *dummy = NULL;    
        dummy = reverseList(head->next);
        head->next->next = head;
        head->next= NULL;
        return dummy;
    }
};



// class Solution {
// public:
//     ListNode* helper(ListNode* cur)
//     {   ListNode* dummy=NULL;
//        if(cur==NULL || cur->next==NULL)
//            return cur;
//         ListNode* forw= cur->next;
//         while(cur->next){
//            cur->next=dummy;
//            dummy=cur;
//             cur=forw;
//             forw=forw->next;
//        }     
//        cur->next=dummy;
//      return cur;
//     }
//     ListNode* reverseList(ListNode* head) {
//         ListNode* cur=head;
//         return helper(cur);
//     }
// };