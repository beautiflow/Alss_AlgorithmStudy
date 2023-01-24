package 박상균.week2.B11866;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        ArrayList<Integer> list = new ArrayList();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        for(int i = 0; i < n; i++) {
            list.add(i+1);
        }

        int[] answer = new int[n];
        int current_index = 0;
        int current_size = n;
        bw.write("<");
        for(int i = 0; i < n; i++) {
            current_index = (current_index + k - 1) % current_size;
            answer[i] = list.remove(current_index);
            current_size -= 1;
            bw.write(answer[i] + "");
            if(i < n - 1) bw.write(", ");
        }
        bw.write(">");
        bw.flush();
        
        bw.close();
        br.close();
    }
}
