public class Java1 {
    

    public static int countUnsafe(int L, int R) {
        int count = 0;
        for (int i = L; i <= R; i++) {
            String s = String.valueOf(i);
            if (s.charAt(0) == s.charAt(s.length() - 1)) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        int L = 10, R = 25;
        System.out.println(countUnsafe(L, R)); // Output: 2
    }

}
