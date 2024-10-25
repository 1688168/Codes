// 20240831 -----------
// 20240831 -----------
class Solution {
    public String reverseWords(String s) {
        String[] ss = s.replaceAll("\\s+", " ").trim().split(" "); //regex
        Collections.reverse(Arrays.asList(ss)); //reverse list of string
        return String.join(" ", ss); //join a list of string, concatenate list of string
    }
}