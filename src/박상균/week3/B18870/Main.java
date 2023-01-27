package 박상균.week3.B18870;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        HashMap<Integer, Integer> hashMap = new HashMap<>();

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for(int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int[] sortedArr = arr.clone();
        Arrays.sort(sortedArr);

        int cur_value = 0;
        for(int i = 0; i < n; i++) {
            if(!hashMap.containsKey(sortedArr[i])) {
                hashMap.put(sortedArr[i], cur_value);
                cur_value++;
            }
        }

        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < n; i++) {
            sb.append(hashMap.get(arr[i]));
            sb.append(" ");
        }

        System.out.println(sb.toString());
        

        br.close();
    }
}
