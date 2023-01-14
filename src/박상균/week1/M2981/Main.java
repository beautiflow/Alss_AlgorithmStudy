package 박상균.week1.M2981;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class Main {
    static int gcd(int a, int b) {
        while(b > 0) {
            int tmp = a;
            a = b;
            b = tmp % b;
        }
        return a;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        for(int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        int[] diff = new int[n - 1];
        for(int i = 1; i <= diff.length; i++) {
            diff[i - 1] = arr[i] - arr[i - 1];
        }

        int gcd = diff[0];
        for(int i = 1; i < diff.length; i++) {
            gcd = gcd(gcd, diff[i]);
        }

        for(int i = 2; i <= gcd; i++) {
            if(gcd % i == 0) bw.write(i + " ");
        }
        
        bw.flush();

        br.close();
        bw.close();
    }
}

