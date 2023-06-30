#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"

/**
 * infinite_while - returns nothing
 * Return: nothin
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - the  zombie processes
 * Return: always success
 */
int main(void)
{
	int x = 0;
	pid_t pid;

	while (x < 5)
	{
		pid = fork();
		if (!pid)
			break;
		printf("Zombie process created, PID: %i\n", (int)pid);
		x++;
	}
	if (pid != 0)
	{
		infinite_while();
	}
	return (0);
}

