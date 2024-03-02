#include <iostream>
#include <set>
#include <vector>

using namespace std;

int main()
{
    long long int n, t;
    cin >> n >> t;

    vector<long long int> points;
    for (long long int i = 1; i <= n; ++i)
    {
        points.push_back(0);
    }

    for (long long int i = 0; i < t; ++i)
    {
        long long int a, b;
        cin >> a >> b;
        points.at(a - 1) += b;

        set<long long int> points_set;
        for (long long int i = 0; i< points.size(); ++i)
        {
            points_set.insert(points.at(i));
        }

        cout << points_set.size() << endl;
    }

    return 0;
}
