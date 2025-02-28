#ifndef GRAPH_GENERATORS_H
#define GRAPH_GENERATORS_H

#include <vector>
#include <map>
#include <random>

// --------------------- CompleteGraph Class ---------------------
class CompleteGraph {
public:
    CompleteGraph(int n);
    std::map<int, std::vector<std::pair<int, double>>> getAdjList();
    std::vector<int> getVertices();
    std::map<std::pair<int, int>, double> getEdgeList();

private:
    int num_vertices;
    std::map<int, std::vector<std::pair<int, double>>> adjList;
    std::vector<int> vertices;
    std::map<std::pair<int, int>, double> edgeList;
    std::mt19937 rng; // Random number generator
    std::uniform_real_distribution<double> dist; // Distribution for random doubles
};

// --------------------- CompleteGraph2D Class ---------------------
class CompleteGraph2D {
public:
    CompleteGraph2D(int n);
    std::map<int, std::vector<std::pair<int, double>>> getAdjList();
    std::vector<int> getVertices();
    std::map<std::pair<int, int>, double> getEdgeList();

private:
    int num_vertices;
    std::map<int, std::vector<std::pair<int, double>>> adjList;
    std::vector<int> vertices;
    std::vector<std::pair<double, double>> points;
    std::map<std::pair<int, int>, double> edgeList;
    std::mt19937 rng;
    std::uniform_real_distribution<double> dist;
};

// --------------------- CompleteGraph3D Class ---------------------
class CompleteGraph3D {
public:
    CompleteGraph3D(int n);
    std::map<int, std::vector<std::pair<int, double>>> getAdjList();
    std::vector<int> getVertices();
    std::map<std::pair<int, int>, double> getEdgeList();

private:
    int num_vertices;
    std::map<int, std::vector<std::pair<int, double>>> adjList;
    std::vector<int> vertices;
    std::vector<std::tuple<double, double, double>> points;
    std::map<std::pair<int, int>, double> edgeList;
    std::mt19937 rng;
    std::uniform_real_distribution<double> dist;
};

// --------------------- CompleteGraph4D Class ---------------------
class CompleteGraph4D {
public:
    CompleteGraph4D(int n);
    std::map<int, std::vector<std::pair<int, double>>> getAdjList();
    std::vector<int> getVertices();
    std::map<std::pair<int, int>, double> getEdgeList();

private:
    int num_vertices;
    std::map<int, std::vector<std::pair<int, double>>> adjList;
    std::vector<int> vertices;
    std::vector<std::tuple<double, double, double, double>> points;
    std::map<std::pair<int, int>, double> edgeList;
    std::mt19937 rng;
    std::uniform_real_distribution<double> dist;
};

// --------------------- HCubeGraph Class ---------------------
class HCubeGraph {
public:
    HCubeGraph(int n);
    std::map<int, std::vector<std::pair<int, double>>> getAdjList();
    std::vector<int> getVertices();
    std::map<std::pair<int, int>, double> getEdgeList();

private:
    int num_vertices;
    std::map<int, std::vector<std::pair<int, double>>> adjList;
    std::vector<int> vertices;
    std::map<std::pair<int, int>, double> edgeList;
    std::mt19937 rng;
    std::uniform_real_distribution<double> dist;
};

#endif // GRAPH_GENERATORS_H