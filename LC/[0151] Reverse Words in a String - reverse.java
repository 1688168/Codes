// 20240831 -----------
class Solution {
    public String reverseWords(String s) {
        String[] ss = s.replaceAll("\\s+", " ").trim().split(" ");
        Collections.reverse(Arrays.asList(ss));        
        return String.join(" ", Arrays.asList(ss)); 
    }
}