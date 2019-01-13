#include"GRAPH.h"

static void randE(GRAPH &G, int E)
{
	for (int i = 0; i < E; i++)
	{
		int v = int(G.V()*rand() / (1.0 + RAND_MAX));
		int w = int(G.V()*rand() / (1.0 + RAND_MAX));
		G.insert(Edge(v, w));
	}
}