#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);

    int n, m;
    cin >> n >> m;

    vector<int> aVec(n);
    for (int i = 0; i < n; i++)
    {
        cin >> aVec.at(i);
    }

    int max = 0;
    int cnt = 0;
    sort(aVec.begin(), aVec.end());
    for (int x : aVec)
    {
        cnt = 0;
        for (int y : aVec)
        {
            if (x > y)
                continue;
            if (y >= x + m)
                break;
            // if (x <= y && y < x + m)
            cnt++;
        }
        if (max < cnt)
            max = cnt;
    }

    cout << max << endl;
}
