#include <iostream>
#include <vector>
#include <regex>

using namespace std;

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int n, q;
    cin >> n >> q;

    string s;
    cin >> s;

    vector<pair<int, int>> ranges;
    for (int i = 0; i < q; ++i) {
        int l, r;
        cin >> l >> r;
        ranges.emplace_back(l, r);
    }

    regex pat("(?=(.)\\1)");

    for (const auto& range : ranges) {
        int l = range.first;
        int r = range.second;

        string substr = s.substr(l - 1, r - l + 1);
        sregex_iterator it(substr.begin(), substr.end(), pat);
        sregex_iterator end;

        int cnt = distance(it, end);
        cout << cnt << endl;
    }

    return 0;
}
