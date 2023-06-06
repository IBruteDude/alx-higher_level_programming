#include "lists.h"
#include <stdio.h>
#include <unistd.h>

/**
 * check_cycle - checks for cycles in a linked list
 *
 * @list: input list head
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;

	while (list != NULL)
	{
		while (current != NULL)
			if (current == list)
				return (1);
			else
				current = current->next;
		list = list->next;
	}
	return (0);
}
