# -*- coding: utf-8 -*-
"""
=== Output of your friend's code: ===

['this', 'film', 'is', 'based', 'on', 'isabel', "allende's", 'not-so', 'much-better', 'novel', 'i', 'hate', 'meryl', 'streep', 'and', 'antonio', 'banderas', 'in', 'non-spanish', 'films', 'and', 'the', 'other', 'actors', 'including', 'winona', 'my', 'favourite', 'actress', 'and', 'jeremy', 'irons', 'try', 'hard', 'to', 'get', 'over', 'such', 'a', 'terrible', 'script']

"""

ample_input = """
There is no way to describe how really, really, really bad this movie is. It's a shame that I actually sat through this movie, this very tiresome and predictable movie. What's wrong with it? Acting: There is not one performance that is even remotely close to even being sub-par (at least they are all very pretty). Soundtrack (songs): "If we get Orgy on the soundtrack then everyone will know that they are watching a horror film!"; Soundtrack (score): Okay, but anyone with a keyboard can make an okay soundtrack these days. Don't even get me started on the "What the hell?" moments, here are a few: Killer can move at the speed of light--door opens actress turns, no one is there, turns back, there is something sitting in front of her.; Out of now where The killer shows up with a power drill, a really big one! The filmmakers get points for at least plugging it in, but can I really believe that the killer took the time to find the power outlet to plug it in. I feel like one of the guards at the beginning of Holy Grail and want to say "Where'd you get the power drill?". I could go on and on about how bad this film is but I only have 1000 words. I will give this 2 out of ten stars. One star for making me laugh and another star for all the cleavage. Seriously, do not waste your time with this one.
"""

sample_input='light--door opens a not-so-much-better actress turns'

import re

#your_regex_pattern = r'^[0-9a-z][-{0,1}\'{0,1}.*][0-9a-z]$'
#your_regex_pattern = r'[a-z]\w*-{0,1}\'{0,1}[a-z]'
your_regex_pattern = r'[a-z0-9]\w*\'{0,1}-{0,1}\w*[a-z0-9]?'
your_regex_pattern = r'([a-z0-9]\w*\'{0,1}-{0,1}\w*[^-])'

#your_regex_pattern = r'[a-z0-9]\w+\'{0,1}-{0,1}?[0-9a-z^\w]+[a-z0-9]?'

sample_output_regex = re.findall(your_regex_pattern, sample_input.lower(), re.VERBOSE)
print sample_output_regex
