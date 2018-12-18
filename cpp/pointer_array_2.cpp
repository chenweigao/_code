#include <stdio.h>

int main() {
    int evens[5] = {0, 2, 4, 6, 8};
    printf("%i\n", *evens);
    // The first even numbers

    int *positive_evens = &evens[1];
    printf("%i\n", positive_evens[0]);
    // The first positive even numbers
}