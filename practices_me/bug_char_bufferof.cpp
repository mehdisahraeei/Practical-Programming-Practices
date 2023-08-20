#include <iostream>
#include <cstring>
#include <cstdlib> // For malloc and free

class BugChar {
public:


    //bugs about buffer overflow strcat and strcpy


    void concat_str() {
        char dst[20] = "one etc ..........";
        char source[3] = "-"; // Initialize the source string with "-"
        strcat(source, dst);  // Concatenate dst to source
        std::cout << "Concatenated string: " << dst << std::endl;
    }


    void copy_arr() {
        char dst[20];
        memset(dst, '1', 18); // Fill dst with 18 repetitions of ASCII value 1
        dst[18] = 'z'; // Null-terminate the string
        strcat(dst, " tam"); // Concatenate "end" to dst



        char *source = (char*)malloc(3); // Allocate memory for source
        strcpy(source, dst); // Copy the content of dst to source
        std::cout << "dst: " << dst << "\a" << std::endl; // Produces a beep sound
        free(source); // Free the allocated memory
    }

};

int main() {
    BugChar obj;
    obj.concat_str(); // Call the concat_str function
    std::cout << "\n";
    obj.copy_arr(); // Call the copy_arr function

    return 0;
}

