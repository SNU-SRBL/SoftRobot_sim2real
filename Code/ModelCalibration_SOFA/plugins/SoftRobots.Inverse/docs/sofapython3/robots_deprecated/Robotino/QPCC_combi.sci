function [lambda, step] = qpcc_combi(Q,p,C,b,ci,cs,me, cclines, ccvalues)
convergence=0;
active_cc_value=[];
active_cc_lines=[];
sizeQ=size(Q,2);
sizeC=size(C,1);

not_cc_values= setdiff([1:sizeQ],ccvalues);
not_cc_constraint= setdiff([1:sizeC],cclines);


// combinatory of the algorithm;
num_cc = size(cclines,2);
combi = 2^num_cc;

activ_table = zeros(1,num_cc);

globalMin=number_properties("huge");
for i=1:combi,
    
    i
    
    // create an "activation table" (test all the combinations)
    for j=1:num_cc,
        if(activ_table(j) == 2) 
            activ_table(j)=0;
            activ_table(j+1)=activ_table(j+1)+1;
        end
        
    end
    
    // put the activation table in active_cc_value and active_cc_lines
    active_cc_value=[];
    active_cc_lines=[];
    numActiveCC=0;
    
    for j=1:num_cc,
        if (activ_table(j)==1) then
            active_cc_value = union(active_cc_value,ccvalues(j));
            active_cc_lines = union(active_cc_lines,cclines(j));
        end
    end
    
    
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
    lambdasol=zeros(sizeQ,1);
    lambdasol(values_set) = lambdared;
    
    // verifies the complementarity constraints
    delta = - C * lambdasol + b;
    
    
    // verifies if the solution is correct for complementarity constraint
    correct=1;
    
    i=0;
    for l=cclines,
        i=i+1;
        v=ccvalues(i);
        
        if (delta(l)<0) then
            correct=0;
        end
        if (lambdasol(v)<0) then
            correct=0;
        end
        if (delta(l)*lambdasol(v) > 0.00001 ) then
            correct=0;
        end
        
    end
    
    
    if (correct) then
        // verifies the minimization
        localMin = lambdasol'*Q*lambdasol + p'*lambdasol;
        
        // compare it to the globalMin
        if (localMin <globalMin) then
            globalMin=localMin;
            lambda = lambdasol;
        end
        
        
    end
    

    
    
    
    // put at the end    
    activ_table(1)= activ_table(1)+1;

end



endfunction
