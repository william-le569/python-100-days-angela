#include <stdio.h>
#include <string.h>

// Define function pointer type
typedef float (*operation_func)(float, float);

// Define actual operations
float add(float a, float b) {
    return a + b;
}
float subtract(float a, float b) {
    return a - b;
}
float multiply(float a, float b) {
    return a * b;
}
float divide(float a, float b) {
    return b != 0 ? a / b : 0; // basic safety
}

// Struct to map symbol to function
typedef struct {
    char symbol[2]; // e.g., "+"
    operation_func func;
} operation_entry;

// Function to find the operation
operation_func get_operation(char* op, operation_entry* ops, int size) {
    for (int i = 0; i < size; i++) {
        if (strcmp(ops[i].symbol, op) == 0) {
            return ops[i].func;
        }
    }
    return NULL; // not found
}

int main() {
    operation_entry operations[] = {
        {"+", add},
        {"-", subtract},
        {"*", multiply},
        {"/", divide}
    };
    int num_ops = sizeof(operations) / sizeof(operations[0]);

    float a, b;
    char op[2];

    printf("Enter first number: ");
    scanf("%f", &a);
    printf("Enter operation (+, -, *, /): ");
    scanf("%s", op);
    printf("Enter second number: ");
    scanf("%f", &b);

    operation_func selected = get_operation(op, operations, num_ops);
    if (selected) {
        float result = selected(a, b);
        printf("%.2f %s %.2f = %.2f\n", a, op, b, result);
    } else {
        printf("Invalid operation.\n");
    }

    return 0;
}