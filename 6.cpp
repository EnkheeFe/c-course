#include<iostream>
using namespace std;

int main(){
	
	int x,y;
	string X="Length x:";
	cout<<X;
	cin>>x;
	cout<<"Breadth y:";
	cin>>y;
	x=2*(x+y);
	cout<<"Perimeter="<<x;
	return 0;
}
