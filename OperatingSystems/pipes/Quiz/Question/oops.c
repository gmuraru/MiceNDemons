#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

#define BUFFSIZE 29

char *msg1 = "(╯°□°)╯︵ ┻━┻";

/* SCENARIO:
 * The PARENT Process writes a message to one end of the pipe
 * and the CHILD Process reads from the other end of the pipe
 * 
 * Q: Why is the child process hanging?
 */
int main(void)
{
    char buff[BUFFSIZE] = {0};
    int p[2], pid, nr_read_bytes;

    if (pipe(p) < 0) {
        fprintf(stderr, "This pipe is broken! Abort the mission!");
        exit(1);
    }

    if ((pid = fork()) > 0) {
        if (write(p[1], msg1, BUFFSIZE) != BUFFSIZE) {
            /* This is emberassing... */
            fprintf(stderr, "[PARENT] Could not send the message!");
            exit(2);
        }

        /* Waiting for the sweet child of mine */
        wait(NULL);
    } else {
    
        close(p[1]);
        while ((nr_read_bytes = read(p[0], buff, BUFFSIZE)) > 0) {
            printf("[CHILD] %s\n", buff);
        }

        if (nr_read_bytes != 0) {
            /* Something went hayware */
            exit(2);
        }

        printf("Finished reading\n");
    }

    return 0;
}