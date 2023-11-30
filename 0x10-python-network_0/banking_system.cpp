#include <iostream>
#include <fstream>
#include <iomanip>

class Account {
private:
    int accountNumber;
    std::string name;
    double deposit;
    double withdraw;
    std::string accountType;

public:
    // Constructor
    Account() : accountNumber(0), name(""), deposit(0), withdraw(0), accountType("") {}

    // Member functions
    void createAccount();
    void displayAccount() const;
    void modifyAccount();
    void depositAmount();
    void withdrawAmount();
    void deleteAccount();

    // File handling functions
    void writeAccount();
    void readAccount(int accNum);
};

void Account::createAccount() {
    std::cout << "Enter Account Number: ";
    std::cin >> accountNumber;
    std::cin.ignore(); // Clear buffer
    std::cout << "Enter Name: ";
    std::getline(std::cin, name);
    std::cout << "Enter Account Type (Savings/Checking): ";
    std::cin >> accountType;
    std::cout << "Enter Initial Deposit: $";
    std::cin >> deposit;

    std::cout << "Account Created Successfully!\n";
}

void Account::displayAccount() const {
    std::cout << std::setw(15) << "Account Number: " << accountNumber << std::endl;
    std::cout << std::setw(15) << "Name: " << name << std::endl;
    std::cout << std::setw(15) << "Account Type: " << accountType << std::endl;
    std::cout << std::setw(15) << "Balance: $" << deposit - withdraw << std::endl;
}

void Account::modifyAccount() {
    std::cout << "Enter New Name: ";
    std::cin.ignore(); // Clear buffer
    std::getline(std::cin, name);
    std::cout << "Enter New Account Type (Savings/Checking): ";
    std::cin >> accountType;

    std::cout << "Account Modified Successfully!\n";
}

void Account::depositAmount() {
    double amount;
    std::cout << "Enter Deposit Amount: $";
    std::cin >> amount;
    deposit += amount;

    std::cout << "Amount Deposited Successfully!\n";
}

void Account::withdrawAmount() {
    double amount;
    std::cout << "Enter Withdrawal Amount: $";
    std::cin >> amount;
    
    if (amount > deposit - withdraw) {
        std::cout << "Insufficient Funds!\n";
    } else {
        withdraw += amount;
        std::cout << "Amount Withdrawn Successfully!\n";
    }
}

void Account::deleteAccount() {
    accountNumber = 0;
    name = "";
    deposit = 0;
    withdraw = 0;
    accountType = "";

    std::cout << "Account Deleted Successfully!\n";
}

void Account::writeAccount() {
    std::ofstream outFile;
    outFile.open("bankData.dat", std::ios::binary | std::ios::app);
    outFile.write(reinterpret_cast<char*>(this), sizeof(Account));
    outFile.close();
}

void Account::readAccount(int accNum) {
    std::ifstream inFile;
    inFile.open("bankData.dat", std::ios::binary);
    if (!inFile) {
        std::cerr << "File could not be opened!\n";
        return;
    }

    bool found = false;
    while (inFile.read(reinterpret_cast<char*>(this), sizeof(Account))) {
        if (accountNumber == accNum) {
            found = true;
            break;
        }
    }

    inFile.close();

    if (!found) {
        std::cerr << "Account not found!\n";
        accountNumber = 0; // Reset accountNumber if not found
    }
}

int main() {
    Account acc;
    int choice, accNum;

    do {
        std::cout << "\n======= BANKING SYSTEM =======\n";
        std::cout << "1. Create Account\n";
        std::cout << "2. Display Account\n";
        std::cout << "3. Modify Account\n";
        std::cout << "4. Deposit\n";
        std::cout << "5. Withdraw\n";
        std::cout << "6. Delete Account\n";
        std::cout << "7. Quit\n";
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        switch (choice) {
            case 1:
                acc.createAccount();
                acc.writeAccount();
                break;
            case 2:
                std::cout << "Enter Account Number: ";
                std::cin >> accNum;
                acc.readAccount(accNum);
                acc.displayAccount();
                break;
            case 3:
                std::cout << "Enter Account Number: ";
                std::cin >> accNum;
                acc.readAccount(accNum);
                acc.modifyAccount();
                break;
            case 4:
                std::cout << "Enter Account Number: ";
                std::cin >> accNum;
                acc.readAccount(accNum);
                acc.depositAmount();
                acc.writeAccount();
                break;
            case 5:
                std::cout << "Enter Account Number: ";
                std::cin >> accNum;
                acc.readAccount(accNum);
                acc.withdrawAmount();
                acc.writeAccount();
                break;
            case 6:
                std::cout << "Enter Account Number: ";
                std::cin >> accNum;
                acc.readAccount(accNum);
                acc.deleteAccount();
                acc.writeAccount(); // Write updated account data to file
                break;
            case 7:
                std::cout << "Exiting the program. Goodbye!\n";
                break;
            default:
                std::cout << "Invalid choice! Please enter a valid option.\n";
        }
    } while (choice != 7);

    return 0;
}

