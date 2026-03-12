#include <iostream>
using namespace std;
int main()
{
    int number;
    int sum;
    for (int count=1;count<=5;count++) {
        cout << "input your number "<<count<<" = ";
        cin >> number;
        sum += number;
        
    }
    cout << "sum = " << sum <<endl;

}   