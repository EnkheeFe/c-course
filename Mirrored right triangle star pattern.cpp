#include<iostream>

using namespace std;

int main(){
		
		int size;
		
		cin>>size;
		
		
		for(int i=0; i<size; i++){
			
			for(int j=i; j<size-1; j++){
					
					cout<<" ";
				
			}
				for(int j=0 ;j<=i ; j++){
					
					cout<<"*";
				}
					cout<<endl;
			
			
		}
		
	
	
	
	
	
	
	
	
	
	
	
	
	return 0;
} 
