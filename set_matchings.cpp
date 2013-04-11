#include<iostream>
#include<fstream>
using namespace std;

int main(int argc, char *argv[]) {
    fstream f("settings.py", ios::out);
    f<<"NUM_MATCHINGS = "<<argv[1]<<endl;
    f.close();
    return 0;
}
