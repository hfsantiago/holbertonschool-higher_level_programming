#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - Checks whether a linked list have a cycle or not.
 * @list: Given linked list to check.
 *
 * Return: returns 0 if there is not cycle, otherwise 1.
 */

int check_cycle(listint_t *list)
{
	listint_t *bryan, *toretto;

	toretto = bryan = list;

	for ( ; toretto && bryan && toretto->next ; )
	{
		toretto = toretto->next->next;
		bryan = bryan->next;

		if (bryan == toretto)
			return (1);
	}

	return (0);
}
