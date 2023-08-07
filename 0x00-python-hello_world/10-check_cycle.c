#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - checks if list has a cycle
 * @list: pointer to singly linked list
 * Return: 0 if no cycle and 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slw = list;
	listint_t *fst = list->next;

	if (list == NULL || list->next == NULL)
		return (0);
	while (slw != NULL && fst->next != NULL)
	{
		if (slw == fst)
			return (1);
		slw = slw->next;
		fst = fst->next->next;
	}
	return (0);
}
