#include "GraphGenerators.h"

#include <random>

namespace GraphGenerators {

    double generate_random_weight() {
        static std::random_device rd;
        static std::mt19937 gen(rd());
        static std::uniform_real_distribution<> dis(0.0, 1.0);
        return dis(gen);
    }

    CompleteGraph::CompleteGraph(int n_in) : n(n_in) {
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                double edge_val = generate_random_weight();
                if (edge_val < 20.0 / n) {
                    adj_list[{i, j}] = generate_random_weight();
                }
            }
        }
    }

    std::map<std::pair<int, int>, double> CompleteGraph::getAdjList() {
        return adj_list;
    }

    HCubeGraph::HCubeGraph(int n_in) : n(n_in) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (((i - j) & (i - j - 1)) == 0 && i - j > 0) {
                    double value = generate_random_weight();
                    if (value < 0.0001 * n + 0.284) {
                        adj_list[{j, i}] = value;
                    }
                }
            }
        }
    }

    std::map<std::pair<int, int>, double> HCubeGraph::getAdjList() {
        return adj_list;
    }

    CompleteGraph2D::CompleteGraph2D(int n_in) : n(n_in) {
        std::vector<std::pair<double, double>> points;
        for (int i = 0; i < n; ++i) {
            points.push_back({generate_random_weight(), generate_random_weight()});
        }

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i != j && i < j) {
                    double dist = std::pow(points[i].first - points[j].first, 2) +
                                  std::pow(points[i].second - points[j].second, 2);
                    dist = std::sqrt(dist);
                    if (dist < 0.0003 * n + 0.131) {
                        adj_list[{i, j}] = dist;
                    }
                }
            }
        }
    }

    std::map<std::pair<int, int>, double> CompleteGraph2D::getAdjList() {
        return adj_list;
    }

    CompleteGraph3D::CompleteGraph3D(int n_in) : n(n_in) {
        std::vector<std::tuple<double, double, double>> points;
        for (int i = 0; i < n; ++i) {
            points.push_back({generate_random_weight(), generate_random_weight(), generate_random_weight()});
        }

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i != j && i < j) {
                    double dist = std::pow(std::get<0>(points[i]) - std::get<0>(points[j]), 2) +
                                  std::pow(std::get<1>(points[i]) - std::get<1>(points[j]), 2) +
                                  std::pow(std::get<2>(points[i]) - std::get<2>(points[j]), 2);
                    dist = std::sqrt(dist);

                    if (dist < 0.0002 * n + 0.131) {
                        adj_list[{j, i}] = dist;
                    }
                }
            }
        }
    }

    std::map<std::pair<int, int>, double> CompleteGraph3D::getAdjList() {
        return adj_list;
    }

    CompleteGraph4D::CompleteGraph4D(int n_in) : n(n_in) {
        std::vector<std::tuple<double, double, double, double>> points;
        for (int i = 0; i < n; ++i) {
            points.push_back({generate_random_weight(), generate_random_weight(), generate_random_weight(),
                             generate_random_weight()});
        }

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i != j && i < j) {
                    double dist = std::pow(std::get<0>(points[i]) - std::get<0>(points[j]), 2) +
                                  std::pow(std::get<1>(points[i]) - std::get<1>(points[j]), 2) +
                                  std::pow(std::get<2>(points[i]) - std::get<2>(points[j]), 2) +
                                  std::pow(std::get<3>(points[i]) - std::get<3>(points[j]), 2);
                    dist = std::sqrt(dist);

                    if (dist < 0.0002 * n + 0.135) {
                        adj_list[{j, i}] = dist;
                    }
                }
            }
        }
    }

    std::map<std::pair<int, int>, double> CompleteGraph4D::getAdjList() {
        return adj_list;
    }
} // namespace GraphGenerators