/**
 * // This is the robot's control interface.
 * // You should not implement it, or speculate about its implementation
 * class Robot {
 *   public:
 *     // Returns true if the cell in front is open and robot moves into the cell.
 *     // Returns false if the cell in front is blocked and robot stays in the current cell.
 *     bool move();
 *
 *     // Robot will stay in the same cell after calling turnLeft/turnRight.
 *     // Each turn will be 90 degrees.
 *     void turnLeft();
 *     void turnRight();
 *
 *     // Clean the current cell.
 *     void clean();
 * };
 */

class Solution {
    unordered_set<string> visited; //x + "#"  + y
public:
    void cleanRoom(Robot& robot) {
        string code = to_string(0) + "#" + to_string(0);
        visited.insert(code);
        DFS(robot, 0, 0, 0);
    }

    void DFS(Robot & robot, int x, int y, int curDir){
        vector<pair<int, int>> dir({{0, 1}, {1,0}, {0, -1}, {-1, 0}});
        robot.clean();//robot clean the current location
        for(int kk=1; kk<=4; ++kk){
            robot.turnRight();
            int nxtDir = (curDir + kk)%4;
            int ii = x + dir[nxtDir].first;
            int jj = y + dir[nxtDir].second;
            string code = to_string(ii) + "#" + to_string(jj);
            if(visited.find(code)==visited.end() && robot.move()){
                visited.insert(code);
                DFS(robot, ii, jj, nxtDir);
                robot.turnRight();
                robot.turnRight();
                robot.move();
                robot.turnRight();
                robot.turnRight();

            }
        }
    }
};