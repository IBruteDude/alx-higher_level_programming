#include "lists.h"

/**
 * insert_node - inserts a created node into its position in a sorted list
 *
 * @head: the address of the head of the list
 * @number: the number to insert into the list
 * Return: the address of the created node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *next;

	if (head == NULL)
		return (NULL);
	node = *head;
	if (node == NULL || number <= node->n)
	{
		*head = (listint_t *) malloc(sizeof(listint_t));
		(*head)->n = number, (*head)->next = node;
		return (*head);
	}
	while (node != NULL)
	{
		if (number > node->n && (!node->next || number <= node->next->n))
		{
			next = node->next;
			node->next = (listint_t *)malloc(sizeof(listint_t));
			node = node->next;
			node->n = number;
			node->next = next;
			return (node);
		}
		node = node->next;
	}
	return (NULL);
}
