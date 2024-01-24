#include <iostream>
#include <fstream>
#include <cstring>

class Student {
private:
    int regNo;
    char name[50];
    float marks;
    char grade;

public:
    void acceptDetails() {
        std::cout << "Enter Registration Number: ";
        std::cin >> regNo;
        std::cin.ignore(); // clear buffer
        std::cout << "Enter Name: ";
        std::cin.getline(name, 50);
        std::cout << "Enter Marks: ";
        std::cin >> marks;
        calculateGrade();
    }

    void displayDetails() {
        std::cout << "\nRegistration Number: " << regNo << "\nName: " << name << "\nMarks: " << marks << "\nGrade: " << grade << "\n";
    }

    void calculateGrade() {
        if (marks >= 90) {
            grade = 'A';
        } else if (marks >= 80) {
            grade = 'B';
        } else if (marks >= 70) {
            grade = 'C';
        } else if (marks >= 60) {
            grade = 'D';
        } else {
            grade = 'F';
        }
    }

    void storeRecord() {
        std::ofstream outFile("student_records.dat", std::ios::binary | std::ios::app);
        outFile.write(reinterpret_cast<char*>(this), sizeof(*this));
        outFile.close();
    }

    static void displayRecords() {
        std::ifstream inFile("student_records.dat", std::ios::binary);
        if (!inFile.is_open()) {
            std::cout << "No records found!\n";
            return;
        }

        while (inFile.read(reinterpret_cast<char*>(new Student), sizeof(Student))) {
            Student* temp = new Student;
            temp->displayDetails();
            delete temp;
        }

        inFile.close();
    }
};

int main() {
    int choice;
    do {
        std::cout << "\n*** STUDENT REPORT CARD ***\n";
        std::cout << "1. Enter Student Details\n";
        std::cout << "2. Display Student Records\n";
        std::cout << "3. Exit\n";
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        switch (choice) {
            case 1: {
                Student student;
                student.acceptDetails();
                student.storeRecord();
                std::cout << "Student record added successfully!\n";
                break;
            }
            case 2:
                Student::displayRecords();
                break;
            case 3:
                std::cout << "Exiting program. Goodbye!\n";
                break;
            default:
                std::cout << "Invalid choice. Please try again.\n";
        }

    } while (choice != 3);

    return 0;
}
