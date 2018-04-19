#include<stdio.h>
#include<stdlib.h>

typedef struct node {
    int val;
    struct node * next;
} node_t;

// percolation //
typedef struct vertex  {
	struct edge * north;
	struct edge * south;
	struct edge * east;
	struct edge * west;
} vertex_t;

typedef struct edge {
	int val; //edge open or closed w.p. p
	struct vertex * v1;
	struct vertex * v2;	
} edge_t;

void main(){
	node_t * head = NULL;
	head = malloc(sizeof(node_t));

	head->val = 1;
	head->next = malloc(sizeof(node_t));

	node_t * current = head;

	int count = 0, idx = 0;
	while(count < 100){
		current->next = malloc(sizeof(node_t));
		current->val = idx;
		idx++;

		printf("%d\n", current->val);

                current = current->next;
		count++;
	}

}



