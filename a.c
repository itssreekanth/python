#include <stdio.h>
int main() {
  int a,sum;
  printf("Enter a value: ");
  scanf("%d",&a);
  sum=(a++ + a++);
  printf("Sum of two integers is:%d \n",sum);
}
