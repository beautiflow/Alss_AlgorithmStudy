package 박상균.week2.B10845;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

import java.util.LinkedList;

public class Main {
    static LinkedList<Integer> q = new LinkedList<>();
    static void queue(String[] str) {
        if(str[0].equals("push")) q.add(Integer.parseInt(str[1])); // push
        if(str[0].equals("pop")) {
            if(q.isEmpty()) System.out.println(-1);
            else System.out.println(q.poll());
        }
        if(str[0].equals("size")) System.out.println(q.size());
        if(str[0].equals("empty")) {
            if(q.isEmpty()) System.out.println(1);
            else System.out.println(0);
        }
        if(str[0].equals("front")) {
            if(q.isEmpty()) System.out.println(-1);
            else System.out.println(q.peek());
        }
        if(str[0].equals("back")) {
            if(q.isEmpty()) System.out.println(-1);
            else System.out.println(q.getLast());
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for(int i = 0; i < n; i++) {
            String[] str = br.readLine().split(" ");
            queue(str);
        }
        br.close();
    }
}
