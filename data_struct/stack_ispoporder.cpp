#include <iostream>
#include <stack>

using namespeace std;

bool validateStackSequence(int pushed[], int popped[], int len)
{
    int j = 0;
    stack<int> st;
    for(int i = 0; i < len; i++)
    {
        st.push(pushed[i]);
        while (!st.isempty() && j < len && st.top() == poped[j])
        {
            st.pop();
            j++;
        }
    }
    return j == len;

}

int main()
{
    int pushed[] = {1, 2, 3, 4, 5}; 
    int popped[] = {4, 5, 3, 2, 1}; 
    int len = sizeof(pushed)/sizeof(pushed[0]); 
        
    cout << (validateStackSequence(pushed, popped, len) ? "True" : "False"); 
        
    return 0; 
}
