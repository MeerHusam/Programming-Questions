import java.util.*;
import java.io.*;

public class QC {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] v = new int[n][2];
        int[] s = new int[n];
        int sum = 0;
        List<Integer> tmp = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String[] parts = br.readLine().split(" ");
            v[i][0] = Integer.parseInt(parts[0]);
            v[i][1] = Integer.parseInt(parts[1]);
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (v[j][0] < v[i][1] && v[i][0] < v[j][1]) {
                    s[i]++;
                    s[j]++;
                    sum++;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            if (s[i] == sum) {
                tmp.add(i + 1); // 1-indexed
            }
        }

        System.out.println(tmp.size());
        for (int val : tmp) {
            System.out.print(val + " ");
        }
    }
}
