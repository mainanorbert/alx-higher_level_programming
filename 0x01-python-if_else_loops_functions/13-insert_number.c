#include "lists.h"

/**
 * insert_node - inserts number to list
 * @head: pointer to pointer of first node of linked list
 * @number: number to be inserted
 * Return: returns address of new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (head == NULL || current->n >= number)
	{
		new->next = current;
		*head = new;
		return (new);
	}
	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}
	new->next = current->next;
	current->next = new;
	return (new);
}
