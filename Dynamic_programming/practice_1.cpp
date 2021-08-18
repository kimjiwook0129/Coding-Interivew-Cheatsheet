#https:  // www.acmicpc.net/problem/1932

#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>

int main() {
    int n;
    std::cin >> n;
    int table[2][n];
    std::cin.ignore();
    for (int i = 0; i < n; ++i) {
        std::string S, T;
        int prev = (i - 1) % 2, cur = i % 2;
        getline(std::cin, S);
        std::stringstream X(S);
        int each_idx = 0;
        while (getline(X, T, ' ')) table[cur][each_idx++] = stoi(T);

        if (i == 0) continue;

        for (int j = 0; j < i + 1; ++j) {
            int left = j > 0 ? table[prev][j - 1] : 0;
            int right = j < i ? table[prev][j] : 0;
            table[cur][j] = table[cur][j] + (left > right ? left : right);
        }
    }
    int f_pos = (n - 1) % 2;
    std::cout << *std::max_element(table[f_pos], table[f_pos] + n) << std::endl;
}