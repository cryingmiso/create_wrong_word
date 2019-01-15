# create_wrong_word

Wrong word created for deep learning data.

This pair data can be used in the seq2seq typo correction model. maybe.


<pre>
#eg:

target_word = "sloth"

deletes = ['loth', 'soth', 'slth', 'sloh', 'slot']

transposes = ['lsoth', 'solth', 'sltoh', 'sloht']

replaces = ['aloth', 'bloth', ... , 'sloty', 'slotz']

inserts = ['asloth', 'bsloth', ..., 'slothy', 'slothz']
</pre>


**but,**

The function looks at every possible edit to the input   a deletion of any character, a transposition of any 2 adjacent characters, replacing any character in the input with a random character or simply inserting a random character.

The result is a challenging amount of computation that needs to happen, and which grows exponentially with respect to the length of the input string.

As a result, it is reasonable to use simulated spelling error data without using such a large amount of nonsensical data.

The link below is a one billion word data set that Google has released for language modeling research.


[Link](https://ai.google/research/pubs/pub41880)
