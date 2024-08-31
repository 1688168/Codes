//20240831 ------------------
class Solution {
    private char[] reverseWord(char[] word){
        int ll=0;
        int rr=word.length-1;
        while(ll<rr){
            char tmp = word[rr];
            word[rr]=word[ll];
            word[ll]=tmp;
            ll+=1;
            rr-=1;
        }

        return word;
    }

    public String reverseWords(String s) {
        //replace all spaces with single space - regular expression
        final String pattern = "\\s+";
        s=s.replaceAll(pattern, " ").trim();
        
        return  String.valueOf(reverseWord((
                        String.join(" ", Arrays.stream(s.split(" ")) //convert to stream of string
                                .map(x -> x.toCharArray())      //convert to stream of char[]
                                .map(x -> reverseWord(x))       //stream of reversed char[]
                                .map(x -> String.valueOf(x))    //stream of String
                                .collect(Collectors.toList()))  //reduce to a list of reversed String
        ).toCharArray()));
    }
}

//20240831 ------------------
class Solution {
    private char[] reverseWord(char[] word){
        int ll=0;
        int rr=word.length-1;
        while(ll<rr){
            char tmp = word[rr];
            word[rr]=word[ll];
            word[ll]=tmp;
            ll+=1;
            rr-=1;
        }

        return word;
    }

    public String reverseWords(String s) {
        //replace all spaces with single space - regular expression
        final String pattern = "\\s+";
        s=s.replaceAll(pattern, " ").trim();

        //split sentence into array of words
        final String[] words = s.split(" ");
        //reverse each word inplace 
        var res = String.join(" ", Arrays.stream(words) //convert to stream of string
        .map(x -> x.toCharArray())      //convert to stream of char[]
        .map(x -> reverseWord(x))       //stream of reversed char[]
        .map(x -> String.valueOf(x))    //stream of String
        .collect(Collectors.toList()));  //reduce to a list of reversed String
        
        return  String.valueOf(reverseWord(res.toCharArray()));
    }
}
//------------------
class Solution {
    private char[] reverseWord(char[] word){
        int ll=0;
        int rr=word.length-1;
        while(ll<rr){
            char tmp = word[rr];
            word[rr]=word[ll];
            word[ll]=tmp;
            ll+=1;
            rr-=1;
        }

        return word;
    }

    public String reverseWords(String s) {
        //replace all spaces with single space - regular expression
        final String pattern = "\\s+";
        s=s.replaceAll(pattern, " ").trim();

        //split sentence into array of words
        final String[] words = s.split(" ");
        //reverse each word inplace 
        var list = Arrays.stream(words) //convert to stream of string
        .map(x -> x.toCharArray())      //convert to stream of char[]
        .map(x -> reverseWord(x))       //stream of reversed char[]
        .map(x -> String.valueOf(x))    //stream of String
        .collect(Collectors.toList());  //reduce to a list of reversed String
        
        final String ss = String.join(" ", list);//concatenate Strings to a single String
        return  String.valueOf(reverseWord(ss.toCharArray()));
    }
}