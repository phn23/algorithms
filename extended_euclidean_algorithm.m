% The flowchart of this algorithm follows from Dr Jossy Sayir's course 4F5:
% Advanced Information Theory and Coding at the University of Cambridge Engineering Department
% (one of the most fun courses)

% user input for n1 and n2
n1 = input('Enter the first number (n1): ');
n2 = input('Enter the second number (n2): ');

% make sure n1 is larger
if n1 < n2
    temp = n1;
    n1 = n2;
    n2 = temp;
end

if n2 <= 0
    error('n2 must be greater than 0.');
end

a1 = 1; b1 = 0
a2 = 0; b2 = 1


% loop


while true
    r = mod(n1, n2) 
    q = floor(n1 / n2)
    if r == 0
        g = n2
        a = a2
        b = b2

        break;
    else
        n1 = n2
        n2 = r

        t = a1
        a1 = a2
        a2 = t - q * a2

        t = b1
        b1 = b2
        b2 = t - q * b2
    end
end

% Display the results
fprintf('The gcd is: %d\n', g);
fprintf('The coefficients are: a = %d, b = %d\n', a, b);
fprintf('g=an1+bn2:  %d = %d*%d + %d*%d',g,  a, n1, b, n2);
