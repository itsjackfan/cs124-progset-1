#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <algorithm>
#include <chrono>
#include <limits>

#include "GraphGenerators.h"

// Union Find Definition
class TreeNode {
public:
    int x;
    TreeNode* parent;
    int rank;

    TreeNode(int x_in) : x(x_in), parent(this), rank(0) {}
};

class UnionFind {
public:
    std::map<int, TreeNode*> nodes;

    UnionFind() {} // makeset

    void makeset(int x) {
        nodes[x] = new TreeNode(x);
    }

    void unite(int x, int y) {
        link(find(x), find(y));
    }

    TreeNode* find(int x) {
        if (nodes[x] != nodes[x]->parent) {
            nodes[x]->parent = find(nodes[x]->parent->x);
        }
        return nodes[x]->parent;
    }

private:
    TreeNode* link(TreeNode* x, TreeNode* y) {
        if (x->rank > y->rank) {
            return link(y, x);
        } else {
            y->rank += 1;
        }
        x->parent = y;
        return y;
    }
};


std::pair<std::map<std::pair<int, int>, double>, double> kruskal(int v, std::map<std::pair<int, int>, double> e) {
    UnionFind uf;
    for (int i = 0; i < v; ++i) {
        uf.makeset(i);
    }

    // Sort edges by weight. C++ needs a vector for this
    std::vector<std::pair<std::pair<int, int>, double>> sorted_edges_vec(e.begin(), e.end());
    std::sort(sorted_edges_vec.begin(), sorted_edges_vec.end(), [](const auto& a, const auto& b){
        return a.second < b.second;
    });

    std::map<std::pair<int, int>, double> X;
    double max_val = 0;
    for (const auto& edge_pair : sorted_edges_vec) {
        std::pair<int, int> edge = edge_pair.first;
        double weight = edge_pair.second;

        if (uf.find(edge.first) != uf.find(edge.second)) {
            X[edge] = weight;
            uf.unite(edge.first, edge.second);
            max_val = std::max(max_val,weight);
        }
    }

    return {X, max_val};
}

int main(int argc, char* argv[]) {
    if (argc != 5) {
        std::cerr << "Usage: program <graph_type> <num_points> <num_trials> <dimension>\n";
        return 1;
    }

    // Note: In C++, argv[0] is the program name itself, so the arguments start from argv[1]
    std::string graph_type = argv[1]; // unused
    int numpoints = std::stoi(argv[2]);
    int numtrials = std::stoi(argv[3]);
    int dimension = std::stoi(argv[4]);

    double kruskal_weight_sum = 0.0;

    // Time measuring using chrono.
    auto start_time = std::chrono::high_resolution_clock::now();

    if (dimension == 0) {
        // create graph
        auto start_time = std::chrono::high_resolution_clock::now();
        for (int _i = 0; _i < numtrials; ++_i) {
            GraphGenerators::CompleteGraph completeGraph(numpoints);
            std::map<std::pair<int, int>, double> adj_list = completeGraph.getAdjList();
           
            std::pair<std::map<std::pair<int, int>, double>, double> kruskal_result = kruskal(numpoints, adj_list);
            std::map<std::pair<int, int>, double> MST_kruskal = kruskal_result.first;
             double max_edge_weight = kruskal_result.second;

            // calculate averages of weights
            for (const auto& edge : MST_kruskal) {
                 kruskal_weight_sum += adj_list.count(edge.first) > 0 ? adj_list[edge.first] : 0;
            }
        }

        double kruskal_avg = kruskal_weight_sum / numtrials;
        std::cout << kruskal_avg << " " << numpoints << " " << numtrials << " " << dimension << std::endl;
    } else if (dimension == 1) {
        // create graph
        auto start_time = std::chrono::high_resolution_clock::now();
        for (int _i = 0; _i < numtrials; ++_i) {
            GraphGenerators::HCubeGraph hCubeGraph(numpoints);
            std::map<std::pair<int, int>, double> adj_list = hCubeGraph.getAdjList();

            std::pair<std::map<std::pair<int, int>, double>, double> kruskal_result = kruskal(numpoints, adj_list);
            std::map<std::pair<int, int>, double> MST_kruskal = kruskal_result.first;
             double max_edge_weight = kruskal_result.second;
            // calculate averages of weights
            for (const auto& edge : MST_kruskal) {
                kruskal_weight_sum += adj_list.count(edge.first) > 0 ? adj_list[edge.first] : 0;
            }
        }

        double kruskal_avg = kruskal_weight_sum / numtrials;
        std::cout << kruskal_avg << " " << numpoints << " " << numtrials << " " << dimension << std::endl;
    } else if (dimension == 2) {
         // create graph
        auto start_time = std::chrono::high_resolution_clock::now();
        for (int _i = 0; _i < numtrials; ++_i) {
            GraphGenerators::CompleteGraph2D completeGraph2D(numpoints);
            std::map<std::pair<int, int>, double> adj_list = completeGraph2D.getAdjList();

            std::pair<std::map<std::pair<int, int>, double>, double> kruskal_result = kruskal(numpoints, adj_list);
            std::map<std::pair<int, int>, double> MST_kruskal = kruskal_result.first;
             double max_edge_weight = kruskal_result.second;

            // calculate averages of weights
            for (const auto& edge : MST_kruskal) {
                kruskal_weight_sum += adj_list.count(edge.first) > 0 ? adj_list[edge.first] : 0;
            }
        }

        double kruskal_avg = kruskal_weight_sum / numtrials;
        std::cout << kruskal_avg << " " << numpoints << " " << numtrials << " " << dimension << std::endl;
    } else if (dimension == 3) {
          // create graph
        auto start_time = std::chrono::high_resolution_clock::now();
        for (int _i = 0; _i < numtrials; ++_i) {
            GraphGenerators::CompleteGraph3D completeGraph3D(numpoints);
            std::map<std::pair<int, int>, double> adj_list = completeGraph3D.getAdjList();

             std::pair<std::map<std::pair<int, int>, double>, double> kruskal_result = kruskal(numpoints, adj_list);
            std::map<std::pair<int, int>, double> MST_kruskal = kruskal_result.first;
             double max_edge_weight = kruskal_result.second;

            // calculate averages of weights
            for (const auto& edge : MST_kruskal) {
                kruskal_weight_sum += adj_list.count(edge.first) > 0 ? adj_list[edge.first] : 0;
            }
        }

        double kruskal_avg = kruskal_weight_sum / numtrials;
        std::cout << kruskal_avg << " " << numpoints << " " << numtrials << " " << dimension << std::endl;
    } else if (dimension == 4) {
        // create graph
        auto start_time = std::chrono::high_resolution_clock::now();
        std::ofstream outfile("output.txt", std::ios::app);

        for (int _i = 0; _i < numtrials; ++_i) {
            GraphGenerators::CompleteGraph4D completeGraph4D(numpoints);
            std::map<std::pair<int, int>, double> adj_list = completeGraph4D.getAdjList();

           
            std::pair<std::map<std::pair<int, int>, double>, double> kruskal_result = kruskal(numpoints, adj_list);
            std::map<std::pair<int, int>, double> MST_kruskal = kruskal_result.first;
             double max_edge_weight = kruskal_result.second;

            // calculate averages of weights
            for (const auto& edge : MST_kruskal) {
                 kruskal_weight_sum += adj_list.count(edge.first) > 0 ? adj_list[edge.first] : 0;
            }

           
        }
        outfile.close();
        double kruskal_avg = kruskal_weight_sum / numtrials;
        std::cout << kruskal_avg << " " << numpoints << " " << numtrials << " " << dimension << std::endl;
    } else {
        //pass
    }

    return 0;
}