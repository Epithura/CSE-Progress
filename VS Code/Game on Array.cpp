#include <bits/stdc++.h>
using namespace std;

pair<long long, long long> ScoreBoard(const vector<int>& arr) {
    unordered_map<int, long long> freq;
    for (int x : arr) freq[x]++;   // count frequencies

    // move into vector for sorting
    vector<pair<int, long long>> L(freq.begin(), freq.end());

    // sort by frequency (ascending)
    sort(L.begin(), L.end(), [](auto &a, auto &b) {
        return a.second < b.second;
    });

    long long Alice = 0, Bob = 0;
    string chance = "Beta";

    while (!L.empty()) {
        auto [key, count] = L.back();  // highest frequency
        L.pop_back();

        long long base = count * (key / 2);

        Alice += base;
        Bob += base;

        if (key % 2 == 1) { // odd key
            if (chance == "Alpha") {
                Alice += count;
                chance = "Beta";
            } else {
                Bob += count;
                chance = "Alpha";
            }
        }
    }
    return {Bob, Alice};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; 
    cin >> t;
    while (t--) {
        int n; 
        cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < n; i++) cin >> arr[i];

        auto [Bob, Alice] = ScoreBoard(arr);
        cout << Bob << " " << Alice << "\n";
    }
    return 0;
}
