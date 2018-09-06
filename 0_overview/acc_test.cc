#include <cstdio>

// This C++ code performs the same task as the Python acc_test.py code, to
// emphasize that the precision is hardware-dependent, and not tied to any
// particular language.

int main() {

    // Let h be a double-precision floating point number. Change "double" to
    // "float" to carry out the test for a single-precision floating point
    // number.
    double h=1;

    // Loop until h becomes less than 1e-20
    while(h>1e-20) {

        // Check if 1+h==1 in floating point arithmetic
        if(1+h==1) printf("%g  1+h=1\n",h);
        else printf("%g  1+h!=1\n",h);

        h*=0.1;
    }
}
