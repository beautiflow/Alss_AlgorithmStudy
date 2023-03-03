package 오나연.week2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class B_1021 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        LinkedList<Integer> deque = new LinkedList<>();

        int count = 0; // 2,3 번 연산 누적 합

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        for(int i = 1; i <= N; i++){
            deque.offer(i);
        }

        int[] seq = new int[M];
        st = new StringTokenizer(br.readLine(), " ");
        for(int i = 0; i < M; i++){
            seq[i] = Integer.parseInt(st.nextToken());
        }

        for(int i = 0; i < M; i++){
            int target_index = deque.indexOf(seq[i]);
            int mid_index;

            if(deque.size() % 2 == 0){
                mid_index = deque.size() / 2 - 1;
            }
            else {
                mid_index = deque.size() / 2;
            }

            if(target_index <= mid_index){
                for(int j = 0; j < target_index; j++){
                    int temp = deque.pollFirst();
                    deque.offerLast(temp);
                    count++;
                }
            }
            else {
                for(int j = 0; j < deque.size() - target_index; j++){
                    int temp = deque.pollLast();
                    deque.offerFirst(temp);
                    count++;
                }
            }
            deque.pollFirst();
        }
        System.out.println(count);
    }
}
