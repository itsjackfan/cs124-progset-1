#include "GraphGenerators.h"
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <limits>
#include <chrono>
#include <string>
#include <numeric> // For accumulate
#include <iomanip> // For setprecision

// --------------------- MST Algorithms and Main Function (GraphAlgorithms.cpp) ---------------------

// TreeNode, UnionFind, MinHeap, prim_with_edge_weights, kruskal classes and functions remain the same as in the previous response

class TreeNode {
public:
    int x;
    TreeNode* parent;
    int rank;

    TreeNode(int x_val) : x(x_val), parent(this), rank(0) {}
};

class UnionFind {
public:
    std::map<int, TreeNode*> nodes;

    UnionFind() {} // makeset

    void makeset(int x) {
        nodes[x] = new TreeNode(x);
    }

    TreeNode* find(int x) {
        if (nodes[x] != nodes[x]->parent) {
            nodes[x]->parent = find(nodes[x]->parent->x);
        }
        return nodes[x]->parent;
    }

    TreeNode* link(TreeNode* x, TreeNode* y) {
        if (x->rank > y->rank) {
            return link(y, x);
        } else {
            y->rank++;
        }
        x->parent = y;
        return y;
    }

    TreeNode* unite(int x, int y) {
        return link(find(x), find(y));
    }
};

class MinHeap {
public:
    std::vector<std::pair<int, double>> heap;
    int size;
    std::set<int> in_set;

    MinHeap() : size(0) {}

    void min_heapify(int i) {
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        int smallest = i;

        if (left < size && heap[left].second < heap[smallest].second) {
            smallest = left;
        }
        if (right < size && heap[right].second < heap[smallest].second) {
            smallest = right;
        }
        if (smallest != i) {
            swap(i, smallest);
            min_heapify(smallest);
        }
    }

    std::pair<int, double> extract_min() {
        if (size == 0) {
            return {-1, -1.0}; // Or throw an exception, depending on error handling
        }

        std::pair<int, double> min_node = heap[0];
        std::pair<int, double> last = heap.back();
        heap.pop_back();
        size--;
        in_set.erase(min_node.first);

        if (size > 0) {
            heap[0] = last;
            min_heapify(0);
        }

        return min_node;
    }

    void insert(int v, double weight) {
        if (in_set.count(v)) {
            for (int i = 0; i < size; ++i) {
                if (heap[i].first == v && heap[i].second > weight) {
                    heap[i] = {v, weight};
                    heapify_up(i);
                    return;
                }
            }
        } else {
            heap.push_back({v, weight});
            size++;
            in_set.insert(v);
            heapify_up(size - 1);
        }
    }

    void heapify_up(int i) {
        int parent = (i - 1) / 2;
        while (i > 0 && heap[parent].second > heap[i].second) {
            swap(i, parent);
            i = parent;
            parent = (i - 1) / 2;
        }
    }

    void swap(int i, int j) {
        std::swap(heap[i], heap[j]);
    }
};


std::pair<std::pair<std::vector<std::pair<int, int>>, double>, std::vector<double>> prim_with_edge_weights(const std::vector<int>& vertices, const std::map<int, std::vector<std::pair<int, double>>>& edges) {
    /**
     * vertices: list of the vertices (not just the total number of vertices)
     * edges: adjacency list in form of dictionary {u: [(v_1,w_1), (v_2,w_2),...],...}
     */
    // Initialize
    int num_points = vertices.size();
    std::map<int, double> d;
    std::map<int, int> prev; // Changed from None to int, using -1 to represent None

    for (int v : vertices) {
        d[v] = std::numeric_limits<double>::infinity();
        prev[v] = -1; // Representing None
    }

    std::set<int> S;
    MinHeap H;

    // Start at source
    int source = vertices[0];
    d[source] = 0;
    prev[source] = -1; // None
    H.insert(source, 0);

    std::vector<std::pair<int, int>> mst;
    double mst_weight = 0;
    std::vector<double> mst_edge_weights; // To collect edge weights

    while (H.size > 0) {
        std::pair<int, double> current = H.extract_min();
        int u = current.first;
        double weight = current.second;

        if (S.count(u)) {
            continue;
        }

        S.insert(u);

        if (prev[u] != -1) {
            mst.push_back({prev[u], u});
            mst_weight += weight;
            mst_edge_weights.push_back(weight); // Add edge weight to the list
        }

        if (edges.count(u)) {
            for (const auto& edge : edges.at(u)) {
                int v = edge.first;
                double w = edge.second;
                if (!S.count(v) && d[v] > w) {
                    d[v] = w;
                    prev[v] = u;
                    H.insert(v, w);
                }
            }
        }
    }

    return {{mst, mst_weight}, mst_edge_weights};
}


std::pair<std::map<std::pair<int, int>, double>, double> kruskal(int v_count, const std::map<std::pair<int, int>, double>& e) {
    UnionFind uf;
    std::map<std::pair<int, int>, double> sorted_edges = e; // Already sorted in Python, but maps are sorted by key in C++ anyway

    std::map<std::pair<int, int>, double> X;

    for (int i = 0; i < v_count; ++i) {
        uf.makeset(i);
    }

    std::vector<std::pair<std::pair<int, int>, double>> sorted_edge_vector;
    for (const auto& edge_pair : sorted_edges) {
        sorted_edge_vector.push_back({edge_pair.first, edge_pair.second});
    }
    std::sort(sorted_edge_vector.begin(), sorted_edge_vector.end(), [](const std::pair<std::pair<int, int>, double>& a, const std::pair<std::pair<int, int>, double>& b) {
        return a.second < b.second;
    });


    for (const auto& edge_item : sorted_edge_vector) {
        std::pair<int, int> edge = edge_item.first;
        double weight = edge_item.second;
        if (uf.find(edge.first) != uf.find(edge.second)) {
            X[edge] = weight;
            uf.unite(edge.first, edge.second);
        }
    }

    double max_edge_weight = 0;
    for (const auto& pair : X) {
        if (pair.second > max_edge_weight) {
            max_edge_weight = pair.second;
        }
    }

    return {X, max_edge_weight};
}


int main(int argc, char* argv[]) {
    if (argc != 5) {
        std::cerr << "Usage: program_name <numpoints> <numtrials> <dimension>" << std::endl;
        return 1;
    }

    int numpoints = std::stoi(argv[2]);
    int numtrials = std::stoi(argv[3]);
    int dimension = std::stoi(argv[4]);

    double kruskal_weight_sum = 0;
    double prim_weight_sum = 0;
    std::vector<double> all_mst_edge_weights; // Declare outside dimension blocks


    if (dimension == 0) {
        all_mst_edge_weights.clear(); // Clear for each dimension

        for (int _ = 0; _ < numtrials; ++_) {
            CompleteGraph graph(numpoints);
            std::map<int, std::vector<std::pair<int, double>>> adj_list = graph.getAdjList();
            std::vector<int> vertices = graph.getVertices();

            auto prim_result_pair = prim_with_edge_weights(vertices, adj_list);
            double prim_weight = prim_result_pair.first.second;
            std::vector<double> mst_edge_weights = prim_result_pair.second;


            prim_weight_sum += prim_weight;
            all_mst_edge_weights.insert(all_mst_edge_weights.end(), mst_edge_weights.begin(), mst_edge_weights.end());
        }


    } else if (dimension == 1) {
        all_mst_edge_weights.clear(); // Clear for each dimension

        for (int _ = 0; _ < numtrials; ++_) {
            HCubeGraph graph(numpoints);
            std::map<int, std::vector<std::pair<int, double>>> adj_list = graph.getAdjList();
            std::map<std::pair<int, int>, double> edge_list = graph.getEdgeList();
            std::vector<int> vertices = graph.getVertices();


            auto mst_kruskal_result = kruskal(numpoints, edge_list);
            std::map<std::pair<int, int>, double> MST_kruskal = mst_kruskal_result.first;

            double current_kruskal_weight_sum = 0;
            std::vector<double> mst_edge_weights;
            for (const auto& edge_pair : MST_kruskal) {
                double weight = edge_list.at(edge_pair.first);
                current_kruskal_weight_sum += weight;
                mst_edge_weights.push_back(weight);
            }
            kruskal_weight_sum += current_kruskal_weight_sum;
            all_mst_edge_weights.insert(all_mst_edge_weights.end(), mst_edge_weights.begin(), mst_edge_weights.end());

        }


    } else if (dimension == 2) {
        all_mst_edge_weights.clear(); // Clear for each dimension
        for (int _ = 0; _ < numtrials; ++_) {
            CompleteGraph2D graph(numpoints);
            std::map<int, std::vector<std::pair<int, double>>> adj_list = graph.getAdjList();
            std::vector<int> vertices = graph.getVertices();

            auto prim_result_pair = prim_with_edge_weights(vertices, adj_list);
            double prim_weight = prim_result_pair.first.second;
            std::vector<double> mst_edge_weights = prim_result_pair.second;


            prim_weight_sum += prim_weight;
            all_mst_edge_weights.insert(all_mst_edge_weights.end(), mst_edge_weights.begin(), mst_edge_weights.end());
        }


    } else if (dimension == 3) {
        all_mst_edge_weights.clear(); // Clear for each dimension
        for (int _ = 0; _ < numtrials; ++_) {
            CompleteGraph3D graph(numpoints);
            std::map<int, std::vector<std::pair<int, double>>> adj_list = graph.getAdjList();
            std::vector<int> vertices = graph.getVertices();

            auto prim_result_pair = prim_with_edge_weights(vertices, adj_list);
            double prim_weight = prim_result_pair.first.second;
            std::vector<double> mst_edge_weights = prim_result_pair.second;


            prim_weight_sum += prim_weight;
            all_mst_edge_weights.insert(all_mst_edge_weights.end(), mst_edge_weights.begin(), mst_edge_weights.end());
        }

    } else if (dimension == 4) {
        all_mst_edge_weights.clear(); // Clear for each dimension
        for (int _ = 0; _ < numtrials; ++_) {
            CompleteGraph4D graph(numpoints);
            std::map<int, std::vector<std::pair<int, double>>> adj_list = graph.getAdjList();
            std::vector<int> vertices = graph.getVertices();

            auto prim_result_pair = prim_with_edge_weights(vertices, adj_list);
            double prim_weight = prim_result_pair.first.second;
            std::vector<double> mst_edge_weights = prim_result_pair.second;


            prim_weight_sum += prim_weight;
            all_mst_edge_weights.insert(all_mst_edge_weights.end(), mst_edge_weights.begin(), mst_edge_weights.end());
        }

    } else {
        return 0;
    }

    if (dimension >= 0 && dimension <= 4) {
        double avg_mst_weight = (dimension == 1) ? (kruskal_weight_sum / numtrials) : (prim_weight_sum / numtrials);
        std::cout << "Average MST weight: " << std::fixed << std::setprecision(5) << avg_mst_weight << " numpoints=" << numpoints << " numtrials=" << numtrials << " dimension=" << dimension << std::endl;

        std::sort(all_mst_edge_weights.begin(), all_mst_edge_weights.end());
        double p_threshold = 0.005;
        int kth_index = static_cast<int>((1.0 - p_threshold) * all_mst_edge_weights.size()) - 1;
        if (kth_index < 0) kth_index = 0;
        double kn_value = all_mst_edge_weights[kth_index];
        std::cout << "k(n) value (for p=" << p_threshold << "): " << std::fixed << std::setprecision(5) << kn_value << " for n=" << numpoints << std::endl;
    }


    return 0;
}