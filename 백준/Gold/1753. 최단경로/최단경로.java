import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Node implements Comparable<Node>{
	int endNode;
	int weight;
	
	public Node(int endNode, int weight) {
		this.endNode = endNode;
		this.weight = weight;
	}

	@Override
	public int compareTo(Node o) {
		return Integer.compare(this.weight, o.weight);
	}
}

public class Main{
	static int V,E;
	static int MAX_VALUE = 123456789;
	static ArrayList<Node> linkList[];
	static int weights[];
	static PriorityQueue<Node> linkStartIdx;
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		V = Integer.parseInt(st.nextToken());	//정점의 개수
		E = Integer.parseInt(st.nextToken());	//간선의 개수
		int startIdx = Integer.parseInt(br.readLine());	//시작 정점
		weights = new int[V+1];		//시작 정점의 다른 무게를 초기화
		linkList = new ArrayList[V+1];	//간선의 정보를 저장
		initWeights(startIdx);		//시작 정점에서 다른 정점간의 거리를 저장하는 배열
		linkStartIdx = new PriorityQueue<>();
		//간선 정보를 초기화
		for(int i=0; i<E; i++) {
			st = new StringTokenizer(br.readLine());
			int startNode = Integer.parseInt(st.nextToken());
			int endNode = Integer.parseInt(st.nextToken());
			int weight = Integer.parseInt(st.nextToken());
			Node node = new Node(endNode,weight);
			linkList[startNode].add(node);
			if(startNode == startIdx) linkStartIdx.offer(node);	//시작 노드에 대해서만 update
		}
		
		findShortestPath(startIdx);
		
		printWeight(sb);
		System.out.println(sb);
	}
	
	private static void initWeights(int startIdx) {
		for(int i=1; i<=V; i++) {
			linkList[i] = new ArrayList<>();
			if(i == startIdx) continue;
			weights[i] = MAX_VALUE;
		}
	}
	private static void findShortestPath(int startIdx) {
		boolean visited[] = new boolean[V+1];
		while(!linkStartIdx.isEmpty()){
			Node node = linkStartIdx.poll();
			if(!visited[node.endNode]) {
				visited[node.endNode] = true;
				weights[node.endNode] = node.weight;
				updateRoute(node.endNode, node.weight, visited);
			}
		}
	}
	
	private static void updateRoute(int idx, int preWeight, boolean[] visited) {
		if(linkList[idx] == null) return;
		for(Node node : linkList[idx]) {
			if(!visited[node.endNode]) {
				if(weights[node.endNode] > preWeight+node.weight) {
					weights[node.endNode] = preWeight + node.weight;
					node.weight = preWeight + node.weight;
					linkStartIdx.offer(node);
				}
			}
		}
	}
	private static void printWeight(StringBuilder sb) {
		for(int i=1; i<=V; i++) {
			if(weights[i] == MAX_VALUE) sb.append("INF\n");
			else sb.append(weights[i]).append("\n");
		}
	}
	
}