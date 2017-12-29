# MITx-6.00-pset1-Problem-3
Write a program that prints the longest substring of s in which the letters occur in alphabetical order

I was stuck on this for a while.  My problem was I was comparing count to hicount inside the second nested for loop.  Moving it out and to the end of the first for loop solved it.

It seems inefficient, as it runs a subloop each time it increments forward.  I want to come back and recode where it iterates thru the string just once, grabbing each qulifying substring and then finding the longest one.
