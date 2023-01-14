package 오나연.week1;

import java.util.Scanner;

public class B_10974 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.close();


        int[] arr = new int[n];  // r 개를 뽑기 위한 n개의 값 저장소
        int[] output = new int[n]; // 뽑힌 r 개의 값 저장소
        boolean[] visited = new boolean[n];  // 중복해서 뽑지 않기 위해 체크하는 값


        for(int i = 0; i < n; i++){
            arr[i] = i + 1;
        }
        perm(arr, output, visited, 0 , n, n);
    }

    // 순서를 지키면서 n 개 중에서 r 개를 뽑는 경우
    static void perm(int[] arr, int[] output, boolean[] visited, int depth, int n, int r){
        if(depth == r){
            print(output, r);
            return;
        }

        for(int i = 0; i < n; i++){
            if(visited[i] != true){
                visited[i] = true;
                output[depth] = arr[i];
                perm(arr, output, visited, depth + 1, n ,r);
                visited[i] = false;
            }
        }
    }

    static void print(int[] arr, int r){
        for(int i = 0; i < r; i++){
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}
