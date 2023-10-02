#include "lists.h"
/**
 * check_cycle : verifie si une liste liée contient un cycle
 * @list: notre list
 * Return: boolean
 */
int check_cycle(listint_t *list)
{
	listint_t rappide = list;
	listint_t lent = list;

	if (!list)
		return (0);
	while (lent && rappide && rappide->next)
	{
		lent = lent->next;
		rappide = rappide->next->next;
		if (lent == rappide)
			return (1);
	}
	return (0);
}
