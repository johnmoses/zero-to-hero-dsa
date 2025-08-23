// Custom Comparator - C++ Example

#include <iostream>
#include <vector>
#include <algorithm>

struct Student {
    std::string name;
    int grade;
};

bool cmp(const Student& a, const Student& b) {
    if (a.grade != b.grade)
        return a.grade > b.grade;
    return a.name < b.name;
}

int main() {
    std::vector<Student> students = {
        {"Alice", 85}, {"Bob", 92}, {"Charlie", 85}
    };

    std::sort(students.begin(), students.end(), cmp);

    for (const auto& student : students) {
        std::cout << student.name << " " << student.grade << std::endl;
    }

    return 0;
}
