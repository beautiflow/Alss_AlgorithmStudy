package 오나연.week3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B_2947 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine()," ");

        int[] arr = new int[5];
        for(int i = 0; i < 5; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        for(int j = 0; j < 5; j++){
            for(int i = 0 ; i < 4; i++){
                if(arr[i]>arr[i+1]){
                    int temp = arr[i];
                    arr[i] = arr[i+1];
                    arr[i+1] = temp;
                    for(int num:arr){
                        System.out.print(num + " ");
                    }
                    System.out.println();
                }
            }
        }
    }
}
