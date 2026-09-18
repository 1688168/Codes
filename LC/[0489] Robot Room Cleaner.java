import java.util.Set;

/**
    * // This is the robot's control interface.
    * // You should not implement it, or speculate about its implementation
    * interface Robot {
    *     // Returns true if the cell in front is open and robot moves into the cell.
    *     // Returns false if the cell in front is blocked and robot stays in the current cell.
    *     public boolean move();
    *
    *     // Robot will stay in the same cell after calling turnLeft/turnRight.
    *     // Each turn will be 90 degrees.
    *     public void turnLeft();
    *     public void turnRight();
    *
    *     // Clean the current cell.
    *     public void clean();
    * }
    */

    class Solution {
        //setup dfs framework
        private final Set<String> visited = new HashSet<>();
        //N, E, S, W
        private static final int[][] DIRS = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

        private String encode(int xx, int yy){
                return xx+"#"+yy;
        }

        private void goBack(Robot robot){
                robot.turnRight();//turn 180
                robot.turnRight();
                robot.move();//return to prev spot
                robot.turnRight();//turn 180 again facing original direction
                robot.turnRight();
        }

        private void dfs(Robot robot, int xx, int yy, int dd){
                robot.clean();//first thing you do in a cell is clean
                //try all directions
                for(int ii=1; ii<=4; ++ii){//4 directions clockwise
                    robot.turnRight(); //try next direction
                    int ndd = (dd+ii)%4;
                    int nxx = xx + DIRS[ndd][0]; 
                    int nyy = yy + DIRS[ndd][1]; 
                    if(!visited.contains(encode(nxx, nyy)) && robot.move()){
                        visited.add(encode(nxx, nyy));
                        dfs(robot, nxx, nyy, ndd);
                        goBack(robot);
                    }   
                }
        }

        public void cleanRoom(Robot robot) {
                visited.clear();//reset visited
                visited.add(encode(0, 0));//starting point
                dfs(robot, 0, 0, 0);
        }
    }