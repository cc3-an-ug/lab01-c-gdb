#include <stdio.h>
#include "eccentric.c"


#define FAILED "V%d has an invalid value '%d'\n"
#define PASSED "V%d OK\n"


void test(int num, int success, int v) {
  if (success)
    printf(PASSED, num);
  else
    printf(FAILED, num, v);
}


int main(void) {
  test(0, V0 == (89 ^ 0x5A), V0);
  test(1, V1 == (25 ^ 0x1A), V1);
  test(2, V2 == (71 ^ 0x44), V2);
  test(3, V3 == (107 ^ 0x68), V3);

  return 0;
}
