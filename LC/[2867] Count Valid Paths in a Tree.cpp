/*
* Given a tree (N-nodes from 1,...N and list of edges)
- count valid path num
- A valid path contains only a single prime number in the trade nodes
*/

using LL = long long;
class Solution {
    int Father[100005]; //10^5 number of nodes
    vector<int> next[100005]; //this is the graph 
    unordered_set<int>primes;
    LL global = 0;    
public:    
    int FindFather(int x)
    {
        if (Father[x]!=x)
            Father[x] = FindFather(Father[x]);
        return Father[x];
    }
    
    void Union(int x, int y)
    {
        x = Father[x];
        y = Father[y];
        if (x<y) Father[y] = x;
        else Father[x] = y;
    }     
    
    unordered_set<int>Eratosthenes(int n)
    {
        vector<int>q(n+1,0);
        unordered_set<int>primes;
        for (int i=2; i<=sqrt(n); i++)
        {
            if (q[i]==1) continue;
            int j=i*2;
            while (j<=n)
            {
                q[j]=1;
                j+=i;
            }
        }        
        for (int i=2; i<=n; i++)
        {
            if (q[i]==0)
                primes.insert(i);                
        }
        return primes;
    }
    
    bool isPrime(int x)
    {
        return primes.find(x)!=primes.end();
    }
    
    long long countPaths(int n, vector<vector<int>>& edges) 
    {
        primes = Eratosthenes(n); //produce primes from 1~N      
        
        for (int i=1; i<=n; i++) //initialize union find data structure
            Father[i] = i;
        
        for (auto& edge: edges) //build graph of the tree
        {
            int a = edge[0], b = edge[1];
            next[a].push_back(b);
            next[b].push_back(a);
            if (!isPrime(a) && !isPrime(b)) //if connected nodes both are not prime -> union
            {
                if (FindFather(a)!=FindFather(b))
                    Union(a,b);
            }
        }
        
        unordered_map<int,int>Map;
        for (int i=1; i<=n; i++)
            Map[FindFather(i)]+=1; //how many groups?
            
        for (int p: primes)//for each prime number in the tree
        {
            vector<LL>arr;
            for (int nxt: next[p])//for all connected nodes of a prime number
            {
                if (!isPrime(nxt))
                    arr.push_back(Map[FindFather(nxt)]);
            }
            LL total = accumulate(arr.begin(), arr.end(), 0LL);
            LL sum = 0;
            /*
            two patterns
            1. a path crosses a single prime
            2. starting from a prime, going to a non-prime
            - total here is the connected non-prime count to the prime
            */
            for (LL x: arr)                    
                sum += x*(total-x);         
            global += sum/2 + total;
        }
                
        return global;
    }
    
};