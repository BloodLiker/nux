# K (1,1) = Black
#   (1,1) = Black
# R (4,4) = Red
# G (9,9) = Green
# Y (8,8) = Yellow
# B (12,12) = Blue
# V (13,13) = Violet
# T (11,11) = Turquoise
# W (0,0) = White
# A (14,14) = Grey and black
# D (5,5) = Dark Red
# E (3,3) = Dark Green
# O (7,7) = Dark Yellow
# U (2,2) = Dark Blue
# I (6,6) = Dark Violet
# Q (10,10) = Dark Turquoise
# L (15,15) = Light Grey

#a=$1
#b=""
#while [ "$a" != "$b" ]
#	do
#	b=$a
#	a=$(echo $b | sed "s/\(.\)\(\.*\)\1/\1\2\./g")
#done
#echo $b
sed "s/W/C0,0\./g" |
sed "s/K/C1,1\./g" |
sed "s/ /C1,1\./g" |
sed "s/U/C2,2\./g" |
sed "s/E/C3,3\./g" |
sed "s/R/C4,4\./g" |
sed "s/D/C5,5\./g" |
sed "s/I/C6,6\./g" |
sed "s/O/C7,7\./g" |
sed "s/Y/C8,8\./g" |
sed "s/G/C9,9\./g" |
sed "s/Q/C10,10\./g" |
sed "s/T/C11,11\./g" |
sed "s/B/C12,12\./g" |
sed "s/V/C13,13\./g" |
sed "s/A/C14,14\./g" |
sed "s/L/C15,15\./g" |
sed "s/C//g"
