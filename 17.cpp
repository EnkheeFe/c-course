#include<iostream>

using namespace std;

int main(){
	
	int n,num,rev=0 ;
	
	cin>>n;
	num=n;
	for(;n!=0;){
	
	rev=(rev*10)+(n%10);
	n/=10;
	
	} if(rev==num){
		cout<<num<<" is palindrome number";
	}else{
		cout<<num<<" is not palindrome number";
	}
	
	
	
	
	
	return 0;
}
