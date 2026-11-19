class Solution {
public:
    int trap(vector<int>& height) {
        stack<int> Stack;
        int ret=0;
        for(int ii=0; ii<height.size(); ++ii){
            while(!Stack.empty() && height[Stack.top()] < height[ii]){
                int base = height[Stack.top()];
                Stack.pop();
                if(Stack.empty()) continue;
                int h=min(height[Stack.top()], height[ii]) - base;
                int w = ii - Stack.top() - 1;
                ret += h*w;
            }

            Stack.push(ii);
        }

        return ret;
        
    }
};