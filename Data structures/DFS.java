import java.util.*;
class DFS {
int[] visited;
int[] sequence;
int count = 0;
static int size = 0;
static int components = 0;

public static void main(String args[]) {
	int[][] graph;
	Scanner scanner = new Scanner(System.in);
	System.out.println("Enter the size of matrix");
	scanner.close();
	size = scanner.nextInt();
	graph = new int[size][size];
	for(int i = 0; i < size; i++)
		for(int j = 0; j < size; j++)	
			graph[i][j] = scanner.nextInt();
	DFS dfs_search = new DFS();
	dfs_search.dfs(graph);
	dfs_search.display();
}

public void dfs(int[][] graph) {
visited = new int[size];
sequence = new int[size];
for(int i = 0; i < size; i++){
	for(int j = 0; j < size; j++)
	if(graph[i][j] != 0)
	if(visited[j] != 1){
		visited[j] = 1;
		sequence[count++] = j;
		components++;
		dfs_visit(graph, j);
}
}
}

public void dfs_visit(int[][] graph, int i) {
	for(int j = 0; j < size; j++){
		if(graph[i][j] != 0)
		if(visited[j] != 1){
			visited[j] = 1;
			sequence[count++] = j;
			dfs_visit(graph, j);
}
}
}

public void display() {
	System.out.println(components);
}
}
