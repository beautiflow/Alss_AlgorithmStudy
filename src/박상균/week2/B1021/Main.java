package 박상균.week2.B1021;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        LinkedList<Integer> dq = new LinkedList<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] arr = new int[m];
        for(int i = 0; i < n; i++) {
            dq.add(i + 1);
        }
        for(int i = 0; i < m; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int count = 0;
        for(int j = 0; j < m; j++) {
            int idx_dq = dq.indexOf(arr[j]);
            int half = (dq.size() % 2 == 0) ? (dq.size() / 2 - 1) : (dq.size() / 2);

            if(idx_dq <= half) {
                for(int i = 0; i < idx_dq; i++) {
                    int p = dq.pollFirst();
                    dq.addLast(p);
                    count++;
                }
            }
            else {
                for(int i = 0; i < dq.size() - idx_dq; i++) {
                    int p = dq.pollLast();
                    dq.addFirst(p);
                    count++;
                }
            }
            dq.pollFirst();
        }
        bw.write(count + "\n");
        bw.flush();

        br.close();
        bw.close();
    }
}
