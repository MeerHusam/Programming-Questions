import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int m = scanner.nextInt();
        int k = scanner.nextInt();

        long[] array = new long[n];
        for (int i = 0; i < n; i++) {
            array[i] = scanner.nextLong();
        }

        int[][] operations = new int[m + 1][3];
        for (int i = 1; i <= m; i++) {
            operations[i][0] = scanner.nextInt();
            operations[i][1] = scanner.nextInt();
            operations[i][2] = scanner.nextInt();
        }

        int[] opFreq = new int[m + 1];
        for (int i = 0; i < k; i++) {
            int start = scanner.nextInt();
            int end = scanner.nextInt();
            opFreq[start]++;
            if (end < m) {
                opFreq[end + 1]--;
            }
        }

        for (int i = 1; i <= m; i++) {
            opFreq[i] += opFreq[i - 1];
        }

        long[] prefixSum = new long[n];
        for (int i = 1; i <= m; i++) {
            int l = operations[i][0];
            int r = operations[i][1];
            int d = operations[i][2];
            prefixSum[l - 1] += (long) d * opFreq[i];
            if (r < n) {
                prefixSum[r] -= (long) d * opFreq[i];
            }
        }

        for (int i = 1; i < n; i++) {
            prefixSum[i] += prefixSum[i - 1];
        }

        StringBuilder output = new StringBuilder();
        for (int i = 0; i < n; i++) output.append(array[i] + prefixSum[i]).append(" ");
        System.out.println(output);
    }
}
