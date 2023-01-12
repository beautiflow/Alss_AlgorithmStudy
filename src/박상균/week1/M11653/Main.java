package 박상균.week1.M11653;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int currentValue = 2;

        while(n > 1) {
            if(n % currentValue == 0) {
                n /= currentValue;
                bw.write(currentValue + "\n");
            }
            else {
                currentValue+=1;
            }
        }
        bw.flush();
        bw.close();
        br.close();
    }
}
