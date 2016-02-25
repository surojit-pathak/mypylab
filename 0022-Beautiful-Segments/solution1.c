#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print_number_of_beautiful_segments(int *arr,
                                        int **memo, int l, int r, int x)
{
    int i, j, count, prod;
 
    count = 0;
    for (i = r; i >= l; i--) {
        for (j = i; j <= r; j++) {
            if (memo[i][j] == -1) {
                memo[i][j] = prod = memo[i][j-1] & arr[j];
            } else {
                prod = memo[i][j];
            }
            if (prod <= x) {
                count++;
            }
        }
    }
    printf("%d\n", count);
}

int main(void)
{
    int q, n, i;
    int l, r, x;
    int **memo;
    int *arr;

    scanf("%d %d", &n, &q);
    memo = (int **)malloc(sizeof(int *) * n);
    arr = (int *)malloc(sizeof(int) * n);
    for (i=0; i < n; i++) {
        memo[i] = (int *)malloc(sizeof(int) * n);
        memset(memo[i], -1, sizeof(int) * n);
    }

    for (i=0; i < n; i++) {
        scanf("%d", &arr[i]);
        memo[i][i] = arr[i];
    }

    for (i=0; i < q; i++) {
        scanf("%d %d %d", &l, &r, &x);
        print_number_of_beautiful_segments(arr, memo, l - 1, r - 1, x);
    }
 
    return 0;
    
}
