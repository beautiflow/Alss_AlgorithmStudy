package 박상균.week2.B9012;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

import java.util.Stack;

public class Main {
    static boolean isVps(char[] parenthesis) {
        Stack<Character> st = new Stack();

        for(char c : parenthesis) {
            if(c == '(') st.push(c);
            else if(c == ')') {
                if(st.isEmpty()) return false;
                if(st.peek() == '(') st.pop();
                else return false;
            }
        }

        if(!st.isEmpty()) return false;
        return true;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        for(int i = 0; i < n; i++) {
            char[] parenthesis = br.readLine().toCharArray();
            if(isVps(parenthesis)) bw.write("YES\n");
            else bw.write("NO\n");
            bw.flush();
        }

        bw.close();
        br.close();
    }
}
