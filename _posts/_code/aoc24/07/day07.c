#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MUL 0
#define ADD 1
#define CAT 2

#define PART 2

#define OPSSIZE 16

int* get_ops(int n, unsigned int b, int *ops, size_t s) {
    // make sure res is large enough to hold result
    if (pow(b, s) < n)
        return NULL;
    int *p = ops;
    while (n >= 0) {
        *p = n % b;
        n = n / b;
        if (n == 0)
            break;
        p++;
    }
    return ops;
}

int main() {
    unsigned long ans = 0;
    FILE *file = fopen("./input.txt", "r");
    if (file == NULL) return EXIT_FAILURE;

    char line[256] = {0};
    while (fgets(line, sizeof(line), file) != NULL) {
        char *endptr;
        long target = strtol(line, &endptr, 10);
        int nums[32] = {0};
        int num_sz = 0;
        char *p;
        while (*endptr != '\n') {
            p = endptr + 1;
            nums[num_sz++] = (int) strtol(p, &endptr, 10);
        };

        int total = PART == 1 ? pow(2, num_sz - 1) : pow(3, num_sz - 1);
        for (int n = 0; n < total; n++) {
            long outcome = (long)nums[0];
            int ops[OPSSIZE] = {0};
            if (PART == 1) {
                get_ops(n, 2, ops, OPSSIZE);
            }
            else if (PART == 2) {
                get_ops(n, 3, ops, OPSSIZE);
            }
            else {
                fclose(file);
                puts("ERROR: PART must be 1 or 2.");
            }
            for (int i = 1; i < num_sz; i++) {
                int op = ops[i-1];
                if (op == MUL)
                    outcome = outcome * nums[i];
                else if (op == ADD) {
                    outcome = outcome + nums[i];
                }
                else if (op == CAT) {
                    char cat[64];  // plenty big for input
                    sprintf(cat, "%ld%d", outcome, nums[i]);
                    outcome = strtol(cat, NULL, 10);
                }
            }
            if (outcome == target) {
                ans += target;
                break;
            }
        }
    }
    printf("%ld\n", ans);
    fclose(file);
    return 0;
}