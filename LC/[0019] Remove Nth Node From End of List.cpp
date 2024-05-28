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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int ii=0;
        ListNode * fast=head;
        ListNode * slow=head;
        while(ii<n && fast != nullptr){
            fast=fast->next;
            ++ii;
        }

        ListNode * prev = nullptr;
        while(fast != nullptr){
            fast=fast->next;
            prev=slow;
            slow=slow->next;
        }
        
        if(prev != nullptr){
            prev->next=slow->next;
        }else{
            head=head->next;
        }
        return head;
    }
};