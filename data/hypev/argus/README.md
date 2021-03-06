Argus YES/NO questions dataset
==============================

This dataset is meant to support answering yes/no questions based on newspaper
snippets:

	https://github.com/AugurProject/argus

The newspaper snippets are extraced by Solr fulltext search on a custom-built
news articles database based on question keywords.  Thus, for each such
snippet, both relevancy and logic relation must be jointly determined.  There
is no direct supervision for relevancy right now; each tuple is labelled by
just whether the question is true, regardless of the supporting snippet
entailing it.

Dataset contains triplets of:
  * questions: dataset of yes/no questions, partially from mTurk,
    partially auto-generated
  * answers: gold standard answer for each question
  * sentences: sentences from our Argus news-articles
    database (The Guardian, NYtimes, and a couple of archive.org-fetched RSS
    streams from ABCnews, Reuters, etc)

Data split to train-val-test sets, same as the split used for Argus evaluation.


| Model                    | trn QAcc | val QAcc | val QF1  | tst QAcc | tst QF1   | settings
|--------------------------|----------|----------|----------|----------|-----------|----------
| avg                      | 0.931244 | 0.797530 | 0.728479 | 0.731408 | 0.649600  | (defaults)
|                          |±0.012570 |±0.006695 |±0.012416 |±0.007907 |±0.013410  |
| DAN                      | 0.949085 | 0.827096 | 0.750504 | 0.742484 | 0.666239  | ``inp_e_dropout=0`` ``inp_w_dropout=1/3`` ``deep=2`` ``pact='relu'`` ``l2reg=1e-5``
|                          |±0.013475 |±0.015297 |±0.028354 |±0.008980 |±0.018475  |
| rnn                      | 0.901008 | 0.854416 | 0.782354 | 0.798259 | 0.742293  | (defaults)
|                          |±0.018453 |±0.009075 |±0.015912 |±0.011856 |±0.018040  |
| cnn                      | 0.902398 | 0.857410 | 0.791902 | 0.796677 | 0.741328  | (defaults)
|                          |±0.019215 |±0.005197 |±0.009707 |±0.010855 |±0.019413  |
| rnncnn                   | 0.915025 | 0.852171 | 0.782774 | 0.779668 | 0.708510  | (defaults)
|                          |±0.023084 |±0.009620 |±0.016334 |±0.014759 |±0.022262  |
| attn1511                 | 0.853626 | 0.842066 | 0.772648 | 0.812500 | 0.770903  | ``sdim=2``
|                          |±0.010105 |±0.006757 |±0.011771 |±0.008588 |±0.017540  |


These results are obtained like this:

	tools/train.py avg hypev data/hypev/argus/argus_train.csv data/hypev/argus/argus_val.csv
	tools/eval.py avg hypev data/hypev/argus/argus_train.csv data/hypev/argus/argus_val.csv data/hypev/argus/argus_test.csv weights-hypev-avg-69b40732de2a1d70-0*
