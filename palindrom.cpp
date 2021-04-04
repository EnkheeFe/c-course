#include<iostream>

using namespace std;

int main(){
	
	int n,m,rev=0;
	cin>>n; // 12321
	m=n;
	for(;n>0;n/=10){
		rev=rev*10+n%10; //2*10+1=21
		
	}if(m==rev){
		cout<<"yes";
	}else{
		cout<<"no";
	}
	
	
	

	
	return 0;
}
