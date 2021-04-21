#include<iostream>

using namespace std;

int main(){
		
		int size;
		
		cin>>size;
		
		
		for(int i=0; i<size; i++){
			for(int j=0; j<=i; j++){
				if( i==size-1 || j==0 || i==j){
					cout<<"*";
				}else{
					cout<<" ";
				}
				
			}
			
			cout<<endl;
			
			
		}
		
	
	
	
	
	
	
	
	
	
	
	
	
	return 0;
} 
