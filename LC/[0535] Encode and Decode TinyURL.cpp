class Solution {
    unordered_map<string, string> Map1;//long->short
    unordered_map<string, string> Map2;//short->long
    string dict="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

public:

    // Encodes a URL to a shortened URL.
    string encode(string longUrl) {
        string str;
        do{
                str="";
                for(int ii=0; ii<7; ++ii){
                    str.push_back(dict[rand()%62]);
                }
        }while (Map1.find(str) != Map2.end());

        Map1[longUrl]=str;
        Map2[str]=longUrl;
        return str;
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
        return Map2[shortUrl];
    }
};

// Your Solution object will be instantiated and called as such:
// Solution solution;
// solution.decode(solution.encode(url));