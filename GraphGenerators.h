#ifndef GRAPHGENERATORS_H
#define GRAPHGENERATORS_H

#include <map>
#include <random>
#include <cmath>
#include <vector>

namespace GraphGenerators {

    // Function to generate a random double between 0 and 1
    double generate_random_weight();

    class CompleteGraph {
    public:
        int n;
        std::map<std::pair<int, int>, double> adj_list;

        CompleteGraph(int n_in);
        std::map<std::pair<int, int>, double> getAdjList();
    };

    class HCubeGraph {
    public:
        int n;
        std::map<std::pair<int, int>, double> adj_list;

        HCubeGraph(int n_in);
        std::map<std::pair<int, int>, double> getAdjList();
    };

    class CompleteGraph2D {
    public:
        int n;
        std::map<std::pair<int, int>, double> adj_list;

        CompleteGraph2D(int n_in);
        std::map<std::pair<int, int>, double> getAdjList();
    };

    class CompleteGraph3D {
    public:
        int n;
        std::map<std::pair<int, int>, double> adj_list;

        CompleteGraph3D(int n_in);
        std::map<std::pair<int, int>, double> getAdjList();
    };

    class CompleteGraph4D {
    public:
        int n;
        std::map<std::pair<int, int>, double> adj_list;

        CompleteGraph4D(int n_in);
        std::map<std::pair<int, int>, double> getAdjList();
    };

} // namespace GraphGenerators

#endif