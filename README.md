# numerical_methods  
  
## systemSolution:  
First folder containes 3 methods: Gauss, Cholesky and Sweep method (called \"running\")  
When program start, you need to enter a number of matrix size, for example 100 it's compute fast, but 500 it will be long.  
With source files in folder locate image with graphics of dependence between matrix size and time execution (integrated function work too fast).  
  
### Task № 1 - Gauss (systemSolution/Gauss.py):    
![](pictures/Gauss_1_300.png)  
### Task № 2 - Sweep (systemSolution/Running.py):    
![](pictures/Running_1_7000.png)    
### Task № 3 - Cholesky (systemSolution/Cholesky.py):   
![](pictures/Cholesky_1_120.png)   
  
## iterativeMethods:  
Is simillar situation like with first folder: Jacobi and Seidel.  
Also with source were attached images with graphics of same dependence.  
  
### Task № 1 - Jacobi (iterativeMethods/Jacobi.py):     
![](pictures/Jacobi_1_400.png)   
### Task № 2 - Seidel (iterativeMethods/Seidel.py):  
![](pictures/Seidel_1_350.png) 
  
## approximation:  
As well as in first and second folders here are the sources. But in addition were attached bonus problem. For Lagrange's method - make it on random grid more faster then was (i could reach asymptotics O(n^2 + mn)), all proofs you can find below. For Splines method - do all on random grid. Derivation of formulas below.   

### Task № 1 - Linear (appoximation/Linear/py):    
![](pictures/Linear.png)  
### Task № 2 - Lagrange (approximation/Lagrange+bonus.py):   
![](pictures/Lagrange.png)   
### Task № 3 - Spline (approximation/Spline+bonus.py):   
![](pictures/Spline.png)

### Bonus tasks:
   
![](https://latex.codecogs.com/gif.latex?\dpi{150}&space;\newline&space;\textbf{1\)Lagrange&space;\&space;polynomial:}\newline&space;P(x)=\sum_{i=0}^{n-1}y_i\prod_{i=0,j\neq&space;i}^{n-1}\frac{x-x_j}{x_i-x_j}\newline&space;\texttt{Standart&space;asymptotics:}\&space;O(n^2m)\newline&space;P(x)=\sum_{i=0}^{n-1}y_i\prod_{j=0,j\neq&space;i}^{n-1}\frac{x-x_j}{x_i-x_j}&space;=\sum_{i=0}^{n-1}y_i&space;\prod_{j=0,j\neq&space;i}^{n-1}\frac{x-x_j}{x_i-x_j}&space;\frac{x-x_i}{x-x_i}&space;=&space;\sum_{i=0}^{n-1}y_i\frac{\prod_{j=0}^{n-1}(x-x_j)}{\prod_{j=0,j\neq&space;i}^{n-1}(x_i-x_j)}&space;\frac{1}{x-x_i}=\newline&space;=&space;\prod_{j=0}^{n-1}(x-x_j)\sum_{i=0}^{n-1}\frac{y_i}{x-x_i}\frac{1}{\prod_{j=0,j\neq&space;i}^{n-1}(x_i-x_j)}&space;=&space;\prod_{j=0}^{n-1}(x-x_j)\sum_{i=0}^{n-1}\frac{A_i}{x-x_i}\newline&space;\texttt{Where:}\newline&space;A_i=\frac{y_i}{\prod_{j=0,j\neq&space;i}^{n-1}(x_i-x_j)},x\neq&space;x_i\newline&space;\texttt{Let}\newline&space;\alpha(x)=\prod_{j=0}^{n-1}(x-x_j),\&space;\beta(x)=\sum_{i=0}^{n-1}\frac{A_i}{x-x_i},\&space;P(x)=\alpha(x)\beta(x)\newline&space;A_i,i=\overline{0,n-1}\Rightarrow&space;O(n^2)\newline\alpha(x)\Rightarrow&space;O(mn)\newline\beta(x)\Rightarrow&space;O(mn)\newline&space;\mathbf{Total:O(n^2&plus;mn)}) 
  
![](https://latex.codecogs.com/gif.latex?\dpi{150}&space;\newline&space;\textbf{2\)Spline&space;interpolation&space;on&space;random&space;grid:}\newline&space;\texttt{Let}\newline&space;P_i(x)=A_i(x-x_i)^3&plus;B_i(x-x_i)^2&plus;C_i(x-x_i)&plus;D_i\newline&space;\texttt{Conditions:}\newline&space;1\)P_i(x_i)=y_i;&space;\&space;i&space;=&space;\overline{0,n-1}\newline&space;2\)P_i(x_{i&plus;1})=y_{i&plus;1};\&space;i=\overline{0,n-1}\newline&space;3\)P'_i(x_{i&plus;1})=P'_{i&plus;1}(x_{i&plus;1});\&space;i=\overline{0,n-2}\newline&space;4\)P''_i(x_{i&plus;1})=P''_{i&plus;1}(x_{i&plus;1}),&space;\&space;i=\overline{0,n-2}\newline&space;5\)P''_0(x_0)=0\newline&space;6\)P''_{n-1}(x_n)=0\newline&space;\texttt{Get}\newline&space;1\)D_i=y_i;\&space;i=\overline{0,n-1}\newline&space;2\)A_ih_i^3&plus;B_ih_i^2&plus;C_ih_i&plus;D_i=y_{i&plus;1};\&space;i&space;=&space;\overline{0,n-1}\newline&space;3\)3A_ih_i^2&plus;2B_ih_i&plus;C_i=C_{i&plus;1};\&space;i=\oveline{0,n-2}\newline&space;4\)6A_ih_i&plus;2B_i=2B_{i&plus;1};\&space;i=\overline{0,n-2}\newline&space;5\)2B_0=0\newline&space;6\)6A_{n-1}h_{n-1}&plus;2B_{n-1}=0)
![](https://latex.codecogs.com/gif.latex?\dpi{150}&space;\newline&space;A_i=\frac{B_{i&plus;1}-B_i}{3h_i}\&space;\texttt{from&space;(4)}\newline&space;\texttt{Let&space;}B_n=0\newline&space;\frac{B_{i&plus;1}-B_i}{3h_i}h_i^3&plus;B_ih_i^2&plus;C_ih_i&plus;y_i=y_{i&plus;1}\&space;(7)\newline&space;3\frac{B_{i&plus;1}-B_i}{3h_i}h_i^2&plus;2B_ih_i^2&plus;C_i=C_{i&plus;1}\&space;\&space;\&space;\&space;\&space;\&space;(8)\newline&space;B_0=0,&space;\&space;B_n=0&space;\newline&space;(7)\Rightarrow\&space;C_i=\frac{y_{i&plus;1}-y_i}{h_i}-\frac{B_{i&plus;1}&plus;2B_i}{3}h_i\&space;\&space;(9)\newline&space;(9)\texttt{&space;and&space;}&space;(8)\Rightarrow&space;(B_{i&plus;1}-B_i)h_i&plus;2B_ih_i=\frac{y_{i&plus;2}-y_{i&plus;1}}{h_{i&plus;1}}-\frac{B_{i&plus;2}&plus;2B_{i&plus;1}}{3}h_{i&plus;1}-\frac{y_{i&plus;1}-y_i}{h_i}&plus;\frac{B_{i&plus;1}&plus;2B_i}{3}h_i\newline&space;B_i(-h_i&plus;2h_i-\frac{2}{3}h_i)&plus;B_{i&plus;1}(h_i&plus;\frac{2}{3}h_{i&plus;1}-\frac{1}{3}h_i)&plus;\frac{1}{3}B_{i&plus;2}h_{i&plus;1}=\frac{y_{i&plus;2}-y_{i&plus;1}}{h_{i&plus;1}}-\frac{y_{i&plus;1}-y_i}{h_i}\newline&space;\textbf{Total:&space;}\newline&space;D_i=y_i\newline&space;A_i=\frac{B_{i&plus;1}-B_i}{3h_i}\newline&space;C_i=\frac{y_{i&plus;1}-y_i}{h_i}-\frac{B_{i&plus;1}&plus;2B_i}{3}h_i\newline&space;B_ih_i&plus;2(h_i&plus;h_{i&plus;1})B_{i&plus;1}&plus;h_{i&plus;1}B_{i&plus;2}=3(\frac{y_{i&plus;2}-y_{i&plus;1}}{h_{i&plus;1}}-\frac{y_{i&plus;1}-y_i}{h_i}))  

<strong>3) Spline on 2 demensional grid:</strong>  
All GUI was created using pygame.  
![](pictures/2DSpline.png)  
#### How to install:   
<code>pip install pygame</code>  
#### Structure of code:  
function for solve problem with 3 diagonal matrix  
<code>def func(a, b, c, f, N)</code>  
a - lower diagonal  
b - central diagonal  
c - upper diagonal  
f - answer vector  
#### function for generate splines:  
<code>def generateSpline(x, y)</code>  
x - coordinates of point on Ox axis  
y - coordinatws of point on Oy axis  
#### function for draw spline:  
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
![](3/2DTSpline.png)  
draw curse using  
<code>draw(...)</code>  
function, mapped on display all changes  
<code>pygame.display.update()</code>  
make pause 0.02 sec  
<code>pygame.time.delay(20)</code>  
and continue working.  

## mathematicalPhysics:
### Diffusion:  
![](pictures/diffusion.png)  
Main purpose - after pressing create temperature spot and it's distribution.
![](pictures/Scheme.png)  
```
newMatrix[i][j] = matrix[i][j] + C * (matrix[i - 1][j] + matrix[i + 1][j] +matrix[i][j - 1] +
                                      matrix[i][j + 1] - 4 * matrix[i][j])
```   
<code>computing()</code> - main function for calculating cell temperature  
<code>draw()</code> - display surface  
<code>pressed = pygame.mouse.get_pressed()</code> - control of pressing on button  
<code>pos = pygame.mouse.get_pos()</code> - get cursor position during pressing    
<code>if pressed[0]:</code>  
&nbsp;&nbsp;&nbsp;&nbsp;<code>matrix[pos[0]][pos[1]] = 400.0</code> - set temperature in pressed pixel  
### Wave:
![](pictures/wave.png)   
```
matrix[i][j] = 2.0 * matrixOld[i][j] - matrixSuperOld[i][j] + C * (matrixOld[i+1][j] + matrixOld[i-1][j] +
                                                                   matrixOld[i][j-1] + matrixOld[i][j+1] -
                                                                   4.0 * matrixOld[i][j])
```  
<code>computing()</code> - main function for calculating wave distribution  
<code>draw()</code> - display surface  
<code>pressed = pygame.mouse.get_pressed()</code> - control of pressing on button  
<code>pos = pygame.mouse.get_pos()</code> - get cursor position during pressing    
<code>if pressed[0]:</code>  
&nbsp;&nbsp;&nbsp;&nbsp;<code>matrix[pos[0]][pos[1]] = 300.0</code> - start wave from pressed pixel 
