# -*- coding: utf-8 -*-
"""
Restriction sites. When an enzyme cuts the string, it does it in a certain location with respect to the target pattern. This information is encoded as a restriction site.

The way a biologist specifies the restriction site is with a special notation that embeds the cut in the pattern. For example, there is one enzyme that has a restriction site of the form, ANT|AAT, where the vertical bar, '|', shows where the enzyme will split the sequence. So, if the input DNA sequence were

   GCATAGTAATGTATTAATGGC
then there would two matches:

   GCATAGTAATGTATTAATGGC
       ^^^^^^  ^^^^^^
       match!  match!
Furthermore, there would be two cuts, since this enzyme splits its pattern in the middle (between ANT and AAT):

   GCATAGT|AATGTATT|AATGGC
       ^^^ ^^^  ^^^ ^^^
That would result in three fragments: GCATAGT, AATGTATT, and AATGGC.
Exercise 3 (5 points). Complete the function, sim_cuts(site_pattern, s), below. The first argument, site_pattern, is the biologist's restriction site pattern, e.g., ANT|AAT, where there may be an embedded cut. The second argument, s, is the DNA sequence to cut. The function should return the fragments in the sequence order.

For the preceding example,

  sim_cuts('ANT|AAT', 'GCATAGTAATGTATTAATGGC') == ['GCATAGT', 'AATGTATT', 'AATGGC']
"""
import re
def bio_to_regex(pattern_bio):
    pattern_d={'N':'.','R':'[GA]','Y':'[TC]','K':'[GT]','M':'[AC]','S':'[GC]','W':'[AT]','B':'[^A]','D':'[^C]','H':'[^G]','V':'[^T]' }
    s=''
    for i in pattern_bio:
        if i in pattern_d:
            s=s+pattern_d[i]
        else:
            s=s+i
    return s

def sim_cuts(site_pattern, s):
    pat=site_pattern.split('|')
    f=bio_to_regex(pat[0])
    b=bio_to_regex(pat[1])
    print f
    print b
    pattern=f+b
    all_pats=re.findall(pattern,s)
    print s
    print all_pats
    print s.split(all_pats[0])
    print s.split(all_pats[1])
    #ind=s.index('|')
    
    
    
sim_cuts('ANT|AAT', 'GCATAGTAATGTATTAATGGC')

