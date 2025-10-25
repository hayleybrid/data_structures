import java.util.HashMap;
import java.util.Scanner;

public class TwoSum {
    public static int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numToIndex = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (numToIndex.containsKey(complement)) {
                return new int[] { numToIndex.get(complement), i };
            }
            numToIndex.put(nums[i], i);
        }

        return new int[] {}; // return empty array if no solution found
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input: numbers separated by spaces
        String[] parts = sc.nextLine().split(" ");
        int[] nums = new int[parts.length];
        for (int i = 0; i < parts.length; i++) {
            nums[i] = Integer.parseInt(parts[i]);
        }

        // Input: target value
        int target = sc.nextInt();

        int[] res = twoSum(nums, target);

        // Output: print indices separated by a space
        for (int i = 0; i < res.length; i++) {
            System.out.print(res[i]);
            if (i < res.length - 1) System.out.print(" ");
        }

        sc.close();
    }
}
