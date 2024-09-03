# KataPlayingCardSecretCode
https://www.codewars.com/kata/59b9a92a6236547247000110/train/python

If you like cryptography and playing cards, have also a look at Card-Chameleon, a Cipher with Playing cards.
And if you just like playing cards, have a look at Playing Cards Draw Order.
As a secret agent, you need a method to transmit a message to another secret agent. But an encrypted text written on a notebook will be suspicious if you get caught. A simple deck of playing cards, however, is everything but suspicious...

With a deck of 52 playing cards, there are 52! different possible permutations to order it. And 52! is equal to 80658175170943878571660636856403766975289505440883277824000000000000. That's a number with 68 digits!

There are so many different possible permutations, we can assert with great confidence that if you shuffle the cards well and put them back together to form a deck, you are the first person in history to get that particular order. The number of possible permutations in a deck of cards is higher than the estimated number of atoms in planet Earth (which is a number with about 50 digits).

With a way to associate a permutation of the cards to a sequence of characters, we can hide a message in the deck by ordering it correctly.

### Correspondence between message and permutation
### Message

To compose our message, we will use an alphabet containing 27 characters: the space and the letters from A to Z. We give them the following values:

<pre>space = 0</pre>
<pre>A = 1</pre>
<pre>B = 2</pre>
<pre>...</pre>
<pre>Z = 26</pre>

We now have a numeral system with a base equal to 27. We can compute a numeric value corresponding to any message:

<pre>"A " = 27</pre>
<pre>"AA" = 28</pre>
<pre>"AB" = 29</pre>
<pre>"ABC" = 786</pre>
<pre>etc.</pre>
Note: an empty message is considered equal to 0, as are messages composed only of spaces.

Permutation
Now we need a way to attribute a unique number to each of the possible permutations of our deck of playing cards.

There are few methods to enumerate permutations and assign a number to each of them, we will use the lexicographical order. For example, with three cards `A`, `B`, and `C` `(with A < B < C)` we have the ordering:

<pre>ABC = 0</pre>
<pre>ACB = 1</pre>
<pre>BAC = 2</pre>
<pre>BCA = 3</pre>
<pre>CAB = 4</pre>
<pre>CBA = 5</pre>
The first arrangement is ABC, and the last one is CBA. With our 52 playing cards – ranks sorted from the Ace to the King, and suits in alphabetical order (Clubs, Diamonds, Hearts, Spades)

King of Spades to Ace of Spades, then King of Hearts to Ace of Hearts, then King of Diamonds to Ace of Diamonds, then King of Clubs to Ace of Clubs.
To transmit a message, we will compute the permutation for which the unique number is the numeric value of the message.

Your task
Write two functions: encode, which converts a string into an ordered collection of strings representing a deck of playing cards, and decode, which does the reverse.

Cards are represented as strings of length two. The first character represents the rank, and the second character represents the suit.

Clubs:
<pre>AC 2C 3C 4C 5C 6C 7C 8C 9C TC JC QC KC</pre>
Diamonds:
<pre>AD 2D 3D 4D 5D 6D 7D 8D 9D TD JD QD KD</pre>
Hearts:
<pre>AH 2H 3H 4H 5H 6H 7H 8H 9H TH JH QH KH</pre>
Spades:
<pre>AS 2S 3S 4S 5S 6S 7S 8S 9S TS JS QS KS</pre>

All provided inputs will be valid.

A preloaded function which prints the deck to the console has been provided:

printDeck(deck, unicode)
The first argument is the deck to print, the second one is a boolean value allowing the selection of the character set: regular or Unicode (for which a font containing the playing cards characters needs to be installed on your system).

Examples
Encoding
`encode("ATTACK TONIGHT ON CODEWARS")`
should return this array of 52 strings:

`[
    "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "TC", "JC", "QC", "KC",
    "AD", "2D", "3D", "4D", "5D", "6D", "JD", "9D", "7S", "9S", "QD", "5S", "TH",
    "7D", "TS", "QS", "2H", "JS", "6H", "3S", "6S", "TD", "8S", "2S", "8H", "7H",
    "4S", "4H", "3H", "5H", "AS", "KH", "QH", "9H", "KD", "KS", "JH", "8D", "AH"
]`

Decoding
`decode([
    "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "TC", "JC", "QC", "KC",
    "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "TD", "JD", "QD", "KD",
    "AH", "2H", "3H", "4H", "8H", "9S", "3S", "2S", "8S", "TS", "QS", "9H", "7H",
    "KH", "AS", "JH", "4S", "KS", "JS", "5S", "TH", "7S", "6S", "5H", "QH", "6H"
])`

should return the string:

`"ATTACK APPROVED"`

Have fun!
I hope you enjoy this kata! Feedback and translations are very welcome.

Further reading
Logarithm
The logarithm function can be used to obtain the number of digits required to represent a number in a given base. For example, `log2(52!) = 225.58`, so we can store 225 bits of information in a deck of cards (and 226 bits are needed to represent the value of 52!). Also, `log27(52!) = 47.44`, so we can store 47 characters of our alphabet in a deck of cards (and some message with 48 characters, but not all of them).
