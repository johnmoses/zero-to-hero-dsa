// Custom Comparator - Java Example

import java.util.*;

class Student {
    String name;
    int grade;
    Student(String name, int grade) {
        this.name = name;
        this.grade = grade;
    }
    public String toString() {
        return name + " " + grade;
    }
}

class CustomComparator {
    public static void main(String[] args) {
        List<Student> students = Arrays.asList(
            new Student("Alice", 85),
            new Student("Bob", 92),
            new Student("Charlie", 85)
        );

        students.sort(Comparator.comparingInt((Student s) -> -s.grade).thenComparing(s -> s.name));

        for (Student s : students) {
            System.out.println(s);
        }
    }
}
