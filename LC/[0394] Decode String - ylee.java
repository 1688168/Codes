class Solution {
    public String decodeString(String s) {
        //mental model: curr_str + curr_num*[next]
        
        Deque<String> str_stk = new ArrayDeque<>(); //how to declare java stack data structure
        Deque<Integer> num_stk = new ArrayDeque<>();
        StringBuilder curr_str = new StringBuilder();//how to accumulate string in java, use StringBuilder
        int curr_num = 0;
        int ii = 0;

        while(ii < s.length()){
            char cc = s.charAt(ii);
            if(Character.isDigit(cc)){ //how to check if char is digit in java
                curr_num = curr_num*10+cc-'0'; //how to accumulate num in java
            }else if(cc=='['){
                str_stk.push(curr_str.toString());
                num_stk.push(curr_num);
                curr_num=0;
                curr_str = new StringBuilder();
            }else if(cc==']'){
                String prev_str = str_stk.pop();
                Integer prev_num = num_stk.pop();
                String parsedString = curr_str.toString();
                curr_str = new StringBuilder(prev_str);
                for(int jj=0; jj<prev_num; ++jj){
                    curr_str.append(parsedString);
                }
            }else{//cc is char
                curr_str.append(cc);
            }
            ++ii;
        }

        return curr_str.toString();
    }
}