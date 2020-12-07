#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *ahead;

	ahead = list;
	while (ahead != NULL)
	{
		list = list->next;
		ahead = ahead->next;
		ahead = ahead->next;
		if (list == ahead)
			return (1);
	}
	return (0);
}
