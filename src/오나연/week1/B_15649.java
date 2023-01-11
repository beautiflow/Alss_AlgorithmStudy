package 오나연.week1;

import java.util.Scanner;

public class B_15649 {

    public static boolean[] visit;
    public static int[] arr;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();

        arr = new int[M];
        visit = new boolean[N];
        dfs(N, M, 0);
        }

        public static void dfs(int N, int M, int depth){
        // 재귀 깊이가 M과 같아지면 탐색 과정에서 담았던 배열을 출력
            if(depth == M){
                for(int val : arr){
                    System.out.print(val + " ");
                }
                System.out.println();
                return;
            }
            for (int i = 0; i < N; i++){
                // 만약 해당 노드(값)를 방문하지 않았다면?
                if(!visit[i]){
                    visit[i] = true; // 해당 노드를 방문상태로 변경
                    arr[depth] = i + 1;  // 해당 깊이를 index 로 하여 i + 1 값 저장
                    dfs(N, M, depth+1); // 다음 자식 노드 방문을 위해 depth 를 1 증가 시키면서 재귀 호출
                    visit[i] = false; // 자식 노드 방문이 끝나고 돌아오면 방문노드를 방문하지 않은 상태로 변경
                }
            }
    }
}
