#include <stdio.h>
#include <math.h>
#include "matfun.h"
#include "geofun.h"

int main() {
    // Coordinates of points A(1, -3) and B(4, 5)
    double **A = createMat(2, 1);
    double **B = createMat(2, 1);

    A[0][0] = 1;   // X-coordinate of point A
    A[1][0] = -3;  // Y-coordinate of point A

    B[0][0] = 4;   // X-coordinate of point B
    B[1][0] = 5;   // Y-coordinate of point B

    // Calculate the ratio using the section formula
    // X-axis divides the line at Y = 0, find the ratio k
    double k = -A[1][0] / (B[1][0]);

    printf("The ratio in which the X-axis divides the line segment is: %.2f\n", k);

    // Calculate the point where the line intersects the X-axis
    double **P = Matsec(A, B, 2, k);

    printf("The point of intersection with the X-axis is: (%.2f, %.2f)\n", P[0][0], P[1][0]);

    // Free memory allocated for matrices
    freeMat(A, 2);
    freeMat(B, 2);
    freeMat(P, 2);

    return 0;
}
