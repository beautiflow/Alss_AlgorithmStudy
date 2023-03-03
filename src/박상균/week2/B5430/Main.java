package 박상균.week2.B5430;

import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;

public class Main {
    static void functions(String func, String[] elements) {
        boolean isReversed = false;
        int head = 0;
        int tail = elements.length - 1;
        String[] funcs = func.split("");
        for(String f : funcs) {
            if(head >= elements.length || head < 0 || tail >= elements.length || tail < 0) {
                System.out.println("error");
                return;
            }
            if(f.equals("R")) {
                int tmp = head;
                head = tail;
                tail = tmp;
                isReversed = !isReversed;
            }
            if(f.equals("D")) {
                if(elements[head].equals("")) {
                    System.out.println("error");
                    return;
                }
                if(!isReversed) {
                    if(head > tail) {
                        System.out.println("error");
                        return;
                    }
                    head += 1;
                }
                else {
                    if(tail > head) {
                        System.out.println("error");
                        return;
                    }
                    head -= 1;
                }
            }
        }

        StringBuilder sb = new StringBuilder("[");
        while(true) {
            if(isReversed){
                if(tail > head) break;
                sb.append(elements[head]);
                if(tail != head) sb.append(",");
                head-=1;
            }
            else {
                if(head > tail) break;
                sb.append(elements[head]);
                if(tail != head) sb.append(",");
                head+=1;
            }
        }
        sb.append("]");
        System.out.println(sb);

    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        for(int i = 0; i < t; i++) {
            String function = br.readLine();
            int n = Integer.parseInt(br.readLine());
            String arr = br.readLine();
            String[] elements = arr.substring(1, arr.length() - 1).split(",");
            functions(function, elements);
        }

        br.close();
    }
}
