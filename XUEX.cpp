#include<iostream>

using namespace std;

int main(){
	
	int a,b,i,x;
	cin>>a>>b;
	for(i=1;i<=a && i<=b;i=i+1){
		if(a%i==0 && b%i==0){
			x=i;
		}	
	}cout<<x;
	
	
	
	
	
	
	return 0;
}

