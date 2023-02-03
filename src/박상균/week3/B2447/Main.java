package 박상균.week3.B2447;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

import java.util.Arrays;

public class Main {
    static char[][] map;
    static void draw(int y, int x, int n) {
        if(n / 3 == 1) {
            map[y][x] = '*'; map[y][x+1] = '*'; map[y][x+2] = '*';
            map[y+1][x] = '*'; map[y+1][x+1] = ' '; map[y+1][x+2] = '*';
            map[y+2][x] = '*'; map[y+2][x+1] = '*'; map[y+2][x+2] = '*';
        }
        else {
            int newN = n / 3;
            draw(y, x, newN); draw(y, x + newN, newN); draw(y, x + 2 * newN, newN);
            draw(y + newN, x, newN); draw(y + newN, x + 2 * newN, newN);
            draw(y + 2 * newN, x, newN); draw(y + 2 * newN, x + newN, newN); draw(y + 2 * newN, x + 2 * newN, newN);
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        map = new char[n][n];

        for(int i = 0; i < n; i++) {
            Arrays.fill(map[i], ' ');
        }

        draw(0, 0, n);

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                bw.write(map[i][j]+"");
            }
            bw.write("\n");
        }
        bw.flush();
        br.close();
        bw.close();
    }
}
