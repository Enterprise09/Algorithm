#include <algorithm>
#include <iostream>
using namespace std;

int main() {
  int n, arr[9999];
  int result = 0, ctr = 0;
  cin >> n;

  // cin은 split 따위를 쓸필요가 없다.
  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }

  sort(arr, arr + n); // ASC

  for (int i = 0; i < n; i++) {
    ctr++;
    if (ctr >= arr[i]) {
      result++;
      ctr = 0;
    }
  }

  cout << result << endl;
}