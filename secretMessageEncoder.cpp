// encodePixelMessage.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;


int main()

{
	string line;
	cout << "Please enter the code word in binary.";
	string wordData;
	cin >> wordData;
	//string file;
	//cout << "Please enter the name of the file that contains the pixels that the message will be encoded in.";
	//cin >> file;
	ifstream pixelData("pixelList.txt");
	fstream encodedMessage("encodedMessage.txt");

	if (pixelData && encodedMessage) {
		cout << "The files are open." << endl;
	}
	else {
		cout << "The files failed to open." << endl;
		return EXIT_FAILURE;
	}

	int i = 0;

	while (getline(pixelData, line) && i < wordData.length()) {

		if (wordData[i] == '0') {
			line[3 + (2 * (i % 3))] = '0';
			encodedMessage << line << "\n";
		}
		if (wordData[i] == '1') {
			line[3 + (2 * (i % 3))] = '1';
			encodedMessage << line << "\n";
		}

		i++;

	}

	// Check if word was encoded correctly
	
	i = 0;
	int amountCorrect = 0;
	encodedMessage.close();
	encodedMessage.open("encodedMessage.txt");

	while (getline(encodedMessage, line) && i < wordData.length()) {

		if (wordData[i] == line[3 + (2 * (i % 3))]) {
			amountCorrect++;
		}
		
		i++;

	}

	if (amountCorrect == wordData.length())  {
		cout << "The word was encoded correctly." << endl;
	}
	else {
		cout << "The word was not encoded correctly." << endl;
		cout << amountCorrect;
	}
	
	encodedMessage.close();
	pixelData.close();

}
			