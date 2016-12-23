##  Code Conventions

* **Class Name** starts with *uppercase* and every new word is *capitalized*
  i.e *"Vertex, NewClass, ..."*.
* **Function Name** starts with *lowercase* and ever new word is *capitalized*
  i.e *"foo, fooName, ..."*.
* **Comments:** You must write a **description** before defining a *Class* or
  a *Function*.
* **For Allah** You have to write a *comment line* before every line of code
  you write.
  
    **Function Example:**
    ```python
    def fooWord ( argu1, argu2, ... ):
    '''
        * Describe the arguments.
        * Describe what fooWord() does.
        * You Must put # End fooWord() at the end of the function.
    '''
        # Comment line for the next line of code
        print "Write your code"
        .
        .
        .
    # End fooWord() 
    ```
    
    **Class Example:**
    ```python
    class ClassName:
    '''
        * Class Description.
        * put # End ClassName at the end of the class.
    '''
        # Class Member Definitions
        .
        .
        .
    # End ClassName
    ```
* Always write a *multi-line comment* to test you code.
* Do **NOT** push until you're sure the code is well-tested.

> This helps everyone to read and maintain the code **even when you're maintain someone else code**

## Game Rules:
* It is a *two-player* game.
* The game starts with an Integer number.
* Both players should subtract X from the starting number.
* **X is non-zero positive square integer less than the current number.**
* *Last person* who can make a subtraction wins.
