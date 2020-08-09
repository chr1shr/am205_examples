# Harvard Applied Math 205: Code Examples
## Unit 1: Data Fitting

##### vander\_cond.txt
This is a transcript of an interactive Python session using NumPy to evaluate
the condition number of several different Vandermonde matrices.

###### v\_inter.py
This Python program does Vandermonde polynomial interpolation, outputting the
results and error to text, which can be reading by plotting programs such
as [Gnuplot](https://gnuplot.info). If the program is run with
```Shell
python v_inter.py >out
```
so that the data is sent to a file called **out**, then within Gnuplot the
results can be shown with the command:
```Gnuplot
plot 'out' u 1:3 t 'Reference curve', 'out' u 1:2 t 'Polynomial fit'
```
The differences between the two can be shown with the command:
```Gnuplot
plot 'out' u 1:4 t 'Interpolation differences'
```

###### v\_inter2.py
This is a second version of v_inter.py that uses Matplotlib to plot the results
directly within Python.

###### ch\_inter.py
This Python program performs Lagrange interpolation using Chebyshev or
linearly-spaced points.

##### lsum.py
This program calculates the sum of absolute values of the Lagrange polynomial,
needed to evaluate the Lebesgue Constant.

##### spline.py & spline2.py
**spline.py** calculates a cubic spline using the library functions in SciPy.
It also calculates the differences between splines using slightly different
control points. **spline2.py** is an example of defining a parametric curve
using two cubic splines x(t) and y(t).

##### lfit.py
This program performs least-squares fitting of a polynomial to samples of
cos(4\*x). It uses two different methods: a direct approach based on the normal
equations (which is generally ill-conditioned) and a built-in Python routine,
**lstsq**, that uses a different algorithm with better conditioning. The methods
used by lstsq will be discussed later in the course.

##### np\_lfit.py
This program performs linear least squares fitting of a sum of exponentials to
a given function. It demonstrates that the linear least squares does not just
work for polynomials.

##### under\_lfit.py
This program demonstrates underconstrained least squares, whereby a high-degree
polynomial is fitted to a small number of data points by imposing additional
constraints.

##### nonlinlsq.py
This program solves a nonlinear least squares problem based on finding the
position of a radio transmitter based on signal received at nearby beacons.
