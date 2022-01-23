#!/usr/bin/python3
sub1 = float(input("Enter the marks of subject1 : "))
sub2 = float(input("Enter the marks of subject1 : "))
sub3 = float(input("Enter the marks of subject1 : "))
sub4 = float(input("Enter the marks of subject1 : "))
sub5 = float(input("Enter the marks of subject1 : "))
avg = (sub1+sub2+sub3+sub4+sub5)/5
grade = 'A';
if avg >75 :
	grade = 'A'
elif avg >65 :
	grade = 'B'
elif avg >55 :
	grade = 'C'
elif avg>45 :
	grade = 'D'
else :
	grade = 'E'
print("Grade for the average =",avg," is : ", grade)

