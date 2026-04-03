#include <bits/stdc++.h>
using namespace std;

vector<int> divineness(int n, long long m) {
    long long max_sum = 1LL * n * (n + 1) / 2;
    if (m < n || m > max_sum) 
        return {-1};

    long long total = 0;
    int k = n;
    vector<int> L;
    L.reserve(n);

    // 1) Greedily take k, k-1, ... until we risk overshooting m
    while (total + k <= m) {
        total += k;
        L.push_back(k);
        --k;
    }

    long long add_needed = m - total;
    int min_add = n - (int)L.size();
    if (add_needed < min_add) {
        L.back() += int(add_needed - min_add);
    }

    // 2) Mark used labels in a vector<char> (1 byte each)
    vector<char> used(n + 1, 0);
    for (int x : L) 
        used[x] = 1;

    // 3) Append the missing labels in [1..n]
    for (int i = 1; i <= n; ++i) {
        if (!used[i]) 
            L.push_back(i);
    }

    return L;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n;
        long long m;
        cin >> n >> m;

        auto res = divineness(n, m);
        if (res.size() == 1 && res[0] == -1) {
            cout << -1 << '\n';
            continue;
        }

        // Print root
        cout << res[0] << '\n';
        // Print the "path" edges
        for (int i = 0; i + 1 < (int)res.size(); ++i) {
            cout << res[i] << ' ' << res[i+1] << '\n';
        }
    }
    return 0;
}
