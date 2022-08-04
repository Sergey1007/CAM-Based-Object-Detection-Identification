#include <iostream>
using namespace std;
#include <string>
#include <stdlib.h>
#include <fstream>
#include <dos.h>
#include <windows.h>
#include "SerialPort.h"

char output[MAX_DATA_LENGTH];
char* port="\\\\.\\COM5";
char incoming[MAX_DATA_LENGTH];



int main() {
	SerialPort arduino(port);
	string path="data.txt";
	ifstream file;

	while(1)
	{
		string str="";
		file.open(path);
		//if (file.is_open()) cout<<"file is open"<<endl;

		string temp="";
		while(!file.eof())
			{
				file>>temp;

				if (temp!="done"&&temp!="close") str=str+temp+' ';
				else str=temp;
			}

		if (str=="close")
			{break; }
		//if (str!="done")  str.pop_back();



		if (str=="done"||str.length()==1)
			{
				//cout<<"empty string"<<endl;;
				file.close();
				Sleep(100);
				continue;
			}


		file.close();

		cout<<str<<endl;
		char *charArray=new char[str.size()+1];
		copy(str.begin(),str.end(),charArray);
		charArray[str.size()]='\0';
		arduino.writeSerialPort(charArray,MAX_DATA_LENGTH);
		arduino.readSerialPort(output,MAX_DATA_LENGTH);
		cout<<output;
		delete [] charArray;


		cout<<"unlock"<<endl;
		ofstream wfile;
		wfile.open("data.txt");
		wfile<<"done";
		wfile.close();
		Sleep(100);

	}
	cout<<"i'm here"<<endl;
	file.close();

	return 0;
}
