public class RepeatedSubstringPattern {

    public static void main(String[] args) {
        System.out.println(repeatedSubstringPattern("abcabcabcabc"));
        // System.out.println(repeatedSubstringPattern("ababab"));
        // System.out.println(repeatedSubstringPattern("aba"));
    }

    static boolean repeatedSubstringPattern(String s) {
        int wsize = 1;
        String cur, next;
        int len = s.length();
        if (len <= 1)
            return false;
        System.err.println(len);
        // System.err.println(s.substring(0, 3)); // last isnt included
        for (int i = 0; i < len; i++) {
            System.err.println(s.charAt(i));
            cur = s.substring(i, wsize + 1);
            next = s.substring(i + wsize + 1, i + wsize + 1 + wsize);
            System.err.println("cur "+cur);
            if (cur == next) {
                System.err.println("into the if");
            }

        }

        return false;
    }
}
