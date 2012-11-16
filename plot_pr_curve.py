from eval_results import EvaluationResult
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sys

if len(sys.argv) < 2 or "-h" in sys.argv:
    print "Plot precision-recall curves."
    print
    print "Usage: python plot_pr_curve.py [-h] [-f OUTFILE] FILE [FILE ...]"
    print
    print "Options:"
    print "-h Show this help message."
    print "-f FILENAME Save the figure to specified file."
    print
    print "Pass multiple files to plot all the runs in the same plot."

if "-h" in sys.argv:
    sys.argv.remove("-h")

outfile = 'pr_curve.pdf'
if "-f" in sys.argv:
    idx = sys.argv.index("-f")
    outfile = sys.argv[idx+1]
    del sys.argv[idx:idx+2]

resultlist = [EvaluationResult(f) for f in sys.argv[1:]]

names = [r.runid for r in resultlist]
iprec = [[r.results[ "iprec_at_recall_0.00"],
         r.results["iprec_at_recall_0.10"],
         r.results["iprec_at_recall_0.20"],
         r.results["iprec_at_recall_0.30"],
         r.results["iprec_at_recall_0.40"],
         r.results["iprec_at_recall_0.50"],
         r.results["iprec_at_recall_0.60"],
         r.results["iprec_at_recall_0.70"],
         r.results["iprec_at_recall_0.80"],
         r.results["iprec_at_recall_0.90"],
         r.results["iprec_at_recall_1.00"]] for r in resultlist]

recall = np.arange(0,1.1,0.1)

plt.xlabel("Recall")
plt.ylabel("Interpolated Precision")

for p in iprec:
    plt.plot(recall, p)

plt.legend(names)
plt.savefig(outfile,  bbox_inches='tight')








