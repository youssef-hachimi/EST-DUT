#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <sys/stat.h>

double getTime() {
    struct timeval t;
    gettimeofday(&t, NULL);
    return (double) t.tv_sec + (double) t.tv_usec/1e6;
}

void wait(int howlong) {
    double t = getTime();
    while ((getTime() - t) < (double) howlong)
      ; //wait...
}

int main(int argc, char *argv[])
{
    char *str = argv[1]; //string we passed

    while (1) {
    printf("%s\n", str);
    wait(5);
    }
    return 0;
}
