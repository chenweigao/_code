#include <iostream>
#include <map>
#include <string>
#include <cctype>
#include <algorithm>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::remove_if;
using Map = std::map<std::string, std::size_t>;

auto count()
{
    Map counts;
    for (string w; cin >> w; ++counts[w])
        ;
    return counts;
}

auto strip(string& str) -> string const& {
    for(auto& ch: str) ch = tolower(ch);
    str.erase(remove_if(str.begin(), str.end(), ispunct), str.end());
    return str;
}

auto strip_and_count()
{
    Map counts;
    for(string w; cin >> w; ++counts[strip(w)]);
    return counts;

}

auto print(Map const &m)
{
    for (auto const &kv : m)
        cout << kv.first << ":" << kv.second << endl;
}

int main(int argc, char const *argv[])
{
    // print(count());
    print(strip_and_count());
    return 0;
}
