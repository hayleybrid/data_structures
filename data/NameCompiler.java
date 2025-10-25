public class NameCompiler {
    
    public class ReverseWords {
        public String reverseWords(String s) {
            String[] words = s.trim().split("\\s+"); // split words
            StringBuilder reversed = new StringBuilder();

            // append words in reverse order
            for (int i = words.length - 1; i >= 0; i--) {
                reversed.append(words[i]);
                if (i != 0) {
                    reversed.append(" ");
                }
            }
            return reversed.toString();
        }
    }

    public static void main (String[] args) {
        NameCompiler nw = new NameCompiler();
        ReverseWords rw = nw.new ReverseWords();
        System.out.println(rw.reverseWords("Hayley Bridges"));

    }
}

