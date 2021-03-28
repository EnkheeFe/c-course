#include<iostream>
using namespace std;

int main() {
	
	
	int a,b,c,d;
	
	cin>>a;
	
	b=a/100;
	c=a%10;
	d=(a%100-a%10)/10;
	cout<<b+c+d;
	
	

	return 0;
}
