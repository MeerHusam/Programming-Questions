import java.util.*;

public class QD {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNext()) {
            int n = scanner.nextInt();
            int[] nums = new int[n];
            for (int i = 0; i < n; i++) {
                nums[i] = scanner.nextInt();
            }
            
            int[] ends = new int[n];
            int[] prevIndices = new int[n];
            Arrays.fill(prevIndices, -1);
            int length = 0;
            
            Map<Integer, Integer> indexMap = new HashMap<>();
            
            for (int i = 0; i < n; i++) {
                int num = nums[i];
                int pos = Arrays.binarySearch(ends, 0, length, num);
                if (pos < 0) {
                    pos = -(pos + 1);
                }
                ends[pos] = num;
                if (pos == length) {
                    length++;
                }
                indexMap.put(num, i);
                if (pos > 0) {
                    prevIndices[i] = indexMap.get(ends[pos - 1]);
                }
            }
            
            int[] lisIndices = new int[length];
            for (int i = indexMap.get(ends[length - 1]), j = length - 1; i >= 0; i = prevIndices[i], j--) {
                lisIndices[j] = i;
            }
            
            System.out.println(length);
            for (int index : lisIndices) {
                System.out.print(index + " ");
            }
            System.out.println();
        }
        scanner.close();
    }
}
