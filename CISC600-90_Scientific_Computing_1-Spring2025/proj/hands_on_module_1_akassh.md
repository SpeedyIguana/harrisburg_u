# Assignment Hands On Module 1

## Meta-Info

- Course: CISC600-90-O
- Semester: Spring 2025
- Student Name: Akassh Shah

## Assignment Instructions

> Solve any one (1) problem from Chapter 1, pages 21-27. Analyze your results and upload your solution in a text, jupyter notebook, or word file.
> (Note: make sure to use the official textbook Chapra and Canale, 8th edition - don't use an earlier or newer edition)

## Assignment

For this assignment, I have chosen to solve the problem 1.16 on page 24.

This problem states

> 1.16   A  fluid  is  pumped  into  the  network  shown  in  Fig.  P1.16.  If Q2 = 0.7, Q3 = 0.5, Q7 = 0.1, and Q8 = 0.3 m3/s, determine the other flows.

For this, the unknowns are Q1, Q4, Q5, Q6, Q9, Q10.

### Working

For simplicity, I'm using lower case `q` instead of upper case `Q`

```text
q1 = q2 + q3
q1 = 0.7 + 0.5 = 1.2

q2 = 0.7

q3 = 0.5
q3 = q4 + q5

q4 = q3 - q5
q4 = 0.5 - 0.3 = 0.2

q5 = q6 + q7
q5 = 0.2 + 0.1 = 0.3

q6 = q8 - q7
q6 = 0.3 - 0.1 = 0.2

q7 = 0.1

q8 = 0.3
q8 = q6 + q7

q9 = q4 + q8
q9 = 0.2 + 0.3 = 0.5

q10 = q2 + q9
q10 = 0.7 + 0.5 = 1.2
```
