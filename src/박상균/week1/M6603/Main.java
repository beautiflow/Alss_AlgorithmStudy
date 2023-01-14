package 박상균.week1.M6603;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.BufferedWriter;

import java.util.ArrayList;

public class Main {
    static ArrayList<boolean[]> checklist = new ArrayList<>();
    static ArrayList<Integer> list = new ArrayList<>();
    static void dfs(int idx, int count, boolean[] checks) { // idx: 확인하는 배열 인덱스, count: 1의 개수
        if(count == 6) {
            checklist.add(checks);
            return;
        }
        if(idx >= list.size()) return;
        
        boolean[] newCheckList1 = checks.clone(); // 이 index check (true)
        boolean[] newCheckList2 = checks.clone(); // false

        newCheckList1[idx] = true;
        dfs(idx + 1, count + 1, newCheckList1);
        dfs(idx + 1, count, newCheckList2);
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        while(true) {
            String[] str = br.readLine().split(" ");
            if(Integer.parseInt(str[0]) == 0) break;

            for(int i = 1; i < str.length; i++) {
                list.add(Integer.parseInt(str[i]));
            }

            dfs(0, 0, new boolean[str.length - 1]);

            // 출력
            for(boolean[] checks : checklist) {
                for(int i = 0; i < checks.length; i++) {
                    if(checks[i]) bw.write(list.get(i) + " ");
                }
                bw.write("\n");
            }
            bw.flush();

            // 초기화
            checklist = new ArrayList<>();
            list = new ArrayList<>();
            bw.write("\n");
        }

        br.close();
        bw.close();
    }
}
