Family members have been asking me about ChatGPT in recent gatherings. I have a
bunch of opinions about ChatGPT, and wanted to put my thoughts together. And
hopefully explain them.

ChatGPT, Google Bard, MetaAI are based on technology known as *large language
models*. There's a bit of jargon to unpack, here.

A *language model* is a computer program that generates probabilities of a
series of words. *Model* is borrowed from physics, where it means a mathematical
representation of a real phenomenon. It's arguable what real phenomenon is
represented by a language model, though, so I think it's best understood as a
set phrase.

So you provide a langauge model with a series of words, and the result is
probabilities (i.e., numbers). What the "probabilities" represent has much to do
with the details of how the models are defined and trained. The important thing
is that they're numbers, which allows programmers to change questions about
*language*

  What is the best word to complete this sentence: The apple is ____.

Into questions about *numbers*

  What word gives us the sentence with the HIGHEST NUMBERS: The apple is ____.

The former is essentially impossible. Is it red? Is it tasty? Is it rotten? Is
it falling? The latter is something drummed into the skull of every undergraduate
computer science student. 


A "language model" is a computer program that ???

  **TODO**: Is there a layperson definition I can give here?  I'm not sure if it's important for the point I want to make, though.  Maybe just ChatGPT throughout?

I find the details of how this all works *just fascinating*. That's why I
voluntarily devoted years of my life to studying machine learning in graduate
school, and have tended to steer my career toward opportunities to use and apply
machine learning. But I don't think that's why so many people are suddenly
asking me about ChatGPT. So I'm not going to try to explain *how it works*. But
I do think it's necessary to understand *what it does*.

Machine learning is about producing a software program based on examples.
Imagine you wanted a program to check whether words were spelled correctly.

  **TODO**: Is there a better example?  Maybe something *useable*.

It seems like this should be conceptually straightforward. Simply give the
program access to a large dictionary, and then check whether each word is in the
dictionary.  But then you get smart alecks that write things like

  I went hiking, and was chaste buy a bare.

Are the words spelled correctly?  As a programmer, I SAY YES!

.
.
.

Bitter, bitter, experience has taught me that as a programmer, *everyone on the
planet that is not a programmer* expects programs to do the opposite of what I
do. I very much suspect that this is the source of frustration people have with
computers. It is not intelligence or patience or anything like that. It is
simply a matter of the person *using* the computer having expectations
*diametrically opposed* to the person *programming* the computer. So I know
people (with the expectation of programmers, and maybe ironic poets) will *not
like* my spell-checking program if it says "chaste," "buy," "and "bare" are
spelled correctly.

We could try to design rules to fix this. Since "bare" is an adjective, and
adjectives Do Not Work Like That, for reasons I recall my English teachers
explaining *at length*, it isn't correct spelling. Similarly, "buy" is a verb
and blah blah blah. Sorry, English teachers.

But what about "chaste?"

  I went hiking, and was chaste by a bear.

Ok, ok, passive voice, etc., but it isn't *ungrammatical*. It just seems somehow
*unlikely* that someone would choose to establish that *particular state* while
describing an encounter with a large, dangerous predator. It reminds me of when
I took a class on surrealist art, and the teacher had us all writing sentence
fragments and put them together randomly.

Machine learning is useful when you want to identify things that are technically
correct, but obviously kinda wrong. The idea is to provide a bunch of examples
of correct sentences:

I went hiking, and was chased by a deer.

I went swimming, and was chased by a shark.

I went to a rave, and was chased by a stereo.

  **TODO**: this all seems too complicated...maybe just go straight to the
  predict next token.

While I have a fair bit of machine learning experience, I don't have expertise
with large language models like ChatGPT specifically. My work would be better
described as "small" models. They tend to focus on solving very specific
problems, while large language models are exciting because they can solve many
problems. That said, I have a decent understanding of the core technology
powering the models (which is the same in large and small models), and lots of
experience turning models into real shipped features.


what do llms do? trained on text completion. but cant just store every most
likely completion. so they form shortcuts. these shortcuts are useful. othello
example. allow them to respond usefully to new input.

why are they useful? generate text that follows multiple rules. examples besides
programming?

what is the problem? i dont like hallucination. that sounds like a disfinction.
but llms aren't malfunctioning when they generate text. they have no specific
understanding of true and false beyond what they encode while trying to perform
well on the training data. companies like openai, Microsoft, etc will try to
make them more accurate overr time.

so llms are very good at generating text that "looks right". in cases where ita
easy to go feom "looks right" to "is right", they are cery helpful. key property
is being able to quickly verify correctness.

programming happens to be a task where its pretty easy to verify that something
is right. a somewhat experienced programmer can often quicly fix something thats
almost right.

writing small amounts of text (a sentence or paragraph ) is similar. assuming
fluency, verifying whether text is correctly written is pretty fast. and minor
mistakes easily corrected. the phenomenon that ots easier to proofread othera
writing plays into the users advantage here i suspect

a more specific search engine. instead of searching for general terms, ask about
the specific case. kotlin example was good. but is there a more accessible one?
helpful for things i do sporadically.

boilerplate. following a specific style. reduces friction

best examples tend to be making people more productive (especially as they
require verification). personally find them best for getting simple projects
done much more quickly rather than anything advanced. like search engines, they
shine when you need to learn something generally well known that you personally
don't know (or dont remember). thats terifdically useful, because we all have
limited time to gain expertise in everything we do. my suggestion is to try
chatgpt for "easy" things. see if it can help you do them faster. then try it
for things that you know are possible, but dont quite know how to do them. is
there an accessible example? maybe draw a parallel with historical event or
famous style.
