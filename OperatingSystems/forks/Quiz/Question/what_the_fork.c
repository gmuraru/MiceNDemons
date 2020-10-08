#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

char *msg = "^⨀ ᴥ ⨀ ^";

/* SCENARIO:
 * The PARENT Process prints a message and then forks
 * * the parent prints a new message after the fork
 * * the child prints a message
 * 
 * Q: What is the final output of the program
 */
int main(void)
{
    pid_t pid;
    printf("%s", msg);

    if ((pid = fork()) > 0) {
	printf("This is the PARENT!");
        wait(NULL);
    } else {
        printf("CHILD Finish");
    }

    return 0;
}
