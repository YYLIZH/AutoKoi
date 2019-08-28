#include <Windows.h>
#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    int ClickWait,AutoWait,ProgramWait;
    ClickWait = 25;
    AutoWait = 50;
    SetConsoleTitleA("Auto Koi");
    cout << "Please point your cursor to the target\n";
    cout << "Press Enter to continue the program......";
    cin.get();
    POINT pt;
    GetCursorPos(&pt);
    cout << "Please when will the program start(in second): 0 means run the code immediately    ";
    cin >> ProgramWait;
    Sleep(ProgramWait * 1000);
    while(true){
        for (int i = 0; i < 5;i++){
            for (int j = 0; j < 4; j++)
            {
                SetCursorPos(pt.x, pt.y);
                mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0);
                mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0);
                Sleep(ClickWait * 1000);
            }
        }
        Sleep(AutoWait * 60 * 1000);
    }
    return 0;
}