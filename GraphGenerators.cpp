#include "GraphGenerators.h"
#include <iostream>
#include <cmath>
#include <tuple>

CompleteGraph::CompleteGraph(int n) : num_vertices(n), rng(std::random_device{}()), dist(0.0, 1.0) {
    vertices.resize(n);
    for (int i = 0; i < n; ++i) {
        vertices[i] = i;
        adjList[i] = std::vector<std::pair<int, double>>();
    }

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            double weight = dist(rng);

            if (weight < 30.0/num_vertices) {
                adjList[i].push_back({j, weight});
                adjList[j].push_back({i, weight});
                edgeList[{std::min(i,j), std::max(i,j)}] = weight;
            }
        }
    }
}

std::map<int, std::vector<std::pair<int, double>>> CompleteGraph::getAdjList() {
    return adjList;
}

std::vector<int> CompleteGraph::getVertices() {
    return vertices;
}
std::map<std::pair<int, int>, double> CompleteGraph::getEdgeList() {
    return edgeList;
}

CompleteGraph2D::CompleteGraph2D(int n) : num_vertices(n), rng(std::random_device{}()), dist(0.0, 1.0) {
    vertices.resize(n);
    points.resize(n);
    for (int i = 0; i < n; ++i) {
        vertices[i] = i;
        adjList[i] = std::vector<std::pair<int, double>>();
        points[i] = {dist(rng), dist(rng)};
    }

    for (int i = 0; i < n; ++i) {
        double x_i = points[i].first;
        double y_i = points[i].second;
        for (int j = 0; j < n; ++j) {
            if (i != j && i < j) {
                double x_j = points[j].first;
                double y_j = points[j].second;
                double dx = x_i - x_j;
                double dy = y_i - y_j;
                double distance = std::sqrt(dx * dx + dy * dy);

                if (distance < 1.52/std::sqrt(num_vertices)) {
                    adjList[i].push_back({j, distance});
                    adjList[j].push_back({i, distance});
                    edgeList[{std::min(i,j), std::max(i,j)}] = distance;
                }
            }
        }
    }
}

std::map<int, std::vector<std::pair<int, double>>> CompleteGraph2D::getAdjList() {
    return adjList;
}

std::vector<int> CompleteGraph2D::getVertices() {
    return vertices;
}
std::map<std::pair<int, int>, double> CompleteGraph2D::getEdgeList() {
    return edgeList;
}

CompleteGraph3D::CompleteGraph3D(int n) : num_vertices(n), rng(std::random_device{}()), dist(0.0, 1.0) {
    vertices.resize(n);
    points.resize(n);
    for (int i = 0; i < n; ++i) {
        vertices[i] = i;
        adjList[i] = std::vector<std::pair<int, double>>();
        points[i] = std::make_tuple(dist(rng), dist(rng), dist(rng));
    }

    for (int i = 0; i < n; ++i) {
        double x_i, y_i, z_i;
        std::tie(x_i, y_i, z_i) = points[i];
        for (int j = 0; j < n; ++j) {
            if (i != j && i < j) {
                double x_j, y_j, z_j;
                std::tie(x_j, y_j, z_j) = points[j];
                double dx = x_i - x_j;
                double dy = y_i - y_j;
                double dz = z_i - z_j;
                double distance = std::sqrt(dx * dx + dy * dy + dz * dz);

                if (distance <= 1.28/std::cbrt(num_vertices)) {
                    adjList[i].push_back({j, distance});
                    adjList[j].push_back({i, distance});
                    edgeList[{std::min(i,j), std::max(i,j)}] = distance;
                }
            }
        }
    }
}

std::map<int, std::vector<std::pair<int, double>>> CompleteGraph3D::getAdjList() {
    return adjList;
}

std::vector<int> CompleteGraph3D::getVertices() {
    return vertices;
}
std::map<std::pair<int, int>, double> CompleteGraph3D::getEdgeList() {
    return edgeList;
}


CompleteGraph4D::CompleteGraph4D(int n) : num_vertices(n), rng(std::random_device{}()), dist(0.0, 1.0) {
    vertices.resize(n);
    points.resize(n);
    for (int i = 0; i < n; ++i) {
        vertices[i] = i;
        adjList[i] = std::vector<std::pair<int, double>>();
        points[i] = std::make_tuple(dist(rng), dist(rng), dist(rng), dist(rng));
    }

    for (int i = 0; i < n; ++i) {
        double x_i, y_i, z_i, a_i;
        std::tie(x_i, y_i, z_i, a_i) = points[i];
        for (int j = 0; j < n; ++j) {
            if (i != j && i < j) {
                double x_j, y_j, z_j, a_j;
                std::tie(x_j, y_j, z_j, a_j) = points[j];
                double dx = x_i - x_j;
                double dy = y_i - y_j;
                double dz = z_i - z_j;
                double da = a_i - a_j;
                double distance = std::sqrt(dx * dx + dy * dy + dz * dz + da * da);

                if (distance < 1.26/std::sqrt(std::sqrt(num_vertices))) {
                    adjList[i].push_back({j, distance});
                    adjList[j].push_back({i, distance});
                    edgeList[{std::min(i,j), std::max(i,j)}] = distance;
                }
            }
        }
    }
}

std::map<int, std::vector<std::pair<int, double>>> CompleteGraph4D::getAdjList() {
    return adjList;
}

std::vector<int> CompleteGraph4D::getVertices() {
    return vertices;
}
std::map<std::pair<int, int>, double> CompleteGraph4D::getEdgeList() {
    return edgeList;
}

HCubeGraph::HCubeGraph(int n) : num_vertices(n), rng(std::random_device{}()), dist(0.0, 1.0) {
    vertices.resize(n);
    for (int i = 0; i < n; ++i) {
        vertices[i] = i;
        adjList[i] = std::vector<std::pair<int, double>>();
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (((i - j) & (i - j - 1)) == 0 && (i - j) > 0) {
                double value = dist(rng);
                if (value <= 16 / std::log2(num_vertices)) {
                    adjList[i].push_back({j, value});
                    adjList[j].push_back({i, value});
                    edgeList[{std::min(i,j), std::max(i,j)}] = value;
                }
            }
        }
    }
}

std::map<int, std::vector<std::pair<int, double>>> HCubeGraph::getAdjList() {
    return adjList;
}

std::vector<int> HCubeGraph::getVertices() {
    return vertices;
}
std::map<std::pair<int, int>, double> HCubeGraph::getEdgeList() {
    return edgeList;
}