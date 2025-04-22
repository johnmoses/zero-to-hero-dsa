/* 
Hashes

Create a basic hash table to store adn access fruits based on their first letters.
*/
#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    unordered_map<char, string> fruits;
    fruits['a'] = "apple";
    fruits['b'] = "banana";
    fruits['c'] = "cherry";

    cout << "Fruits starting with 'a': " << fruits['a'] << endl;
    cout << "Fruits starting with 'b': " << fruits['b'] << endl;
    cout << "Fruits starting with 'c': " << fruits['c'] << endl;

    return 0;
}

