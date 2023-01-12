package 박상균.week1.M8393;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int sum = 0;
        for(int i = 1; i < n + 1; i++) {
            sum += i;
        }
        System.out.println(sum);
        br.close();
    }
}
