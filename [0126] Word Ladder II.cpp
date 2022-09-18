class Solution {
public:
    unordered_set<string>wordSet;
    unordered_map<string,vector<string>>next;
    unordered_map<string,unordered_set<string>>prev;
    vector<vector<string>>results;
    string beginWord;

    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList)
    {
        wordList.push_back(beginWord);

        //create word_set
        for (auto str:wordList)
            wordSet.insert(str);
        this->beginWord = beginWord;

        //edge case: if end word not in word_list: just return empty list
        if (wordSet.find(endWord)==wordSet.end()) return {};

        //construct connected word graph
        for (int i=0; i<wordList.size(); i++)
        {
            string str = wordList[i];
            for (int k=0; k<str.size(); k++)
            {
                for (char ch='a'; ch<='z'; ch++)
                {
                    string temp = str;
                    temp[k] = ch;
                    if (temp==str) continue;
                    if (wordSet.find(temp)!=wordSet.end())
                        next[str].push_back(temp);
                }
            }
        }

        unordered_set<string>visited;
        queue<string>q;
        int flag = 0;

        //BFS to find the valid path
        q.push(beginWord);
        visited.insert(beginWord);

        while (!q.empty())
        {
            int len = q.size();
            unordered_set<string>newVisited;

            for (int k=0; k<len; k++)//for each level
            {
                string str = q.front();
                q.pop();

                for (auto nextStr: next[str])//add all children for next level
                {
                    if (visited.find(nextStr)!=visited.end()) //if already visited
                        continue;
                    prev[nextStr].insert(str);//update ancestor mapping table
                    newVisited.insert(nextStr);

                    if (nextStr==endWord) flag = 1;
                }
            }

            for (auto x: newVisited)
            {
                visited.insert(x);
                q.push(x);
            }

            if (flag==1) break;
        }

        if (flag==0) return {};

        DFS(endWord,{endWord});

        return results;
    }

    void DFS(string word, vector<string> path)
    {
        if (word==beginWord)
        {
            reverse(path.begin(),path.end());
            results.push_back(path);
            return;
        }

        for (auto preStr:prev[word])
        {
            vector<string>newPath=path;
            newPath.push_back(preStr);
            DFS(preStr, newPath);
        }
        return;
    }
};
