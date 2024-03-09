import java.util.Scanner;

class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read the first line of input for n and q
        int n = scanner.nextInt();
        int q = scanner.nextInt();

        // Initialize the efficiency array
        double[] efficiency = new double[n];
        for (int i = 0; i < n; i++) {
            efficiency[i] = scanner.nextDouble();
        }

        // Process each query
        for (int j = 0; j < q; j++) {
            int func = scanner.nextInt();
            if (func == 1) {
                // Update the efficiency value at a specific index
                int i = scanner.nextInt();
                efficiency[i - 1] = scanner.nextDouble();
            } else if (func == 2) {
                // Find and print the maximum efficiency value within a range
                int left = scanner.nextInt();
                int right = scanner.nextInt();
                double currMax = findMax(efficiency, left - 1, right - 1);
                System.out.println(currMax);
            } else if (func == 3) {
                // Calculate and print the average efficiency value within a range
                int left = scanner.nextInt();
                int right = scanner.nextInt();
                double avg = findAverage(efficiency, left - 1, right - 1);
                System.out.printf("%.1f%n", avg);
            }
        }

        scanner.close();
    }

    private static double findMax(double[] efficiency, int left, int right) {
        double max = efficiency[left];
        for (int i = left + 1; i <= right; i++) {
            if (efficiency[i] > max) {
                max = efficiency[i];
            }
        }
        return max;
    }

    private static double findAverage(double[] efficiency, int left, int right) {
        double sum = 0;
        for (int i = left; i <= right; i++) {
            sum += efficiency[i];
        }
        return sum / (right - left + 1);
    }
}
