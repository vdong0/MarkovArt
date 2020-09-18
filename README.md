# MarkovArt

System Title: MarkovArt

To set up and run my code, simply cd into the MarkovArt project and run:

      python3 Runner.py

in the command line. This will create a png image named "CreatedImage.png" in
the project directory.

Description: My system takes in images as training data, and converts each image
into a list of (R,G,B) tuples, each tuple representing a pixel. A markov dictionary
is then created from these (R,G,B) pixel lists, the key being a string pair of
R,G,B values (because I used second-order) and this represents a 'state',
and the value being a list of (R,G,B) tuples, and this list represents all the
possible color pixels that the key state can transition to, based on the training
image data. Using this markov dictionary, I create an image by building a
(R,G,B) list based off the markov model, and then convert this RGB list into an
image.

This system is personally meaningful to me because this was one of the first
projects I've ever done where the instructions were vague. Usually, in projects
i've done in the past there are set rules and guidelines to follow, and also the
professor usually gives a template or an example to base your project off of. My
past projects had little room for me to explore because I would just blatantly
follow the guidelines, however for this project it was started fully from scratch.
I had to design the system on my own, as well as implement it fully on my own.
While my final system has a few bugs, I was able to create meaningful visual art.

While I was able to essentially convert my conceptual thoughts into code.
this posed a huge challenge for me. Designing my system on paper was quite simple,
however when I would try to implement it into code I would see issues or errors,
and then I would have to go back to the drawing board and make some modifications
to my design. I was pushed out of my comfort zone because most cases I would be
in a group, and someone else would create a design and I would just blatantly follow
my peer's design. This was one of the first projects where my system was implemented
based off MY design, and only mine. This was a very important challenge for me because
I know I cannot keep depending on others all the time; there were numerous times
during this project where I wanted to reach out to my peers for help, but I was eager
to try to implement the system solely on my own. The next steps for me is to
create a fully working system, there was a bug that I was not able to solve;
although I knew what caused the bug I did not know how to fix it. This bug did
not prevent me from creating a visual piece, however there are times when u try
to run my code and it doesn't work :(.

I believe my system is not creative mainly because it fails the turing test. My
training data was a couple of popular Vincent Van Gogh artworks, and if a person
were to see the visual art created by my system, that person would probably be able
to tell that the visual art was created by a computer system and not a human. I also
don't believe my system is that novel because while I designed it myself, I have a
feeling that others have designs in a similar fashion. 
