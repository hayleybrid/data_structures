import java.util.*;
public class java2 {
    public static long maxProfit(int[] cost, int[] sell, long K) {
        int n = cost.length;
        List<int[]> items = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int gain = sell[i] - cost[i];
            if (gain > 0) { // ignore non-positive gains
                items.add(new int[]{cost[i], gain});
            }
        }
        items.sort(Comparator.comparingInt(a -> a[0])); // sort by cost ascending

        long capital = K;
        for (int[] it : items) {
            int c = it[0];
            int g = it[1];
            if (capital >= c) {
                capital += g;
            } else {
                break;
            }
        }
        return capital - K;
    }

    public static void main(String[] args) {
        int[] cost = {5, 10, 3, 12};
        int[] sell = {7, 15, 3, 20};
        long K = 5;
        System.out.println(maxProfit(cost, sell, K)); // prints 2
    }

}
