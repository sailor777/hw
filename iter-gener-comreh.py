from time import time
from os import system
<<<<<<< HEAD
import itertools
=======
>>>>>>> b61b6a194d207306fb98d5a19275a0e4c197f005

sumb = 0
result = []
fw = open('result.log','w')

def eval_byte_sum(fname):
    f = open(fname,'r')
    start_t = time()
    sumb = sum((int(line.split()[-1]) for line in f if line.split()[-1].isdigit()))
<<<<<<< HEAD
                    #if line.split()[-1] != '-' or line.split()[-1] != ''])
    end_t = time() - start_t
    fw.write('Sum = {} bytes of {} by sum() time = {} second\n'.format(sumb,f.name,end_t))
=======
    end_t = time() - start_t
    fw.write('Sum = {} bytes of {} by sum() time = {} s\n'.format(sumb,f.name,end_t))
>>>>>>> b61b6a194d207306fb98d5a19275a0e4c197f005
    f.close()
    return 0

def count_word(fname,word):
    f = open(fname,'r')
    start_t = time()
    sumb = sum((line.count(word) for line in f))
    end_t = time() - start_t
<<<<<<< HEAD
    fw.write('Find {} word {} in {}, time = {} second\n' \
=======
    fw.write('Find {} word {} in {}, time = {} s\n' \
>>>>>>> b61b6a194d207306fb98d5a19275a0e4c197f005
            .format(sumb,word,f.name,end_t))
    f.close()
    return 0

def replace_word(fname,word1,word2):
    result = ''
    f = open(fname,'r')
    fnew = open(fname + '_new','w')
    start_t = time()
    result = [fnew.write(line.replace(word1,word2)) for line in f]
    end_t = time() - start_t
<<<<<<< HEAD
    fw.write('Replace {} => {} in {}, new file = {}, time = {} second\n' \
=======
    fw.write('Replace {} => {} in {}, new file = {}, time = {} s\n' \
>>>>>>> b61b6a194d207306fb98d5a19275a0e4c197f005
            .format(word1,word2,f.name,fnew.name,end_t))
    del result
    f.close()
    fnew.close()
    return 0

eval_byte_sum('user.log')
eval_byte_sum('user1.log')
count_word('user.log','GET')
count_word('user1.log','GET')
replace_word('user.log','GET','POST')
replace_word('user1.log','POST','GET')
fw.close()
system('cat result.log')
