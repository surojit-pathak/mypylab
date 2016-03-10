#include <stdio.h>
#include <stdlib.h>

//#define INT unsigned char
#define INT unsigned int
int main(void)
{
   INT n, t, r;
   scanf("%u", &n);
   t = n; r = 0;
   while (t) {
       INT m = t % 10;
       t = t / 10;
       r = r * 10 + m;
       printf("%d -> %d\n", t, r);
   }

   printf("%d -> %d\n", n, r);

   return 0;
}


