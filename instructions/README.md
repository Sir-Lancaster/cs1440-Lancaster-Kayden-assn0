# CS 1440 Assignment 0: Demo Project - Instructions

## Description

This assignment eases you into the DuckieCorp workflow by introducing you to the Unix command line interface and to the Git version control system.  You will create a clone of this repository and submit it under your account on GitLab.  You will follow the same procedure for all assignments in this course.

This repository also contains a partially-working Python program, along with documentation.  This is an introduction to DuckieCorp coding and documentation standards.  You will fix a bug in this program and complete the documentation.  The solution to the bug is revealed as you work through lesson `6-git.sh` of the Shell Tutor.  If you try to fix the bug on your own, you're doing it wrong!


## Previous Semester Assignment Statistics

Statistic                        | Value
--------------------------------:|:---------------
Average Hours Spent              | 2.56
Average Score % (Grade)          | 99.3%
% students thought this was Easy | 52.14%
... Medium                       | 43.57%
... Hard                         | 2.86%
... Too Hard/Did not complete    | 1.43%


## Terminal Function Plotter

`src/plotter.py` plots the output of mathematical functions such as `y = sin(x)`, `y = cos(x)`, etc.  It does this by treating the terminal as an XY grid and drawing X,Y coordinate pairs as spaces ` ` or asterisks `*`.

This problem is described in Programming Perls, p. 28 in the chapter "Data Structures Programs" as an alternative to storing output in an array.

This program demonstrates how to succinctly represent a sine wave in code by immediately printing each "pixel" as it is computed.  This implementation is an alternative to the more obvious approach of defining a 2D array of `*`s and spaces, or a 1D array encoding (X, Y) coordinates, 

This approach saves memory (this program doesn't create any arrays) in exchange for spending a lot of extra CPU time (the value of the function is re-computed for each pixel, whether or not a `*` is to be printed there).

Looked at another way, the terminal itself is used as a 2D array that stores the value of the function for each point in the viewport.

You can decide if this is a good use of the computer's resources ;-)


### Program Requirements

*   The user is expected to input a single character, then press `Enter`
    *   Both upper- and lower-case input is accepted
    *   The menu is repeated when an invalid option is chosen
        *   A brief error message is shown which echoes the user's input
        *   This is to help the user understand their mistake and reduce their frustration
    *   The program immediately quits when `q` or `Q` is entered
*   When a valid input is given that function is plotted on the screen
    *   The name of the function is printed
    *   A vertical line is printed along the left margin
    *   A horizontal line is printed along the bottom margin
    *   The points where the function has values are denoted with **bold yellow** asterisks `*`
    *   For all other points a space ` ` is printed
    *   The size of the plot is **80 columns** wide by **14 lines tall**
*   The **domain** and **range** of each plot must be chosen such that the functions do not raise errors
    *    For example, the square root function `math.sqrt()` crashes with a `ValueError` when it is given a negative number as input
    *   Care must be taken by the programmer to choose a valid **domain** for each function so that crashes are avoided
*   After the plot is drawn, the user is returned to the menu
*   If the user presses `Ctrl-C` to forcibly terminate the program, Python will exit with an exception
    *   This is the only acceptable way for this program to crash


### Running the Terminal Function Plotter

When the user runs `src/plotter.py` they are *prompted* for one of a set of functions to plot.  The menu looks like this:
 
```
$ python src/plotter.py
Terminal Function Plotter
-------------------------
a) sin(x)
b) cos(x)
c) tan(x)
d) x^2
e) x^3
f) abs(x)
g) floor(x)
h) sqrt(x)
i) log10(x)
j) exp(x)
q) Quit

>
```

*Note that `$` denotes the command shell prompt and `>` represents the prompt in `src/plotter.py`.*


### Output examples

#### Invalid Input

When the user provides an invalid option, a brief message is printed before the menu is redisplayed.

```
> 8
Unrecognized option '8'

> seven
Unrecognized option 'seven'

> exit
Unrecognized option 'exit'
```


#### Killing the program with `Ctrl-C`

As described above, the program may crash when the user enters `Ctrl-C`.  The exact output may vary, but will be similar to:

```
> ^CTraceback (most recent call last):
  File "/home/fadein/school/cs1440-falor-erik-assn0/src/plotter.py", line 50, in <module>
    o = input(menu).lower().rstrip()
KeyboardInterrupt
```

Whatever the user's Python system outputs in this situation is acceptable.


#### Function Plots
Below are samples of what each function's plot should look like.  Your program's output must match these samples *exactly* (with the understanding that the asterisks `*` will be printed in **bold yellow**).

##### sin(x)

```
y = sin(x)
|
|
| ****                                              ****
|*    ****                                      ****    ****
|         **                                  **            **
|           **                              **                **
|             **                          **                    **
|               *                        *                        *
|                **                    **                          **
|                  **                **                              **
|                    **            **                                  **
|                      ****    ****                                      ****    *
|                          ****                                              ****
|
|
+---------------------------------------------------------------------------------
```


##### cos(x)

```
y = cos(x)
|
|
|                                      *****
|                                   ***     ***
|                                ***           ***
|                               *                 *
|**                           **                   **                           **
|  **                       **                       **                       **
|    *                    **                           **                    *
|     **                **                               **                **
|       ***           **                                   **           ***
|          ***     ***                                       ***     ***
|             *****                                             *****
|
|
+---------------------------------------------------------------------------------
```


##### tan(x)

```
y = tan(x)
|                                                   *                             
|                                                                            *    
|*                                                                                
|                         *                        *                        *     
|                        *                        *                        *      
|                      **                       **                       **       
|                  ****                     ****                     ****         
|             *****                    *****                    *****             
|         ****                     ****                     ****                  
|       **                       **                       **                      
|      *                        *                        *                        
|     *                        *                        *                         
|                                                                                *
|    *                                                                            
|                             *                                                   
+---------------------------------------------------------------------------------
```


##### x^2

```
y = x^2
|               *                                                 *               
|                *                                               *                
|                 *                                             *                 
|                  *                                           *                  
|                   *                                         *                   
|                    *                                       *                    
|                     *                                     *                     
|                      *                                   *                      
|                       **                               **                       
|                         *                             *                         
|                          **                         **                          
|                            **                     **                            
|                              **                 **                              
|                                ****         ****                                
|                                    *********                                    
+---------------------------------------------------------------------------------
```

##### x^3

```
y = x^3
|                                                                                 
|                                                    *                            
|                                                   *                             
|                                                                                 
|                                                  *                              
|                                                **                               
|                                              **                                 
|                                   ***********                                   
|                                 **                                              
|                               **                                                
|                              *                                                  
|                                                                                 
|                             *                                                   
|                            *                                                    
|                                                                                 
+---------------------------------------------------------------------------------
```

##### abs(x)

```
y = abs(x)
|**                                                                             **
|  ***                                                                       ***  
|     ***                                                                 ***     
|        ***                                                           ***        
|           ****                                                   ****           
|               ***                                             ***               
|                  ***                                       ***                  
|                     ***                                 ***                     
|                        ***                           ***                        
|                           ***                     ***                           
|                              ****             ****                              
|                                  ***       ***                                  
|                                     *** ***                                     
|                                        *                                        
|                                                                                 
+---------------------------------------------------------------------------------
```


##### floor(x)

```
y = floor(x)
|                                                                                *
|                                                                        ******** 
|                                                                                 
|                                                                ********         
|                                                        ********                 
|                                                                                 
|                                                ********                         
|                                        ********                                 
|                                ********                                         
|                                                                                 
|                        ********                                                 
|                ********                                                         
|                                                                                 
|        ********                                                                 
|********                                                                         
+---------------------------------------------------------------------------------
```


##### sqrt(x)

```
y = sqrt(x)
|                                                                           ******
|                                                                ***********      
|                                                      **********                 
|                                              ********                           
|                                     *********                                   
|                              *******                                            
|                       *******                                                   
|                  *****                                                          
|             *****                                                               
|         ****                                                                    
|     ****                                                                        
|   **                                                                            
| **                                                                              
|                                                                                 
|*                                                                                
+---------------------------------------------------------------------------------
```


##### log10(x)

```
y = log10(x)
|                                             ************************************
|               ******************************                                    
|     **********                                                                  
|  ***                                                                            
| *                                                                               
|                                                                                 
|                                                                                 
|                                                                                 
|                                                                                 
|                                                                                 
|                                                                                 
|                                                                                 
|                                                                                 
|                                                                                 
|                                                                                 
+---------------------------------------------------------------------------------
```

##### exp(x)

```
y = exp(x)
|                                                                                *
|                                                                               * 
|                                                                              *  
|                                                                            **   
|                                                                           *     
|                                                                         **      
|                                                                       **        
|                                                                     **          
|                                                                  ***            
|                                                               ***               
|                                                           ****                  
|                                                      *****                      
|                                              ********                           
|                              ****************                                   
|******************************                                                   
+---------------------------------------------------------------------------------
```
