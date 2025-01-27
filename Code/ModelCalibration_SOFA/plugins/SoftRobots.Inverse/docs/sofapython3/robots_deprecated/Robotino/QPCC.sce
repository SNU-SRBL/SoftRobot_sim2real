
// todo, supprimer cs ?

// cc lines provide is the list of row in C that are complementarity constraints 
// cc values provide the rows in vector x that are the dual values for complementarity constraints
// we suppose that the equality constraints are set at the first rows
convergence=0;
active_cc_value=[];
active_cc_lines=[];
sizeQ=size(Q,2);
sizeC=size(C,1);

not_cc_values= setdiff([1:sizeQ],ccvalues);
not_cc_constraint= setdiff([1:sizeC],cclines);


maxStep=12;
step=0;
lambda=zeros(sizeQ,1);

while (convergence==0 & step<maxStep),
    
    // list of active constraints and values
    values_set=[not_cc_values active_cc_value];
    constraint_set=[not_cc_constraint active_cc_lines];
    
    // reduced optimization problem
    Qred= Q(values_set, values_set);
    pred= p(values_set);
    Cred= C(constraint_set,values_set);
    bred= b(constraint_set);
    cired= ci(values_set);
    
    lambdared= qpsolve(Qred,pred,Cred,bred,cired,cs,me);
    
    // put the values into lambda
    lambda=zeros(sizeQ,1);
    lambda(values_set) = lambdared;
    
    // verifies the complementarity constraints
    delta = - C * lambda + b;
    
    
    // pivoting
    old_active_cc_lines= active_cc_lines;
    old_active_cc_value= active_cc_value;
    numActiveCC=size(active_cc_lines,2);
    desactivateC=0;
    violationValue=0;
    violationInd=0;

    i=0;
    for l=cclines,
        i=i+1;
        v=ccvalues(i);
        
        // test if line l is active
        if (size(intersect(l,active_cc_lines),1)) then
            //line is active:  verifies the complementarity
            if (delta(l)*lambda(v) > 0.00001 ) then
                // should desactivate this constraint
                ind = find(l==old_active_cc_lines)
                active_cc_lines = old_active_cc_lines([1:ind-1 ind+1:numActiveCC]);
                active_cc_value = old_active_cc_value([1:ind-1 ind+1:numActiveCC]);
                 
                desactivateC=1;
                break;
            end
            
           
       else 
            // line is not active: verifies if violation
            if (delta(l)<-0.0000001) then
                if (delta(l)<violationValue) then
                    violationValue = delta(l);
                    violationInd = l;
                    violationInd2= v;
                end
            end
        end
    end
    
    if (desactivateC==0 & violationInd==0) then
        convergence=1;
    end

    
        
    if (desactivateC==0 & violationInd>0) then
         active_cc_lines = union(active_cc_lines, violationInd);
         active_cc_value = union(active_cc_value, violationInd2);
    end

    
    
    
    step=step+1;
end

lambda(values_set) = lambdared;






