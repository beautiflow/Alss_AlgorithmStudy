package 박상균.week1.M9020;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    static boolean isPrime(int x) {
        if(x == 2) return true;
        if(x % 2 == 0) return false;
        if(x == 1) return false; // 1은 소수가 아니다.
        for(int i = 3; i <= (x / 3); i += 2) {
            if(x % i == 0) return false;
        }
        return true;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for(int i = 0; i < n; i++) {
            int x = Integer.parseInt(br.readLine());

            int smaller = x / 2;
            int bigger = smaller;

            while(smaller > 1) {
                if(isPrime(smaller) && isPrime(bigger)) break;

                smaller--;
                bigger++;
            }

            System.out.println(smaller + " " + bigger);
        }
        br.close();
    }
}
