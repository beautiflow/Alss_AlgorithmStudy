package 오나연.week3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class B_11650 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int[][] arr = new int[N][2];

        StringTokenizer st;
        for(int i = 0; i < N ;i++){
            st = new StringTokenizer(br.readLine());
            arr [i][0] = Integer.parseInt(st.nextToken());
            arr [i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr, new Comparator<int[]>() {
            @Override
            public int compare(int[] E1, int[] E2) {
                if(E1[0] == E2[0]) {   // 첫번째 원소가 같다면 두 번째 원소와의 비교
                    return E1[1] - E2[1];
                }
                else {
                    return E1[0] - E2[0];
                }
            }
        });

        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < N; i++){
            sb.append(arr[i][0] + " " + arr[i][1]).append('\n');
        }
        System.out.println(sb);
    }
}
