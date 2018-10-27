#include <stdio.h>
#include <stdlib.h>
#define hdjaksdad


/* Wilson's algortihm creates a uniform spanning tree
using a loop-erased random walk
*/

typedef struct node {
	/* Two dimensional grid */

	struct node *north;
	struct node *east;
	struct node *south;
	struct node *west;
	char status;
} bond;


int main(void){
	bond *examplenode;
	bond *examplenode2;
	examplenode->north = malloc(sizeof(bond));
	examplenode->north=examplenode2;

	printf("%p\n", examplenode->north);

	// we pick a root //


	return 0;
}



