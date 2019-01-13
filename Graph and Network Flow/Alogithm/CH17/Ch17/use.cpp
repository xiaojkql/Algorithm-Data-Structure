#include<iostream>
#include <stdlib.h>
#include "GRAPH.h"
#include "IO.h"
#include "CC.h"

main(int argc, char *argv[])
{
	int V = atoi(argv[1]);
	GRAPH G(V,false);
	IO<GRAPH>::scan(G);
	if (V < 20) IO<GRAPH>::show(G);
	std::cout << G.E() << " edges ";
	CC<GRAPH> Gcc(G);
	std::cout << Gcc.count() << " components" << std::endl;
}