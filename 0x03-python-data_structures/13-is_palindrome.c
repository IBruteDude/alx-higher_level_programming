#include "lists.h"

int is_palindrome(listint_t **head)
{
	size_t i, len = 0;
	int *node_arr;
	listint_t *node;

	if (head == NULL || *head == NULL)
		return (1);

	node = *head;
	while (node != NULL)
		len++, node = node->next;
	node_arr = (int *)malloc((len + 1) * sizeof(int));
	node = *head;
	for (i = 0; i < len; i++)
		node_arr[i] = node->n, node = node->next;
	for (i = 0; i < (size_t) len / 2; i++)
		if (node_arr[i] != node_arr[len - i - 1])
			return (0);
	return (1);
}