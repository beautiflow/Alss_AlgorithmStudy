package 오나연.week1;

import java.util.Scanner;

public class B_2609 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        System.out.println(eucd(a, b));
        System.out.println(lcm(a, b));

    }
    public static int eucd(int a, int b){
        int r = a % b;
        if(r == 0){
            return b;
        }else{
            return eucd(b,r);
        }
    }

    public static int lcm(int a, int b){
        return a*b / eucd(a,b);
    }
}
