package 오나연.week3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B_10870 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        System.out.println(fibonachi(N));

    }
    static int fibonachi(int N){
        if(N == 0){
            return 0;
        }
        if(N == 1){
            return 1;
        }

        return fibonachi(N-1) + fibonachi(N-2);
    }


}
