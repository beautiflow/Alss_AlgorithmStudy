package 박상균.week2.B2493;


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        int[] answer = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Stack<Integer []> s = new Stack<>();
        s.push(new Integer[] {arr[n - 1], n - 1});

        for(int i = n - 2; i >= 0; i--) {
            int value = arr[i];
            if(s.isEmpty()) {
                s.push(new Integer[] {arr[i], i});
                continue;
            }
            if(s.peek()[0] > value) s.push(new Integer[] {arr[i], i});
            else {
                int currentStackTop = s.peek()[0];
                while(!s.isEmpty()) {
                    if(currentStackTop > value) break;
                    Integer[] p = s.pop();
                    answer[p[1]] = i + 1;
                    if(s.isEmpty()) break;
                    currentStackTop = s.peek()[0];
                }
                s.push(new Integer[] {value, i});
            }
        }

        for(int i = 0; i < n; i++) {
            bw.write(answer[i] + " ");
        }
        bw.write("\n");
        bw.flush();

        br.close();
        bw.close();
    }
}
