#include <stdio.h>
#include <stdlib.h>

void flip_bits(unsigned int a)
{
    printf("%u\n", ~a);
}

int main(void)
{
    unsigned int a, n;
    int i;

    scanf("%d", &n);
    for (i = 0; i < n; i++) {
        scanf("%d", &a);
        flip_bits(a);
    }

}
