#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print_number_of_beautiful_segments_sparse(int *arr,
                                               int l, int r, int x)
{
    int **memo;
    int i, j, count, prod;
    int n = (r - l) + 1;
    memo = (int **)malloc(sizeof(int *) * n);
    for (i=0; i < n; i++) {
        memo[i] = (int *)malloc(sizeof(int) * n);
        memset(memo[i], -1, sizeof(int) * n);
    }

    for (i = l; i <= r; i++) {
        memo[i - l][i - l] = arr[i];
    }
  
    count = 0;
    for (i = r; i >= l; i--) {
        for (j = i; j <= r; j++) {
            if (memo[i-l][j-l] == -1) {
                memo[i-l][j-l] = prod = memo[i-l][j-l-1] & arr[j];
            } else {
                prod = memo[i-l][j-l];
            }
            if (prod <= x) {
                count++;
            }
        }
    }
    printf("%d\n", count);
    for (i=0; i < n; i++) {
        free(memo[i]);
    }
    free(memo);
    
}

int main(void)
{
    int q, n, i;
    int l, r, x;
    int *arr;

    scanf("%d %d", &n, &q);
    arr = (int *)malloc(sizeof(int) * n);

    for (i=0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    for (i=0; i < q; i++) {
        scanf("%d %d %d", &l, &r, &x);
        print_number_of_beautiful_segments_sparse(arr, l - 1, r - 1, x);
    }
 
    return 0;
    
}
