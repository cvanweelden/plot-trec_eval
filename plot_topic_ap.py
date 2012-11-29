from eval_results import EvaluationResult
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sys
import re

def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)

def usage():
    print "Plot AP per topic for 1 run or per-topic difference for 2 runs."
    print 
    print "Usage: python plot_topic_ap.py [-h] [-f OUTFILE] FILE1 [FILE2]"
    print
    print "Options:"
    print "-h Show this help message and exit."
    print "-f FILENAME Save the figure to specified file."
    print "-s Sort the topics in descending AP/difference."
    print
    print "When passing two files the plotted difference is FILE1 - FILE2."

if "-h" in sys.argv:
    usage()
    sys.exit()

outfile = 'topic_ap.pdf'
if "-f" in sys.argv:
    idx = sys.argv.index("-f")
    outfile = sys.argv[idx+1]
    del sys.argv[idx:idx+2]

sort_on_AP = False
if "-s" in sys.argv:
    sort_on_AP = True
    sys.argv.remove("-s")

if len(sys.argv) == 2: #plot single run
    r = EvaluationResult(sys.argv[1])
    topic_names = natural_sort(r.queries.keys())
    AP = np.array([r.queries[q]["map"] for q in topic_names])
    ylabel = "Average Precision"
elif len(sys.argv) == 3: #plot two runs
    r1 = EvaluationResult(sys.argv[1])
    r2 = EvaluationResult(sys.argv[2])
    
    assert all([k in r2.queries for k in r1.queries.keys()]), "Topic set is not the same!"
    assert all([k in r1.queries for k in r2.queries.keys()]), "Topic set is not the same!"
    
    topic_names = natural_sort(r1.queries.keys())
    
    ap1 = np.array([r1.queries[q]["map"] for q in topic_names])
    ap2 = np.array([r2.queries[q]["map"] for q in topic_names])
    
    AP = ap1 - ap2
    ylabel = "Average Precision difference"
else: #Not enough/unknown arguments
    usage()
    sys.exit()


if sort_on_AP:
    topic_names = [n for (d,n) in sorted(zip(AP,topic_names), reverse=True)]
    AP = sorted(AP, reverse=True)

ind = np.arange(len(topic_names))
width = 1.0
rects = plt.bar(ind, AP, width)
plt.xticks(ind+0.5*width, topic_names, fontsize=10, rotation='vertical')
plt.ylabel(ylabel)
plt.xlabel("Topic")

plt.savefig(outfile,  bbox_inches='tight')




