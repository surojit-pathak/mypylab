#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

bool test_palindrome (char *str, int i, int j)
{
    if (i > j) return false;
    while (i < j) {
        if (str[i] == str[j]) {
            i++; j--;
        } else return false;
    }
    return true;
}

void find_longest_palindromic_substring (char *s)
{
    int max_len = 1;
    int max_s = 0, max_e = 0;
    int n = strlen(s);
    int i, j;

    for(i=0; i < n; i++) {
       for(j=n-1; j > i; j--) {
           if (j - i + 1 > max_len) {
               if (test_palindrome(s, i, j)) {
                   max_len = j - i + 1;
                   max_s = i;
                   max_e = j;
                   break;
               }
            } else {
               break;
            }
        }
    }

    for (i=max_s; i <= max_e; i++) putchar(s[i]);
    printf("\n");
}

int main (void) 
{
   char str[1000000];
   scanf("%s", str);
   find_longest_palindromic_substring(str);
}
