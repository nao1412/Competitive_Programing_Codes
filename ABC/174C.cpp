#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); ++i)

int main() {
  int k;
  cin >> k;
  int cnt = 1;
  int seven = 7;
  bool flag = true;
  if (k % 2 == 0) {
    cout << -1 << endl;
    return 0;
  }
  while (flag)
  {
    if (seven % k == 0) {
      flag = false;
    }
    else {
      seven = seven * 10 + 7;
      cnt++;
    }
  }
  cout << cnt << endl;
}