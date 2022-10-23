#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

int main() {
  /*   code for check string().find() return value
    string str = "helloasdf";
    if(str.find("3") == string::npos){
      cout << "NPOS" << endl;
    }else{
      cout << str.find("3") << endl;
    }
  */
  int h, m, s, n;
  int ctr = 0;

  cin >> n;

  for (h = 0; h < n + 1; h++) {
    for (m = 0; m < 60; m++) {
      for (s = 0; s < 60; s++) {
        string str =
            to_string(h) + "시 " + to_string(m) + "분 " + to_string(s) + "초";
        if (str.find("3") != string::npos) {
          ctr++;
          cout << str << endl;
        }
      }
    }
  }
  cout << ctr << endl;
}