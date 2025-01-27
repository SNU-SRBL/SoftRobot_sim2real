function [Vresult]=Rotate(Q,V)

Vresult=[((1 - 2 * (Q(2) *Q(2) +Q(3) *Q(3)))*V(1) + (2 * (Q(1) *Q(2) -Q(3) *Q(4))) * V(2) + (2 * (Q(3) *Q(1) +Q(2) *Q(4))) * V(3));
((2 * (Q(1) *Q(2) +Q(3) *Q(4)))*V(1) + (1 - 2 * (Q(3) *Q(3) +Q(1) *Q(1)))*V(2) + (2 * (Q(2) *Q(3) -Q(1) *Q(4)))*V(3));
((2 * (Q(3) *Q(1) -Q(2) *Q(4)))*V(1) + (2 * (Q(2) *Q(3) +Q(1) *Q(4)))*V(2) + (1 - 2 * (Q(2) *Q(2) +Q(1) *Q(1)))*V(3))];
endfunction

function [Vresult]=inverseRotate(Q,V)
Vresult=[((1 - 2 * (Q(2) *Q(2) +Q(3) *Q(3)))*V(1) + (2 * (Q(1) *Q(2) +Q(3) *Q(4))) * V(2) + (2 * (Q(3) *Q(1) -Q(2) *Q(4))) * V(3));
((2 * (Q(1) *Q(2) -Q(3) *Q(4)))*V(1) + (1 - 2 * (Q(3) *Q(3) +Q(1) *Q(1)))*V(2) + (2 * (Q(2) *Q(3) +Q(1) *Q(4)))*V(3));
((2 * (Q(3) *Q(1) +Q(2) *Q(4)))*V(1) + (2 * (Q(2) *Q(3) -Q(1) *Q(4)))*V(2) + (1 - 2 * (Q(2) *Q(2) +Q(1) *Q(1)))*V(3))];
endfunction


function [R]=RotM(Q)
  R= [(1 - 2 * (Q(2) *Q(2) +Q(3) *Q(3)))  (2 * (Q(1) *Q(2) -Q(3) *Q(4))) (2 *(Q(3) *Q(1) +Q(2) *Q(4)));
 (2 * (Q(1) *Q(2) +Q(3) *Q(4)))  (1 - 2 * (Q(3) *Q(3) +Q(1) *Q(1)))       (2 * (Q(2) *Q(3) -Q(1)*Q(4)));
 (2 * (Q(3) *Q(1) -Q(2) *Q(4)))  (2 * (Q(2) *Q(3) +Q(1) *Q(4))) (1 - 2 * (Q(2) *Q(2) +Q(1) *Q(1)))];
endfunction


function [c]=cross(a,b)
  c = [a(2)*b(3) - a(3)*b(2);
  a(3)*b(1) - a(1)*b(3);
  a(1)*b(2) - a(2)*b(1)];
endfunction

function [A]=CrossM(a)
  A=[0 -a(3) a(2); a(3) 0 -a(1); -a(2) a(1) 0];
endfunction

function [Q]=AlignXbyRotateY(x)
    
    d = x/norm(x);
    // angle of rotation
    cTheta = d(1);
    theta= acos(cTheta);
    
    // axis of rotation
    a = [0;-d(3); d(2)];
    an=a/norm(a);
    
    Q=[an*sin(theta/2); cos(theta/2)]
    
endfunction
