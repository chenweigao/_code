#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include <iomanip>
using namespace std;

const int MAXN = 1024;
vector<string> LineWords[MAXN];
size_t WordLen[MAXN], MaxWords, LineCnt;
int main() {
    string line, word;
    MaxWords = 0;
    LineCnt = 0;
    fill_n(WordLen, MAXN, 0);
    while (getline(cin, line)) {
        stringstream ss(line);
        size_t wi = 0;
        while (ss >> word) {
            WordLen[wi] = max(WordLen[wi], word.size());
            wi++;
            LineWords[LineCnt].push_back(word);
        }
        MaxWords = max(MaxWords, wi);
        LineCnt++;
//        cout << line << endl;
    }
        for (int i = 0; i < LineCnt; ++i) {
            const auto& ws = LineWords[i];
            for (int j = 0; j < ws.size(); j++) {
                cout << left << setw(j < ws.size() - 1 ? WordLen[j] + 1 : 0) << ws[j];
            }
            cout << endl;
    }
    return 0;
}
