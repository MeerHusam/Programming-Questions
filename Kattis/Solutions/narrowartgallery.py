#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1000000;

vector<vector<vector<int>>> dp;
vector<vector<int>> gallery;

const int LEFT = 0;
const int RIGHT = 1;

int min_val(initializer_list<int> values) {
    return *min_element(values.begin(), values.end());
}

int f(int k, int r, int c);

int f(int k, int r) {
    return min_val({f(k, r, LEFT), f(k, r, RIGHT)});
}

int f(int k, int r, int c) {
    if (k == 0) {
        return 0;
    }
    if (r < 0) {
        return INF;
    }
    if (dp[k][r][c] != -1) {
        return dp[k][r][c];
    }
    int roomValue = gallery[r][c];
    return dp[k][r][c] = min_val({f(k - 1, r - 1, c) + roomValue, f(k, r - 1)});
}


int main() {
    while (true) {
        int N, K;
        cin >> N >> K;

        if (N == 0 && K == 0) break;

        gallery.assign(N, vector<int>(2));
        dp.assign(K + 1, vector<vector<int>>(N, vector<int>(2, -1)));

        int sum = 0;
        for (int i = 0; i < N; i++) {
            int index = N - i - 1;
            cin >> gallery[index][LEFT] >> gallery[index][RIGHT];
            sum += gallery[index][LEFT] + gallery[index][RIGHT];
        }

        cout << sum - f(K, N - 1) << endl;
    }

    return 0;
}