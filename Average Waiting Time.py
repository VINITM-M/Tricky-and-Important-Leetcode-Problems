There is a restaurant with a single chef. You are given an array customers, where customers[i] = [arrivali, timei]:

arrivali is the arrival time of the ith customer. The arrival times are sorted in non-decreasing order.
timei is the time needed to prepare the order of the ith customer.
When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle. The customer waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a time. The chef prepares food for customers in the order they were given in the input.

Return the average waiting time of all customers. Solutions within 10-5 from the actual answer are considered accepted.

customers = [[1,2],[2,5],[4,3]] 

1 cusomter arrives , his waiting time 2  : total time taken 3 

Assumes that we're in 3 clock , but 2 clock itself the guy ordered , we've 1 min extra + actual waiting time  

Maximum clock - 3 clock , 
overall clocl = max(a, clock) 
b - waiting 
total += overall clock - b 

Code: 

t = 0 ; diff = 0 
for a, b in customers:
  t = max(a, t)  
  t += b 
  diff += (t - a) 
return diff / len(customers)
