from eval_results import EvaluationResult
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sys


def usage():
    print "Plot per-topic difference in AP for 2 runs."
    print 
    print "Usage: python plot_pr_curve.py [-h] [-f OUTFILE] FILE1 FILE2"
    print
    print "Options:"
    print "-h Show this help message and exit."
    print "-f FILENAME Save the figure to specified file."
    print "-s Sort the topics in descending difference."
    print
    print "The plotted difference is FILE1 - FILE2."

if "-h" in sys.argv:
    usage()
    sys.exit()

outfile = 'topic_difference.pdf'
if "-f" in sys.argv:
    idx = sys.argv.index("-f")
    outfile = sys.argv[idx+1]
    del sys.argv[idx:idx+2]

sort_on_difference = False
if "-s" in sys.argv:
    sort_on_difference = True
    sys.argv.remove("-s")

if not len(sys.argv) == 3:
    usage()
    sys.exit()

r1 = EvaluationResult(sys.argv[1])
r2 = EvaluationResult(sys.argv[2])

assert all([k in r2.queries for k in r1.queries.keys()]), "Topic set is not the same!"
assert all([k in r1.queries for k in r2.queries.keys()]), "Topic set is not the same!"

topic_names = sorted(r1.queries.keys())

ap1 = np.array([r1.queries[q]["map"] for q in topic_names])
ap2 = np.array([r2.queries[q]["map"] for q in topic_names])

diff = ap1 - ap2

if sort_on_difference:
    topic_names = [n for (d,n) in sorted(zip(diff,topic_names), reverse=True)]
    diff = sorted(diff, reverse=True)

ind = np.arange(len(topic_names))
width = 1.0
rects = plt.bar(ind, diff, width)
plt.xticks(ind+0.5*width, topic_names, fontsize=10, rotation='vertical')
plt.ylabel("Average Precision")
plt.xlabel("Topic")

plt.savefig(outfile,  bbox_inches='tight')




