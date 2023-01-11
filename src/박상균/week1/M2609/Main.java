package 박상균.week1.M2609;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

import java.util.StringTokenizer;

public class Main {
    public static int gcd(int n, int m) {
        if(m == 0) return n;
        return gcd(m, n % m);
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int gcd = gcd(n, m);
        int lcm = n * m / gcd;
        System.out.println(gcd);
        System.out.println(lcm);
        br.close();
    }
}
