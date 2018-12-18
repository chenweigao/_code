#include <assert.h>

int main(){
    int abc[] = {0, 1, 2};
    int *copy = abc;
    
    copy[0] = 3;
    assert(abc[0] == 3);
}