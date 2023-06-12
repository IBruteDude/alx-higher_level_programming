#include "lists.h"

int is_palindrome(listint_t **head)
{
	size_t i, len = 0;
	listint_t *node_arr, *node;

	if (head == NULL || *head == NULL)
		return (1);

	node = *head;
	while (node != NULL)
		len++, node = node->next;
	node_arr = (listint_t *)malloc((len + 1) * sizeof(listint_t));
	node = *head;
	for (i = 0; i < len; i++)
		node_arr[i] = *node, node = node->next;
	for (i = 0; i < (size_t) len / 2; i++)
		if (node_arr[i].n != node_arr[len - i - 1].n)
			return (0);
	return (1);
}