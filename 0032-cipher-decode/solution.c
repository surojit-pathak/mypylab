#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

void cipher_decode(char *output, int n, int k)
{
    char *input, prod;
    int  i, j;

    input = (char *)malloc(n + 1);
    input[0] = output[0];
    for (i=1; i < k; i++) {
        input[i] = output[i] ^ output[i-1];
    }
    for (i=k; i < n; i++) {
        prod = input[i - k + 1];
        for (j = i - k + 2; j < i; j ++) {
            prod = prod ^ input[j];
        }
        input[i] = output[i] ^ prod;
    }
    for(i=0; i < n; i++) printf("%u", input[i]);
    printf("\n");
}

int main (void) 
{
   int i, n, k;
   char *output;

   scanf("%d %d", &n, &k);
   output = (char *)malloc(n + k + 1);
   scanf("%s", output);
   for(i=0; i <n; i++) {
       output[i] = output[i] - '0';
   }
   cipher_decode(output, n, k);
}
