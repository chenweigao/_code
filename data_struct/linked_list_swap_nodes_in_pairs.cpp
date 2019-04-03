/*
We define the function to implement as swap(head), where the input parameter head refers to the head of a linked list. The function should return the head of the new linked list that has any adjacent nodes swapped.

Following the guidelines we lay out above, we can implement the function as follows:

1. First, we swap the first two nodes in the list, i.e. head and head.next;
2. Then, we call the function self as swap(head.next.next) to swap the rest of the list following the first two nodes.
3. Finally, we attach the returned head of the sub-list in step (2) with the two nodes swapped in step (1) to form a new linked list.
*/
#include <iostream>

using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution
{
  public:
    ListNode *swapPairs(ListNode *head)
    {
        if ((head == nullptr) || (head->next == nullptr))
            return head;
        ListNode *n = head->next;
        head->next = swapPairs(n->next);
        n->next = head;
        return n;
    }
}