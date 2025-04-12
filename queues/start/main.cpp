/* 
Write a basic array queue data structure showing basic functionalities
*/

#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    cout << "Queues: ";
    vector<string> queue;
    queue.push_back("A");
    queue.push_back("B");
    queue.push_back("C");
    cout << "Queue: ";
    for (int i = 0; i < queue.size(); i++) {
        cout << queue[i] << " ";
    }
    queue.erase(queue.begin());
    cout << "\nQueue after removing first element: ";
    for (int i = 0; i < queue.size(); i++) {
        cout << queue[i] << " ";
    }
    cout << endl;


    return 0;
}