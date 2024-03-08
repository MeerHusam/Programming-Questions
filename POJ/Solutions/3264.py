import java.io.*;
import java.util.*;

public class Main {
    static int[] data;
    static int N, Q, offset;
    static int[] TreeMax, TreeMin;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        Q = Integer.parseInt(st.nextToken());
        data = new int[N];
        initTree();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            data[i] = Integer.parseInt(st.nextToken());
            update(offset + i, data[i]);
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < Q; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int[] val = query(s + offset - 1, e + offset - 1);
            int ans = val[0] - val[1];
            sb.append(ans).append("\n");
        }

        System.out.println(sb);
    }

    static void initTree() {
        int n = 0;
        while ((1 << n) < N) {
            n++;
        }
        offset = 1 << n;
        TreeMax = new int[offset * 2];
        TreeMin = new int[offset * 2];
        Arrays.fill(TreeMin, Integer.MAX_VALUE);
    }

    static void update(int index, int val) {
        while (index > 0) {
            TreeMax[index] = Math.max(TreeMax[index], val);
            TreeMin[index] = Math.min(TreeMin[index], val);
            index = index >> 1;
        }
    }

    static int[] query(int s, int e) {
        int max = 0;
        int min = Integer.MAX_VALUE;
        int[] val = new int[2];
        val[0] = max;
        val[1] = min;
        while (s <= e) {
            if ((s & 1) == 1) {
                val[0] = Math.max(TreeMax[s], val[0]);
                val[1] = Math.min(TreeMin[s], val[1]);
                s++;
            }
            if ((e & 1) == 0) {
                val[0] = Math.max(TreeMax[e], val[0]);
                val[1] = Math.min(TreeMin[e], val[1]);
                e--;
            }
            s = s >> 1;
            e = e >> 1;
        }
        return val;
    }
}
