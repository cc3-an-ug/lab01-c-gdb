#include <stdio.h>

// Cambiar estos 4 valores
#define V0 0
#define V1 -1
#define V2 0
#define V3 0

// No editar a partir de aquí

#ifndef TEST
int main(void) {
  int a;
  char *s;

  /**
    Esto es un print statement. Noten la 'f' al final!
    Puede ser útil investigar cómo funciona printf para futuras
    necesidades de debugging...
  */
  printf("Galileo eccentrics:\n====================\n");

  /* Ciclo for */
  for (a=0; a<V0; a++) {
    printf("UG ");
  }
  printf("\n");

  /* Switch */
  switch (V1) {
    case 0:   printf("Andres\n");
    case 1:   printf("Darth Vader\n");     break;
    case 2:   printf("Walter White\n");
    case 3:   printf("Andres\n");           break;
    case 4:   printf("Ragnar\n");      break;
    case 5:   printf("Obama\n");
    default:  printf("No conozco a estas personas!\n");
  }

  /* Operador ternario, se parece a Java no ? */
  s = (V3==3) ? "Vamos" : "No";

  /* If */
  if (V2) {
    printf("\n%s clase CC3AN!\n", s);
  } else  {
    printf("\n%s funciona!\n", s);
  }

  return 0;
}
#endif
