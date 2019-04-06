from gensim.models import KeyedVectors,Word2Vec
import string

#using the limit as 1000000 because systems hangs if full dataset is considered
model_1 = KeyedVectors.load_word2vec_format("GoogleNews-vectors-negative300.bin",binary=True, limit = 1000000)

# A new text file is being created for the conveneince of reading outputs
# the Whole Python Script is Decided into different sections all of which can be run simultaneously or modularly as per the cob=veneince
# The name of the text file is vperur.txt
file = open("readme.txt","w+")

#--------------------------------------------------------------------------------------------------------------------------#

# Question 3.1 Similarity

#Words for which we need similarity
wordsForSimilarity = ['mango','football','guitar','Google','taichi']
file.write("Question 3.1\n\n")
print("The Words Chosen for Similarity")
print(wordsForSimilarity)
file.write("The Words Chosen for Similarity are:\n")
file.writelines(["%s " %word for word in wordsForSimilarity])
file.write("\n")
for i in wordsForSimilarity:
	#finding the top ten similar words using most_similar function
	output = model_1.wv.most_similar(i, topn = 10)
	print("The 10 most similar words of [%s] along with similarity are:\n"%(i))
	print(output)
	file.write("The 10 most similar words of [%s] along with similarity are:\n"%(i))
	file.writelines(["similarWord = %s | similarity = %s\n" %(word,sim)  for word,sim in output])
	file.write("\n")

file.write("\n\n")
#--------------------------------------------------------------------------------------------------------------------------#

# Question 3.2 Antonyms

#Words for which we need to find antonyms
antonymWords = ['white','hot','obedient','small','dry']

file.write("Question 3.2\n\n")
print("The Words Chosen for Antonyms")
print(antonymWords)
file.write("The Words Chosen for Antonyms are:\n")
file.writelines(["%s " %word for word in antonymWords])
file.write("\n")
file.write("Here we are expected to find an antonym when we are calculating the 10 most similar words\n")
file.write("\n")
for i in antonymWords:
	#finding the top ten similar words using most_similar function
	output = model_1.wv.most_similar(i, topn = 10)
	print("The 10 most similar words of [%s] along with similarity are:\n"%(i))
	print(output)
	file.write("The 10 most similar words of [%s] along with similarity are:\n"%(i))
	file.writelines(["similarWord = %s | similarity = %s\n" %(word,sim)  for word,sim in output])
	file.write("\n")


#--------------------------------------------------------------------------------------------------------------------------#

# Question 4
# A function used to find the analogies given the analogies to be chosen from
# This function is used both in question 4.1 and 4.2

def findSimilarWordFromAnalogy(words_analogy):
	analogies = words_analogy.split(":")
	wordsCorpus = []
	for analogy in analogies:
		words = analogy.split()
		wordsCorpus.append(words) 
	count = 0.0
	for analogyWords in wordsCorpus:
		# temp = model_1.wv.most_similar(positive=[analogyWords[1], analogyWords[2]], negative=analogyWords[0])
		file.write("The analogy chosen is (%s : %s) :: (%s : ?)\n"%(analogyWords[0],analogyWords[1],analogyWords[2]))
		temp = model_1[analogyWords[1]] - model_1[analogyWords[0]] + model_1[analogyWords[2]]
		# finding the analogy using the similar_by_vector fuunction from gensim
		res = model_1.wv.similar_by_vector(temp, topn=4)
		result = res
		existing = [analogyWords[0].lower(),analogyWords[1].lower(),analogyWords[2].lower()]
		result  = []
		# Removing the words which we already used as analogies
		for i in res:
			if i[0].lower() not in existing:
				result.append(i)
		if result[0][0] == analogyWords[3]:
			count+=1.0
			print("Correct Output found %s"%(result[0][0]))
			file.write("Correct Output found %s\n"%(result[0][0]))
		else:
			print("Wrong Expected output %s But result is %s"%(analogyWords[3],result[0][0]))
			file.write("Wrong Expected output %s But result is %s\n"%(analogyWords[3],result[0][0]))

	accuracy = (count/len(wordsCorpus))*100
	print("The accuracy is %s\n"%(accuracy))
	file.write("The accuracy is %s \n\n"%(accuracy))

# Question 4.1 Existing Analogies
# The word_analogy are taken from word_analogy txt file

file.write("Question 4.1\n\n")
words_analogy = """Tokyo Japan London England :
Berlin Germany Madrid Spain :
Athens Greece Baghdad Iraq :
Chicago Illinois Houston Texas : 
Chicago Illinois Portland Oregon :
Houston Texas Anchorage Alaska : 
boy girl brother sister : 
boy girl husband wife : 
boy girl nephew niece : 
boy girl policeman policewoman :
husband wife king queen :
husband wife man woman :
husband wife prince princess :
husband wife son daughter :
father mother groom bride : 
father mother grandfather grandmother :
brother sister father mother :
USA dollar Europe euro : 
USA dollar India rupee :
USA dollar Algeria dinar"""

print("The results after using the equation")
findSimilarWordFromAnalogy(words_analogy)

newAnalogies  = """ Gujarat Gandhinagar Rajasthan Jaipur :
Superman Superwoman King Queen :
India Asia Italy Europe :
Cyprus Euro Russia ruble :
Maharashtra Mumbai Goa Panaji
Earth Humans Mars Martians
"""

# Question 4.2 New Analogies

print("Question 4.2\n\n")
file.write("Question 4.2\n\n")
findSimilarWordFromAnalogy(newAnalogies)





	
#--------------------------------------------------------------------------------------------------------------------------#


# Question 5
# Training Corpus Taken from wikipedia on Nature 

trainingCorpus = """Nature is the natural environment which surrounds us, cares us and nourishes us every moment. It provides us a protective layer around us to prevent from the damages. We are not able to survive on the earth without nature like air, land, water, fire and sky. Nature includes everything around us like plants, animals, river, forests, rain, lake, birds, sea, thunder, sun, moon, weather, atmosphere, mountain, desserts, hills, ice, etc. Every form of nature is very powerful which has ability to nourish as well as destroy us.
Now a day, everyone has less time to enjoy nature. In the increasing crowd we forgot to enjoy nature and improve health. We started using technological instruments for our health fitness. However it is very true that nature has power to nourish us and fit us forever. Most of the writers have described the real beauty and advantage of the nature in their writings. Nature has ability to make our mind tension free and cure our diseases. Because of technological advancement in the life of human being, our nature is declining gradually which needs a high level of awareness to keep it in balance and to conserve natural assets.
God has created everything very beautifully seeing which our eyes can never be tired. But we forgot that we too have some responsibility towards our nature to relationship between nature and human beings. How beautiful scenery it looks in morning with sunrise, songs of birds, sounds of lakes, rivers, air and happy gatherings of friends in the evening in garden after a long day of crush. But we forgot to enjoy the beauty of the nature in just fulfilling our duties towards our families.
Sometimes during our holidays we spend our whole day by watching TV, reading news paper, playing indoor games or on the computer but we forgot that outside the door we can do something interesting in the lap of nature ad natural environment. Unnecessarily we left on all the lights of home, we use electricity without need which ultimately increases the heat in the environment called global warming. Our other activities like cutting trees and forests increase the amount of CO2 gas in the environment causing green house effect and global warming.
If we want to be happy and healthy always we should try our best to save our planet and its beautiful nature by stopping our foolish and selfish activities. In order to keep ecosystem in balance we should not cut trees, forests, practice energy and water conservation and many more. Ultimately we are the real user of the nature so we should really take care of it. Nature, in the broadest sense, is the natural, physical, or material world or universe. "Nature" can refer to the phenomena of the physical world, and also to life in general. 
The study of nature is a large, if not the only, part of science. Although humans are part of nature, human activity is often understood as a separate category from other natural phenomena. 
For example, manufactured objects and human interaction generally are not considered part of nature, unless qualified as, for example, "human nature" or "the whole of nature". This more traditional concept of natural things which can still be found today implies a distinction between the natural and the artificial, with the artificial being understood as that which has been brought into being by a human consciousness or a human mind. Depending on the particular context, the term "natural" might also be distinguished from the unnatural or the supernatural. 
To go into solitude, a man needs to retire as much from his chamber as from society. I am not solitary whilst I read and write, though nobody is with me. But if a man would be alone, let him look at the stars. The rays that come from those heavenly worlds, will separate between him and what he touches. One might think the atmosphere was made transparent with this design, to give man, in the heavenly bodies, the perpetual presence of the sublime. Seen in the streets of cities, how great they are! If the stars should appear one night in a thousand years, how would men believe and adore; and preserve for many generations the remembrance of the city of God which had been shown! But every night come out these envoys of beauty, and light the universe with their admonishing smile.
The stars awaken a certain reverence, because though always present, they are inaccessible; but all natural objects make a kindred impression, when the mind is open to their influence. Nature never wears a mean appearance. Neither does the wisest man extort her secret, and lose his curiosity by finding out all her perfection. Nature never became a toy to a wise spirit. The flowers, the animals, the mountains, reflected the wisdom of his best hour, as much as they had delighted the simplicity of his childhood.
When we speak of nature in this manner, we have a distinct but most poetical sense in the mind. We mean the integrity of impression made by manifold natural objects. It is this which distinguishes the stick of timber of the wood-cutter, from the tree of the poet. The charming landscape which I saw this morning, is indubitably made up of some twenty or thirty farms. Miller owns this field, Locke that, and Manning the woodland beyond. But none of them owns the landscape. There is a property in the horizon which no man has but he whose eye can integrate all the parts, that is, the poet. This is the best part of these men's farms, yet to this their warranty-deeds give no title.
To speak truly, few adult persons can see nature. Most persons do not see the sun. At least they have a very superficial seeing. The sun illuminates only the eye of the man, but shines into the eye and the heart of the child. The lover of nature is he whose inward and outward senses are still truly adjusted to each other; who has retained the spirit of infancy even into the era of manhood. His intercourse with heaven and earth, becomes part of his daily food. In the presence of nature, a wild delight runs through the man, in spite of real sorrows. Nature says, -- he is my creature, and maugre all his impertinent griefs, he shall be glad with me. Not the sun or the summer alone, but every hour and season yields its tribute of delight; for every hour and change corresponds to and authorizes a different state of the mind, from breathless noon to grimmest midnight. Nature is a setting that fits equally well a comic or a mourning piece. In good health, the air is a cordial of incredible virtue. Crossing a bare common, in snow puddles, at twilight, under a clouded sky, without having in my thoughts any occurrence of special good fortune, I have enjoyed a perfect exhilaration. I am glad to the brink of fear. In the woods too, a man casts off his years, as the snake his slough, and at what period soever of life, is always a child. In the woods, is perpetual youth. Within these plantations of God, a decorum and sanctity reign, a perennial festival is dressed, and the guest sees not how he should tire of them in a thousand years. In the woods, we return to reason and faith. There I feel that nothing can befall me in life, -- no disgrace, no calamity, (leaving me my eyes,) which nature cannot repair. Standing on the bare ground, -- my head bathed by the blithe air, and uplifted into infinite space, -- all mean egotism vanishes. I become a transparent eye-ball; I am nothing; I see all; the currents of the Universal Being circulate through me; I am part or particle of God. The name of the nearest friend sounds then foreign and accidental: to be brothers, to be acquaintances, -- master or servant, is then a trifle and a disturbance. I am the lover of uncontained and immortal beauty. In the wilderness, I find something more dear and connate than in streets or villages. In the tranquil landscape, and especially in the distant line of the horizon, man beholds somewhat as beautiful as his own nature.
The greatest delight which the fields and woods minister, is the suggestion of an occult relation between man and the vegetable. I am not alone and unacknowledged. They nod to me, and I to them. The waving of the boughs in the storm, is new to me and old. It takes me by surprise, and yet is not unknown. Its effect is like that of a higher thought or a better emotion coming over me, when I deemed I was thinking justly or doing right.
Yet it is certain that the power to produce this delight, does not reside in nature, but in man, or in a harmony of both. It is necessary to use these pleasures with great temperance. For, nature is not always tricked in holiday attire, but the same scene which yesterday breathed perfume and glittered as for the frolic of the nymphs, is overspread with melancholy today. Nature always wears the colors of the spirit. To a man laboring under calamity, the heat of his own fire hath sadness in it. Then, there is a kind of contempt of the landscape felt by him who has just lost by death a dear friend. The sky is less grand as it shuts down over less worth in the population."""

# Here I have removed stop words because they are insignificant for similarity
stopwords = """i
me
my
myself
we
our
ours
ourselves
you
your
yours
yourself
yourselves
he
him
his
himself
she
her
hers
herself
it
its
itself
they
them
their
theirs
themselves
what
which
who
whom
this
that
these
those
am
is
are
was
were
be
been
being
have
has
had
having
do
does
did
doing
a
an
the
and
but
if
or
because
as
until
while
of
at
by
for
with
about
against
between
into
through
during
before
after
above
below
to
from
up
down
in
out
on
off
over
under
again
further
then
once
here
there
when
where
why
how
all
any
both
each
few
more
most
other
some
such
no
nor
not
only
own
same
so
than
too
very
s
t
can
will
just
don
should
now"""
stopWords = stopwords.split("\n")
# print(stopWords)
newTestSentences = trainingCorpus.split(".")
tempSentences = []
# Removing the punctuations marks using translate
for i in newTestSentences:
	te = i.translate(None, string.punctuation)
	te = te.lower()
	tempSentences.append(te)
sentences = []
for sentence in tempSentences:
	te = sentence.split()
	sentences.append(te)

sentences.pop()
newSentences = []
for i in sentences:
	te = []
	for word in i:
		if word not in stopWords:
			te.append(word)
	newSentences.append(te)
# print(newSentences)
model_2 = Word2Vec(size = 50,min_count = 1)
model_2.build_vocab(newSentences)
model_2.train(newSentences, total_examples=model_2.corpus_count, epochs=200)

# words taken for considering similarity
testWords = ["nature","crowd","man","sun","humans"]
file.write("Question 5\n\n")
print("The Words Chosen for Similarity")
print(testWords)
file.write("The Words Chosen for Similarity are:\n")
file.writelines(["%s " %word for word in testWords])
file.write("\n")
for i in testWords:
	#finding the top ten similar words using most_similar function
	output = model_2.wv.most_similar(i, topn = 10)
	print("The 10 most similar words of [%s] along with similarity are:\n"%(i))
	print(output)
	file.write("The 10 most similar words of [%s] along with similarity are:\n"%(i))
	file.writelines(["similarWord = %s | similarity = %s\n" %(word,sim)  for word,sim in output])
	file.write("\n")
file.write("\n\n")
