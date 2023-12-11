// Function to find the intersecting points between two intervals
std::vector<std::vector<int>> IntervalsIntersection(std::vector<std::vector<int>> intervalListA, std::vector<std::vector<int>> intervalListB)
{
    std::vector<std::vector<int>> intersections{}; 
    int i = 0, j = 0;
    while (i < intervalListA.size() && j < intervalListB.size())
    {
        int start = std::max(intervalListA[i][0], intervalListB[j][0]);
        int end = std::min(intervalListA[i][1], intervalListB[j][1]);
        if (start <= end)
        {
            intersections.push_back({start, end});
        }
        if (intervalListA[i][1] < intervalListB[j][1])
        {
            i += 1;
        }
        else
        {
            j += 1;
        }
    }
    return intersections;
}

// Function to print a vector of vectors of integers
void printVector(const std::vector<std::vector<int>>& vec) {
    std::cout << "{";
    for (size_t i = 0; i < vec.size(); ++i) {
        std::cout << "{";
        for (size_t j = 0; j < vec[i].size(); ++j) {
            std::cout << vec[i][j];
            if (j != vec[i].size() - 1) {
                std::cout << ", ";
            }
        }
        std::cout << "}";
        if (i != vec.size() - 1) {
            std::cout << ", ";
        }
    }
    std::cout << "}";
}

// Driver code
int main()
{
    std::vector<std::vector<std::vector<int>>> inputIntervalListA = {
        {{1, 2}},
        {{1, 4}, {5, 6}, {9, 15}},
        {{3, 6}, {8, 16}, {17, 25}},
        {{4, 7}, {9, 16}, {17, 28}, {39, 50}, {55, 66}, {70, 89}},
        {{1, 3}, {5, 6}, {7, 8}, {12, 15}}
    };

    std::vector<std::vector<std::vector<int>>> inputIntervalListB = {
        {{1, 2}},
        {{2, 4}, {5, 7}, {9, 15}},
        {{2, 3}, {10, 15}, {18, 23}},
        {{3, 6}, {7, 8}, {9, 10}, {14, 19}, {23, 33}, {35, 40}, {45, 59}, {60, 64}, {68, 76}},
        {{2, 4}, {7, 10}}
    };

    for (int i = 0; i < inputIntervalListA.size(); i++)
    {
        std::cout << i + 1 << ".\t Interval List A: ";
        printVector(inputIntervalListA[i]);
        std::cout << "\n\t Interval List B: ";
        printVector(inputIntervalListB[i]);
        std::cout << "\n\t Intersecting intervals in 'A' and 'B' are: ";
        printVector(IntervalsIntersection(inputIntervalListA[i], inputIntervalListB[i]));
        std::cout << "\n" << std::string(100, '-') << "\n";
    }
}