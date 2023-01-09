package 오나연.week1;

import java.util.Scanner;

import static java.lang.Math.sqrt;

public class B_11653 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        for(int i = 2; i <= sqrt(n); i++){
            while(n % i == 0){
                System.out.println(i);
                n /= i;
            }
        }
        if(n != 1){
            System.out.println(n);
        }
    }
}
