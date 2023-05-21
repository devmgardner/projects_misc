#include <iostream>
#include <string>

int main() {

    double number;
    std::string name;
    std::cout << "enter an integer\n";
    std::cin >> number;
    std::cout << "enter your name\n";
    std::cin >> name;
    std::cout << "user " << name << " entered number " << number << "\n";
    system("pause");

}