import java.util.*;

public class QB {


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        while (t-- > 0) {
            int n = scanner.nextInt();
            int p = scanner.nextInt();
            int k = scanner.nextInt();
            scanner.nextLine();  // Consume the newline
            String a = scanner.nextLine();
            int x = scanner.nextInt();
            int y = scanner.nextInt();

            int[] c = new int[n];
            for (int i = n - 1; i >= p - 1; i--) {
                c[i] = (i + k < n ? c[i + k] : 0) + (a.charAt(i) == '0' ? 1 : 0);
            }

            int minTime = Integer.MAX_VALUE;
            for (int q = p; q <= n; q++) {
                int time = c[q - 1] * x + (q - p) * y;
                minTime = Math.min(minTime, time);
            }
            System.out.println(minTime);
        }
        scanner.close();
    }
}
