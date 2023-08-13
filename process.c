#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_BUFF_SIZE 256

int main() {
    FILE* fp;
    char buffer[MAX_BUFF_SIZE];

    // Execute the "ps" command to get the list of running processes
    fp = popen("ps -e", "r");
    if (fp == NULL) {
        perror("Error executing command");
        exit(EXIT_FAILURE);
    }

    // Read the output of the "ps" command line by line and print the process details
    printf("%-8s %-8s %s\n", "PID", "PPID", "COMMAND");
    while (fgets(buffer, MAX_BUFF_SIZE, fp) != NULL) {
        // Skip the first line (header)
        if (strstr(buffer, "PID") != NULL)
            continue;

        int pid, ppid;
        char command[MAX_BUFF_SIZE];

        // Parse the PID, PPID, and COMMAND from the output
        sscanf(buffer, "%d %d %[^\n]", &pid, &ppid, command);

        // Print the process details
        printf("%-8d %-8d %s\n", pid, ppid, command);
    }

    // Close the file pointer
    pclose(fp);

    return 0;
}
