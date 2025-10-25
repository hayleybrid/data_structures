public class Java3 {

    /**
     * Returns the minimum number of boxes Mary must buy from the top
     * so that she has at least one copy of each candle 1..K.
     * If impossible (some number in 1..K not present), returns -1.
     *
     * @param stack an array of length N representing the stack from top (index 0)
     *              to bottom (index N-1)
     * @param K     the highest numbered candle Mary needs (needs 1..K)
     * @return minimal number of boxes to buy, or -1 if impossible
     */
    public static int minPurchasesForCandles(int[] stack, int K) {
        if (K <= 0)
            return 0; // nothing required

        // keep track of which numbers 1..K we've seen
        boolean[] seen = new boolean[K + 1]; // index 0 unused
        int remain = K; // number of distinct required candles still needed

        for (int i = 0; i < stack.length; i++) {
            int val = stack[i];
            if (val >= 1 && val <= K) {
                if (!seen[val]) {
                    seen[val] = true;
                    remain--;
                    if (remain == 0) {
                        // i is 0-based index; number of purchases is i+1
                        return i + 1;
                    }
                }
            }
            // otherwise the candle is irrelevant (outside 1..K)
        }

        // after scanning all boxes some required candle(s) are missing
        return -1;
    }

    // example driver
    public static void main(String[] args) {
        int[] stack1 = { 2, 5, 1, 3, 2, 4 }; // top is index 0
        System.out.println(minPurchasesForCandles(stack1, 4)); // prints 6

        int[] stack2 = { 1, 2, 3 };
        System.out.println(minPurchasesForCandles(stack2, 3)); // prints 3

        int[] stack3 = { 2, 2, 2 };
        System.out.println(minPurchasesForCandles(stack3, 2)); // prints -1 (no candle 1)
    }
}
