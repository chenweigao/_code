#include <vector>
#include <iostream>
#include <string>
#include <map>

using std::cin;
using std::cout;
using std::map;
using std::string;
using std::vector;
using Families = map<string, vector<string>>;

auto make_families()
{
    Families families;
    for (string ln; cout << "Last Name: \n", cin >> ln && ln != "@q";)
        for (string cn; cout << "Children's name: \n", cin >> cn && cn != "@q";)
            families[ln].push_back(cn);
    return families;
}

auto print(Families const &families)
{
    for (auto const &family : families)
    {
        cout << family.first << ":\n";
        for(auto &child : family.second)
            cout << child << " ";
        cout << "\n";
    }
}

int main() {
    print(make_families());
    return 0;
}