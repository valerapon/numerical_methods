# numerical_methods  
  
### Folder № 1:  
First folder containes 3 methods: Gauss, Cholesky and sweep method (called \"running\")  
When program start, you need to enter a number of matrix size, for example 100 it's compute fast, but 500 it will be long.  
With source files in folder locate image with graphics of dependence between matrix size and time execution (integrated function work too fast).  
  
##### Task № 1 - Gauss (1/Gauss.py):    
![](1/Gauss_1_300.png)  
##### Task № 2 - Sweep (1/Running.py):    
![](1/Running_1_7000.png)    
##### Task № 3 - Cholesky (1/Cholesky.py):   
![](1/Cholesky_1_120.png)   
  
### Folder № 2:  
Is simillar situation like with first folder: Jacobi and Seidel.  
Also with source were attached images with graphics of same dependence.  
  
##### Task № 1 - Jacobi (2/Jacobi.py):     
![](2/Jacobi_1_400.png)   
##### Task № 2 - Seidel (2/Seidel.py):  
![](2/Seidel_1_350.png) 
  
### Folder № 3:  
As well as in first and second folders here are the sources. But in addition were attached bonus problem. For Lagrange's method - make it on random grid more faster then was (i can reach asymptotics O(n^2 + mn)) all proofs you can find on photo, which called like a it's source. For Splines method - do all on random grid. Derivation of formulas enclose in photo. There isn't just third superbonus, but it will apper soon.   

##### Task № 1 - Linear (3/Linear/py):    
![](3/Linear.png)  
##### Task № 2 - Lagrange (3/Lagrange+bonus.py):   
![](3/Lagrange.png)   
##### Task № 3 - Spline (3/Spline+bonus.py):   
![](3/Spline.png)

#### Bonus tasks:
  
<strong>1) Lagrange with O(n^2 + m\*n) asymptotics:</strong>  
  
&nbsp;![](3/Lagrange+bonus.jpg)  

<strong>2) Spline on random grid:</strong>  

&nbsp;![](3/Spline+bonus.jpg)  

<strong>3) Spline on 2 demensional grid:</strong>  
All GUI was created using pygame.  
##### How to install:   
<code>pip install pygame</code>  
##### Structure of code:  
function for solve problem with 3 diagonal matrix  
<code>def func(a, b, c, f, N)</code>  
a - lower diagonal  
b - central diagonal  
c - upper diagonal  
f - answer vector  
##### function for generate splines:  
<code>def generateSpline(x, y)</code>  
x - coordinates of point on Ox axis  
y - coordinatws of point on Oy axis  
##### function for draw spline:  
<code>def draw(xFactors, yFactors, tStart, tEnd)</code>  
Where xFactors and yFactors are arrays of factor of polynomial At^3+Bt^2+Ct+D (for x(t) and y(t)), tStart and tEnd are coordinates of axis "T" start and end of segment of value.   
set color:  
white for background, red for curve, green for points  
<code>WHITE = (255, 255, 255)</code>    
<code>RED = (225, 0, 50)</code>   
<code>GREEN = (0, 225, 0)</code>   
<code>pygame.init()</code> - start pygame modul  
<code>window = pygame.display.set_mode((600, 600))</code> - create window 600x600 sizes  
<code>window.fill(WHITE)</code> - set white background  
<code>pygame.display.update()</code> - show window  
Main cycle will perform while won't push exit button. For control all events use  
<code>pygame.event.get()</code>  
This function generate list of all users action.  
If type of event will be QUIT  
<code>event.type == pygame.QUIT</code>  
program just finish execution.  
If user pressed the mouse button, program will know about them using  
<code>event.type == pygame.MOUSEBUTTONDOWN</code>  
and  
<code>event.button == 1</code>  
that it was left mouse button.  
After that program set white background  
<code>window.fill(WHITE)</code>  
draw all points  
<code>pygame.draw.circle(window, GREEN, (x[j], y[j]), 5)</code>  
generate splines for x and y  
<code>generateSpline(t, x)</code>  
and  
<code>generateSpline(t, y)</code>  
draw curse using  
<code>draw(...)</code>  
function, mapped on display all changes  
<code>pygame.display.update()</code>  
make pause 0.02 sec  
<code>pygame.time.delay(20)</code>  
and continue working.  
