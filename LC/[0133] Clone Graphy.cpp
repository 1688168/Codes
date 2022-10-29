/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    unordered_map<Node *, Node *> old2new;
    Node* cloneGraph(Node* node) {
        if(node == nullptr) return nullptr;

        if(old2new.find(node) != old2new.end()){
            return old2new[node];//already cloned (visited)
        }

        old2new[node]=new Node(node->val); //make a copy
        for(auto & c: node->neighbors){ //DFS for all neighbors
            old2new[node]->neighbors.push_back(cloneGraph(c)); //adjacency list
        }

        return old2new[node];
    }
};
