
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;

/*
 * BOJ_1697
 * - 수빈이는 동생과 숨바꼭질
 * - 수빈이는 걷거나 순간이동 가능
 * - 만약 수빈이의 위치가 X 일 때 걷는 다면, 1초 후에 x-1. x+ 1 이동
 * - 순간이동을 하는 경우 2 * x
 * 수빈이와 동생 위치가 주어질 때 수빈이가 동생을 찾는 가장 빠른 방법?
 * 
 * - N과 K가 0, 10만 과 같은 상황이라면, DFS일 경우 쓸데없이 많은 연산처리가 되는 것이죠,,, 실제로 제출해보면 시간초과가 뜹니다.
 * 
 * - 그래서 BFS로 풀었습니다. 
 * 
 * */

public class Main {
	
	static BufferedReader br;
	static StringTokenizer st;

	static int N, K;
	static int result;
	
	static int [] distance; // 거리 전체를 놓고 ! (메모이제이션 기법)

	public static void bfs(int start) {
		
		Deque<Integer> queue = new ArrayDeque<Integer>();
		queue.add(start); // 큐에 시작 위치 넣기
		distance[start] = 0;
		
		while (!queue.isEmpty()) {
			int currentIdx = queue.poll();
			
			// 만약 동생을 찾으면,
			if (currentIdx == K) {
				System.out.println(distance[currentIdx]);
				return;
			}

			for (int nextIdx : new int[] {currentIdx+1, currentIdx-1, currentIdx * 2}) {	
				if (0 > nextIdx || nextIdx >= 100001) {
					continue;
				}
					
				// 처음 방문했을경우
				if (distance[nextIdx] == 0) {
					distance[nextIdx] = distance[currentIdx] + 1;
					queue.add(nextIdx);
				}
				
			}
			
		}
		
	}

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub

		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine().trim());
		
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		distance = new int[100001];
		bfs(N);
	}

}
