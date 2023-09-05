# Week 2 Tutorial Answers

### Q1. What is a bit?
A bit is a single binary digit. A binary digit can only be one of 2 values, (0 or 1).

### Q2. What is a byte?
A byte is a sequence of 8 bits (8 binary digits). A byte can represent 256 unique values as there are $2^8 = 256$ unique sequences that can be made with 8 bits. 

### Q3. What is a file?
Just like how an integer can be made up of 4 bytes and a boolean can be made up of 1 byte, files are also instances of datatypes which can be made up of tens of thousand of bytes. These files represent special datatypes that humans agreed upon to make life convenient and standardised. This way, every computer knows how to interpret some special combination of bytes as a pdf for example.

### Q4. What is a directory?
A directory is a folder where files can be saved. 

### Q5. What is a variable? What does it mean to declare a variable? What does it mean to initialise a variable? Which of these steps are required?
A variable is a chunk of memory that can be assigned a name and a value. 
Declaring a variable is specifying how much storage should be set aside for the variable.
Initialising the variable is to fill up the storage that was set aside during declaration.

### Q6. C is a typed language. What does this mean? Why is this useful?
C is a statistically typed language, meaning the users will have to define the data type of a variable in the program. 
If data types are defined prior, the compiler can easily check for errors in the code and hence compile quickly.

### Q7. What are the types of variables that we've seen so far and what do they represent?
1. int : Integer which uses 4 bytes.
2. long : Integer which uses 8 bytes, allowing it to store larger integers.
3. float : decimal which uses 4 bytes.
4. double : decimal which uses 8 bytes, allowing it to store larger and/or more precise numbers.
5. char : 1 byte of data that can be used either as an integer or an ASCII character

### Q8. What is the difference between declaring variable and using a ```#define```?
Simply declaring a variable allows the variable to be mutated (if the variable is mutable to begin with). 
With ```#define MAX 20```, the word ```MAX``` will always be replaced with the value 25, allowing for programmers to use a constant. 

### Q9. Which of the following are valid variable names in C? If they are valid, would they be a good variable name?
```
THX1138 (valid, but a bad name as it is not descriptive)
2for1 (invalid, should not start with a number)
mr_bean (valid)
my space (invalid, should not have spaces)
event_counter (valid)
^oo^ (invalid, should not start with weird characters)
_MEMLIMIT (valid, used for private variables)
return
```

### Q10. What is wrong with each of the following fragments of code:
1. 
``` c
// wrong
int num1 = 3;
int num2 = 8;
printf("The numbers are %d\n", num1, num2);
```

There needs to be 2 seperate ```%d``` as 2 different integers are to be printed. 

2. 
``` c
// wrong
int num1 = 3;
int num2 = 8;
printf("The numbers are %d %d\n", num1);
```
The variable num2 has not been added to printf. 

3. 
``` c
// wrong
double num1 = 3;
int num2 = 8;
printf("The numbers are %d %d\n", num1, num2);
```
num1 is a double but in printf, the datatype of num1 has been indicated as decimal using ```%d``` placeholder

```c
// correct
printf("The numbers are %d and %d\n", num1, num2);
```

### Q11. We can use the ```scanf``` function to read input from the terminal.
``` c
int num;
printf("Enter a number: ");
scanf("%d", &num);
printf("Your number was %d\n", num);
```
Suppose when using the above code, the user types invalid input such as "hello". What will the program output?

The program will output ```Your number was 1```. Any string input gets casted into an integer 1. 


### Q12. What is the syntax of C if statements? What is the role of if statements in programs?

``` c
if (predicate_1)
{
    // action A
}
else if (predicate_2)
{
    // action B
}
else
{
    // action C
}
```
if statements provide a form of control flow. They are used to control the flow of the program based on conditions. 






### Q13. Can you then write some simple code using if/else statements in C that decides if a year is a Leap Year?

```c
int main(void)
{
    printf("Input a year: ");
    int year;
    scanf("%d", &year);

    if (year % 400 == 0)
    {
        printf("%d is a Leap year", year);
    }
    else if (year % 100 == 0)
    {
        printf("%d is a not a Leap year", year);
    }
    else if (year % 4 == 0)
    {
        printf("%d is a Leap year", year);
    }
    else
    {
        printf("%d is a not a Leap year", year);        
    }
}
```

### Q14. What does precedence of an operator mean? Make the precedence explicit in the following expressions by adding parentheses and evalute the expressions:

Precedence of an operator refers to the priority given when taking operatoins in order. 
```
3 + (5 * 10) - 12
3 + (15 % 10) - (12 / 2)
```

### Q15. Determine the value of each expression and sub-expression:
```c
1 / 2 * 500 = 0

1 / 2.0 * 500 = 250.0

(17 / 5) * 5 + (17 % 5) = 17

(12 - 17) % 6 - 4 = -9

10 / (1 / 2) = warning: division by zero is undefined
```

