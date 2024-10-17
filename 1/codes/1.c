#include <stdio.h>

// Function to calculate the ratio in which the X-axis divides the line segment
void find_ratio(float *x1, float *y1, float *x2, float *y2, float *k) {
    // Compute the ratio using the formula: k = -y1 / (y2 - y1)
    *k = -*y1 / *y2;  // Correctly update the value at the address of k
}

int main() {
    // Coordinates of the points A(1, -3) and B(4, 5)
    float x1 = 1, y1 = -3;
    float x2 = 4, y2 = 5;

    float k;

    // Call the function to calculate the ratio
    find_ratio(&x1, &y1, &x2, &y2, &k);

    // Print the calculated ratio
    printf("The ratio in which the X-axis divides the line segment is: %.2f\n", k);

    return 0;
}
