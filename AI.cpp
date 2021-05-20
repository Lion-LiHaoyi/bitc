//本程序用于执行训练程序
#include <windows.h>
#include <iostream>
#include <fstream>
using namespace std;
int main(){
	int t;
	cout <<
	        "Enter the number of training sessions";
	cin >> t;
	cout << "Done";
	for (int i = 0; i < t; i++) {
		cout << i << endl;
		system("bitc.py");
	}
}
