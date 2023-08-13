#include <stdio.h>
#include <string.h>
#include <stdbool.h>

// The maximum length of special token keys, chosen based on the longest keys: Three, Seven, Eight
#define SPECIALS_MAX_KEY 6UL

// Define a structure to encapsulate special tokens and their corresponding values
typedef struct {
    const char k[SPECIALS_MAX_KEY]; // Key representing a special token
    char v;                         // Corresponding value for the special token
} specials_t;

// Determine the size of the specials array based on the number of elements
#define SPECIALS_SIZE (sizeof(specials) / sizeof(specials[0]))

// An array of special tokens and their associated values
const specials_t specials[] = {
    { .k = "One",   .v = '1' },
    { .k = "Two",   .v = '2' },
    { .k = "Three", .v = '3' },
    { .k = "Four",  .v = '4' },
    { .k = "Five",  .v = '5' },
    { .k = "Six",   .v = '6' },
    { .k = "Seven", .v = '7' },
    { .k = "Eight", .v = '8' },
    { .k = "Nine",  .v = '9' },
    { .k = "Zero",  .v = '0' },
    { .k = "Dash",  .v = '-' }
};

// Delimiter employed to tokenize the input response
#define DELIMITER " "

// Function dedicated to discerning a special token and extracting its corresponding value
static inline bool find_special_token(const char* token, char* output) {
    for (size_t i = 0; i < SPECIALS_SIZE; i++) {
        // Check if the current token matches any of the defined special token keys
        if (strncmp(token, specials[i].k, SPECIALS_MAX_KEY) == 0) {
            *output = specials[i].v; // Assign the associated value to the output
            return true;             // Indicate successful identification of a special token
        }
    }
    return false; // No special token found
}

// Main execution point
int main(void)
{
    // Input response comprising a fusion of special tokens and conventional words
    char response[] = "Whiskey Hotel Four Tango Dash Alpha Romeo Three Dash"
                      " Yankee Oscar Uniform Dash Sierra One November Kilo"
                      " India November Golf Dash Four Bravo Zero Uniform Seven";

    // Tokenize the input response using the designated delimiter
    char* token = strtok(response, DELIMITER);
    while (token != NULL) {
        char special_token = { 0 }; // Placeholder for the special token's value

        // Identify if the current token corresponds to a special token, if so, print its value
        if (find_special_token(token, &special_token)) {
            putchar(special_token);
        } else {
            // In the absence of a special token match, print the initial character of the token
            putchar(token[0]);
        }

        token = strtok(NULL, DELIMITER); // Move to the next token
    }
    putchar('\n'); // Print a newline character to finalize the output

    return 0; // Indicate successful program execution
}
