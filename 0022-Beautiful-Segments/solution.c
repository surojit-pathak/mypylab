#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <assert.h>

typedef struct memo {
    int * memo;
    int   n;
    int   n_real;
} memo_t;

memo_t *memo_init(int n) 
{
    static memo_t *g_memo;
    bool new = true;
    memo_t *m;

    if (g_memo) {
        if (g_memo->n_real > n) {
            g_memo->n = n;
            memset(g_memo->memo, -1, sizeof(int) * n);
            new = false;
        } else {
            free(g_memo->memo);
            free(g_memo);
            g_memo = NULL;
        }
    }

    if (new) {
	m = (memo_t *)malloc(sizeof(memo_t));
	m->n = n;
        m->n_real = n;
	m->memo = (int *)malloc(sizeof(int) * n);
	memset(m->memo, -1, sizeof(int) * n);
        g_memo = m;
    }

    return g_memo;
}
inline void memo_put (memo_t *m, int i, int j, int data)
{
    if (i <= j) {
        int idx = i > 0 ? (((i - 1) * (2 * m->n -1)) / 2) : 0 + j;
        m->memo[idx] = data;
    } else assert(0);
}
inline int memo_get (memo_t *m, int i, int j)
{
    if (i <= j) {
        int idx = i > 0 ? (((i - 1) * (2 * m->n -1)) / 2) : 0 + j;
        return m->memo[idx];
    } else assert(0);
}
void print_number_of_beautiful_segments_sparse(int *arr,
                                               int l, int r, int x)
{
    int i, j, count, prod;
    int n = (r - l) + 1;
    memo_t *m = memo_init(n);

    for (i = l; i <= r; i++) {
        memo_put(m, i - l, i - l, arr[i]);
    }
  
    count = 0;
    for (i = r; i >= l; i--) {
        for (j = i; j <= r; j++) {
            if (memo_get(m, i-l, j-l) == -1) {
                prod = memo_get(m, i-l, j-l-1) & arr[j];
                memo_put(m, i-l, j-l, prod); 
            } else {
                prod = memo_get(m, i-l, j-l);
            }
            if (prod <= x) {
                count++;
            }
        }
    }
    printf("l:%10d, r:%10d, x:%5d, c:%10d\n", l, r, x, count);
    fflush(stdout);
}

int main(int argc, char *argv[])
{
    int q, n, i;
    int l, r, x;
    int *arr;

    FILE * fd = fopen(argc > 1 ? argv[1] : "./input03.txt", "r");

    fscanf(fd, "%d %d", &n, &q);
    arr = (int *)malloc(sizeof(int) * n);

    for (i=0; i < n; i++) {
        fscanf(fd, "%d", &arr[i]);
    }

    for (i=0; i < q; i++) {
        fscanf(fd, "%d %d %d", &l, &r, &x);
        print_number_of_beautiful_segments_sparse(arr, l - 1, r - 1, x);
    }
 
    return 0;
    
}
