public class prim {
    public static void main(String[] args) {
        String[] vertices = {"1","2","3","4","5","6","7","8"};
        
        int[][] edges = {
            {0,1,1},{0,3,10},{0,5,12}, // Vertex 1
            {1,0,1},{1,2,8},{1,3,4},{1,4,7}, // Vertex 2
            {2,1,8},{2,4,2},{2,7,5}, // Vertex 3
            {3,0,10},{3,1,4},{3,4,5},{3,5,8},{3,6,11}, // Vertex 4
            {4,1,7},{4,2,2},{4,3,5},{4,6,3},{4,7,9}, // Vertex 5
            {5,0,12},{5,3,8},{5,6,5},{5,7,6}, // Vertex 6
            {6,3,11},{6,4,3},{6,5,5},{6,7,4}, // Vertex 7
            {7,2,5},{7,4,9},{7,5,6},{7,6,4} // Vertex 8
        };

        WeightedGraph<String> graph1 = new WeightedGraph<>(vertices,edges);

        WeightedGraph<String>.MST tree1 = graph1.getMinimumSpanningTree(0);

        tree1.printTree();
    }
    
}