package 박상균.week1.M1929;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        int arr[] = new int[n+1];

        for(int i = 2; i < n + 1; i++) {
            arr[i] = i;
        }

        for(int i = 2; i <= n / 2; i++) {
            if(arr[i] == 0) continue;
            for(int j = 2 * i; j < n + 1; j += i) {
                arr[j] = 0;
            }
        }

        for(int i = m; i < n + 1; i++) {
            if(arr[i] != 0) System.out.println(i);
        }

        br.close();
    }
}
