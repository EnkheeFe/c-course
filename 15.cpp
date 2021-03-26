#include<iostream>

using namespace std;

int main(){
	
	int num,pro,lastdigit ;
	pro=1;
	cin>>num;
	
	for(;num!=0;){
	lastdigit=num%10;
	pro=pro*lastdigit;
	num=num/10;
	
	}cout<<pro;
	
	
	
	
	
	return 0;
}
