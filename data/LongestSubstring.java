import java.util.HashMap;

public class LongestSubstring {
    public static int longestSubstringWithoutRepeating(String s) {
        int longest = 0;
        int left = 0;
        HashMap<Character, Integer> counter = new HashMap<>();

        for (int right = 0; right < s.length(); right++) {
            char current = s.charAt(right);
            counter.put(current, counter.getOrDefault(current, 0) + 1);

            while (counter.get(current) > 1) {
                char leftChar = s.charAt(left);
                counter.put(leftChar, counter.get(leftChar) - 1);
                left++;
            }

            longest = Math.max(longest, right - left + 1);
        }

        return longest;
    }

    public static void main(String[] args) {
        String input = "abcabcbb";
        System.out.println("Length of longest substring without repeating characters: " +
                           longestSubstringWithoutRepeating(input));
    }
}
