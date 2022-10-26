#include <bits/stdc++.h>
using namespace std;

string str;
vector<char> result;
int ctr = 0;

int main(void) {
  cin >> str;
  
  // C언어의 경우에는 Python과 같은 list 형식이 아니기 때문에 다른 방법으로 구현   
  for (int i = 0; i < str.size(); i++) {
    if (isalpha(str[i])) {
      result.push_back(str[i]);
    }
    else {
      // 숫자일 경우 아스키 코드를 빼서 숫자로 만든다. (형변환)
      ctr += str[i] - '0';
    }
  }
  sort(result.begin(), result.end());
  for (int i = 0; i < result.size(); i++) {
    cout << result[i];
  }

  if (ctr != 0) {
    cout << ctr;
  }
  cout << '\n';
}