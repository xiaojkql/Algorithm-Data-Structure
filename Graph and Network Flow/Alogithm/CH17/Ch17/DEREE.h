template <class Graph> class DEGREE
{
	const Graph &G;
	vector <int> degree;
public:
	DEGREE(const Graph &G) : G(G), degree(G.V(), 0)
	{
		for (int v = 0; v < G.V(); v++)
		{
			typename Graph::adjIterator A(G, v);
			for (int w = A.beg(); !A.end(); w = A.nxt())
				degree[v]++;
		}
	}
	int operator[](int v) const
	{
		return degree[v];
	}
};