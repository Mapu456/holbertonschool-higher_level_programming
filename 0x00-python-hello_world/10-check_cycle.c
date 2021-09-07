#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - checks a cycle
 * @list: linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *before = list;
	listint_t *after = list;

	while (after != NULL && after->next != NULL)
	{
		before = before->next;
		after = after->next->next;

		if (before == after)
		{
			return (1);
		}
	}
	return (0);
}
