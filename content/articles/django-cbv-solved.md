Title: The 24 Hour Django Problem
Date: 2016-4-5 05:01pm
Category: Blog
Tags: django,class-based views, tdd
Slug: django-cbv-solved
Author: Alec Patrizio
Summary: Getting the hang of Django's class-based views

### Getting the hang of Django's class-based views
I've been working through the excellent [Test Driven Development](http://chimera.labs.oreilly.com/books/1234000000754) by Harry Percival for a few months, with irregularity. For the most part, the learning process has been smooth, apart from some minor issues here and there -- usually my own stupid mistakes.

I just completed [Chapter 14](http://chimera.labs.oreilly.com/books/1234000000754/ch14.html), which left off with a new deployment of the To-Do List app to the live server, with new form validation features. It was all working fantastically, until I noticed a bug that slipped through the cracks -- something that I had overlooked. Now, whether this is something that the author will cover in the next few chapters I do not know yet. But it was bugging me enough that I had to fix it myself, without the helping hand of Mr. Percival. Although he is very helpful and very quickly responded to some questions of mine via email, I would attempt this one solo. Only the testing goat would be there to hold me.

So off I went, on a journey through the Django docs, Googling the wrong questions, and sifting through the quality Stack Overflow posts that only lightly touched on my question, and left me with more questions -- all fairly standard when hitting walls in self-study of programming.

I finally stumbled upon a [website](http://ccbv.co.uk/) which gave clear and easily searchable documentation on Django's class-based views (CBVs), which I had just recently figured was the problem. Don't get me wrong--the Django docs are excellent and were also very useful. This site simply laid out the source code for every method so I was easily able to find those which I thought were giving me problems, and gained insight into the inner workings of what these magical CBVs were actually doing under the hood. This, combined with the previous resources I mentioned, allowed me to fully grasp my problem, and figure out the right solution. Then it was just a matter of getting proper syntax to get Django's CBVs to do what I wanted. 

In hindsight, I could have did some more testing myself in the interactive shell, to explore things like the MRO (method resolution order) that might have given me insight. In any case, I feel that all this has given me a better understanding of not just CBVs, but how classes and inheritance work in Python overall. Can't complain about that.
