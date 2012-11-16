plot-trec_eval
==============

Plotting scripts for trec_eval output. Useful for reporting on IR system evaluations.

These require Python (2.6 or 2.7), [NumPy](http://numpy.scipy.org/), and [matplotlib](http://matplotlib.org/).

###Precision-recall curves

Plot precision-recall curves. These show the performance over all topics for ranked retrieval systems.

Usage: `python plot_pr_curve.py [-h] [-f OUTFILE] FILE [FILE ...]`

Options:   
`-h` Show this help message and exit.   
`-f FILENAME` Save the figure to specified file.   

Pass multiple files to plot all the runs in the same plot.

#### Example

`$ python plot_pr_curve -f pr_curve.pdf indri.eval okapi.eval`

### Per-topic AP difference

Plot per-topic difference in AP for 2 runs.

Usage: `python plot_topic_difference.py [-h] [-f OUTFILE] FILE1 FILE2`

Options:   
`-h` Show this help message and exit.   
`-f FILENAME` Save the figure to specified file.   
`-s` Sort the topics in descending difference.   

The plotted difference is FILE1 - FILE2.

#### Example

`$ python plot_topic_difference -f topic_difference.pdf indri.eval okapi.eval -s`