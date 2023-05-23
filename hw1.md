---
layout: default
img: bratconll2k
img_link: "http://weaver.nlplab.org/~brat/demo/latest/#/not-editable/CoNLL-00-Chunking/train.txt-doc-1"
caption: Explore phrasal chunking interactively using Brat
title: Homework 3 | Robust Phrasal Chunking
active_tab: homework
---

# Homework 1: BERT Finetuning for Robust Phrasal Chunking

<span class="text-info">Start on {{ site.hwdates[1].startdate }}</span> |
<span class="text-warning">Due on {{ site.hwdates[1].deadline }}</span>

## Getting Started

If you have already cloned my homework repository `nlp-class-hw` for
previous homeworks then go into that directory and update the directory:

    git pull origin/master
    cd nlp-class-hw/bertchunker

If you don't have that directory anymore then simply clone the
repository again:

    git clone https://github.com/anoopsarkar/nlp-class-hw.git

Clone your own repository from GitLab if you haven’t done it already:

    git clone git@csil-git1.cs.surrey.sfu.ca:USER/advnlpclass-{{ site.semcode }}-g-GROUP.git

Note that the `USER` above is the SFU username of the person in
your group that set up the GitLab repository.

Then copy over the contents of the `bertchunker` directory into your
`hw3` directory in your repository.

Set up the virtual environment:

    python3.10 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt

You must use Python 3.10 (or later) for this homework.

Note that if you do not change the requirements then after you have
set up the virtual environment `venv` you can simply run the following
command to get started with your development for the homework:

    source venv/bin/activate

## Background

The syntax of a natural language, similar to the syntax of a programming language involves
the arrangement of tokens into meaningful groups. Phrasal chunking is the task of finding 
non-recursive syntactic groups of words. For example, the sentence:

> He reckons the current account deficit will narrow to only # 1.8 billion in September .

can be divided into phrasal chunks as follows[^1]:

> [NP <span style="color: DarkBlue">He</span>] 
[VP <span style="color: BlueViolet">reckons</span>] 
[NP <span style="color: DarkBlue">the current account deficit</span>] 
[VP <span style="color: BlueViolet">will narrow</span>] 
[PP <span style="color: red">to</span>] 
[NP <span style="color: DarkBlue">only # 1.8 billion</span>] 
[PP <span style="color: red">in</span>] 
[NP <span style="color: DarkBlue">September</span>] .

[^1]: *Caveat*: If you have a linguistic background, you might find the verb phrases `VP` and prepositional phrases `PP` are different from what you might be used to. In this task, the `VP` is a verb and verb modifiers like auxiliaries (`were`) or modals (`might`), and the `PP` simply contains the preposition. This difference is because of the fact that the chunks are non-recursive (cannot contain other phrases) -- we need trees for full syntax.

## Data set

The train and test data consist of three columns separated by spaces.
Each word has been put on a separate line and there is an empty
line after each sentence.

The first column contains the current word, the second column is
the part-of-speech tag for that word, and the third column is
the chunk tag.

Here is an example of the file format:

    He        PRP  B-NP
    reckons   VBZ  B-VP
    the       DT   B-NP
    current   JJ   I-NP
    account   NN   I-NP
    deficit   NN   I-NP
    will      MD   B-VP
    narrow    VB   I-VP
    to        TO   B-PP
    only      RB   B-NP
    #         #    I-NP
    1.8       CD   I-NP
    billion   CD   I-NP
    in        IN   B-PP
    September NNP  B-NP
    .         .    O

The chunk tags contain the name of the chunk type, for example I-NP
for noun phrase words and I-VP for verb phrase words.  Most chunk
types have two types of chunk tags, B-CHUNK for the first word of
the chunk and I-CHUNK for each other word in the chunk. See the
Appendix below for a detailed description of the part-of-speech
tags and the chunk tags in this data set. The full set of tags
for this task is in the file `data/tagset.txt`.

The sequence of labels, `B-NP`, ..., `I-NP` represents a single
phrasal chunk. For instance, the following sequence of labels:

    the       DT   B-NP
    current   JJ   I-NP
    account   NN   I-NP
    deficit   NN   I-NP

gives us the NP phrase:

> [NP <span style="color: DarkBlue">the current account deficit</span>] 

The O chunk tag is used for tokens which are not part of any chunk.

The data set comes from the Conference on Natural Language Learning:
[CoNLL 2000 shared task](http://www.cnts.ua.ac.be/conll2000/chunking/)[^2].

[^2]: [Introduction to the CoNLL-2000 Shared Task: Chunking](https://www.aclweb.org/anthology/W00-0726/)

There is a helpful program `count_sentences.py` which allows you
to count how many sentences are in a CoNLL formatted file.

This homework is not just about phrasal chunking but **robust**
phrasal chunking. The input data in dev and test files have been
infected with noise so the input to your chunker will look like
this:

    Rqckwell NNP
    , ,
    based VBN
    in IN
    El NNP
    Segundo NNP
    , ,
    Calief. NNP
    , ,
    is VBZ
    an DT
    aerospace NN
    , ,
    electronics NNS
    , ,
    automotive JJ
    and CC
    graphics NNS
    concern VBP
    . .

As you see the words have been infected with noise so
that it contains several spelling mistakes, e.g. `Rockwell` 
is now `Rqckwell`. The training data is clean and any
model trained on the training data will treat these 
noisy words as unknown words.

The input files do not have the output chunk labels
which appear in `data/reference/dev.out` for input `data/input/dev.txt`.

## Data files

The data files provided are:

* `data/train.txt.gz` -- the training data used to train the `answer/default.py` model
* `data/input` -- input files `dev.txt` and `test.txt` infected with noise
* `data/reference/dev.out` -- the reference output for the `dev.txt` input file

## Default solution

The default solution is provided in `answer/default.py`. To use the default
as your solution:

    cd answer
    cp default.py bertchunker.py
    cp default.ipynb bertchunker.ipynb
    cd ..
    python3 zipout.py
    python3 check.py

The default solution will look for the file `chunker.pt`
in the data directory. If it does not find this file it
will start training on the `data/train.txt.gz` file. This
will take about 15-20 minutes.

You can either download the `chunker.pt` model file from:

    https://drive.google.com/file/d/1Cob8vewgpvNhJ2KnZlYq2Tntkgc0l2yx/view

Please do not commit the file into your git repository as it is
moderately large and you can go over your disk quota. 

If you have a `chunker.pt` in the `data` directory then you can simply run:

    python3 answer/default.py > output.txt

And then you can check the score on the dev output file called `output.txt` by running:

    python3 conlleval.py -o output.txt

which produces the following detailed evaluation:

    processed 23663 tokens with 11896 phrases; found: 13226 phrases; correct: 9689.
    accuracy:  87.04%; (non-O)
    accuracy:  87.45%; precision:  73.26%; recall:  81.45%; FB1:  77.14
                 ADJP: precision:  13.32%; recall:  53.98%; FB1:  21.37  916
                 ADVP: precision:  31.16%; recall:  58.79%; FB1:  40.73  751
                CONJP: precision:   0.00%; recall:   0.00%; FB1:   0.00  8
                 INTJ: precision:   0.00%; recall:   0.00%; FB1:   0.00  11
                  LST: precision:   0.00%; recall:   0.00%; FB1:   0.00  3
                   NP: precision:  80.58%; recall:  80.86%; FB1:  80.72  6258
                   PP: precision:  95.97%; recall:  86.93%; FB1:  91.23  2211
                  PRT: precision:  22.15%; recall:  77.78%; FB1:  34.48  158
                 SBAR: precision:  36.12%; recall:  80.17%; FB1:  49.80  526
                  UCP: precision:   0.00%; recall:   0.00%; FB1:   0.00  64
                   VP: precision:  83.75%; recall:  84.33%; FB1:  84.04  2320
    (73.25722062603963, 81.44754539340954, 77.13557837751772)

For this homework we will be scoring your solution based on the FB1 score
which is described in detail in the Accuracy section below. However the FB1
score is not the only focus. You can focus on efficiency, model size, 
experimental comparison with other approaches and many other choices.

Make sure that the command line options are kept as they are in
`answer/default.py`. You can add to them but you must not delete any
command line options that exist in `answer/default.py`.

Submitting the default solution without modification will get you
zero marks.

### The default model

The model used in `answer/default.py` is a BERT-based Transformer
model that is fine-tuned to predict the phrase chunking tags 
for each (sub-word) token. It is trained on the data provided
in `data/train.txt.gz` which has the ground truth phrase tags
for each token and these sentences are used to fine-tune the
BERT model.

The model structure can be examined using the following code,
assuming that you are in the `nlp-class-hw/chunker` directory or
if you have the `data` directory in your current directory with the
training data and the model file:

    from default import *
    chunker = FinetuneTagger('data/chunker', '.pt', 'distilbert-base-uncased')
    print(chunker.model_str())

This prints out the model:

    TransformerModel(
      (encoder): DistilBertModel(
        (embeddings): Embeddings(
          (word_embeddings): Embedding(30522, 768, padding_idx=0)
          (position_embeddings): Embedding(512, 768)
          (LayerNorm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
          (dropout): Dropout(p=0.1, inplace=False)
        )
        (transformer): Transformer(
          (layer): ModuleList(
            (0-5): 6 x TransformerBlock(
              (attention): MultiHeadSelfAttention(
                (dropout): Dropout(p=0.1, inplace=False)
                (q_lin): Linear(in_features=768, out_features=768, bias=True)
                (k_lin): Linear(in_features=768, out_features=768, bias=True)
                (v_lin): Linear(in_features=768, out_features=768, bias=True)
                (out_lin): Linear(in_features=768, out_features=768, bias=True)
              )
              (sa_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
              (ffn): FFN(
                (dropout): Dropout(p=0.1, inplace=False)
                (lin1): Linear(in_features=768, out_features=3072, bias=True)
                (lin2): Linear(in_features=3072, out_features=768, bias=True)
                (activation): GELUActivation()
              )
              (output_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
            )
          )
        )
      )
      (classification_head): Linear(in_features=768, out_features=22, bias=True)
    )

Optimizing the above parameters to find the minimum loss on the
training data by gradient descent is done automatically using Pytorch
API calls in `answer/default.py`.

### Hyperparameters

For this homework we will enforce that the base BERT model should not
be changed. Use `distilbert-base-uncased` as your base BERT model.
You can change the fine-tuning model and parameters as you wish.

### Pytorch

You will need to use some Pytorch API calls to solve this homework.
We do not expect you to already know Pytorch in great detail.
The following links will help you get started but you can learn
a lot of the Pytorch basics by understanding `default.py` and
the process of solving this homework.

Some useful links if you feel lost at the beginning:

* [60 mins intro to Pytorch](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html)
* [Introduction to the transformers library](https://huggingface.co/docs/transformers/notebooks)

Read the source code in `default.py` in detail.

## The Challenge

Your task is to _improve the accuracy as much as possible while
keeping the hyperparameters used in the default solution for the
phrasal chunker_. The score is explained in detail in the Accuracy
section below. With substantial computational resources and using
large pre-trained models (which are beyond the scope of this homework)
the [state of the art accuracy on this
dataset](https://nlpprogress.com/english/shallow_syntax.html) has
reached an F1-score above 97.5 percent (typically by using more 
information than just the training data available for this
task).

However, the numbers from that leaderboard do not apply to the dev
and test data in this homework. The dev and test data used here are
much more challenging than the standard CoNLL 2000 chunking task
because several typos have been introduced into the data (as explained
above).

## Improving the model

Here are some specific things you can try to improve the accuracy
of the fine-tuned model:

1. Improve the classification head by using a multi-layer perceptron instead of a single linear layer.
1. Use two different optimizers with different learning rates for the pre-trained encoder layers and the classification head layer.
1. Improve the output layer handling using a CRF or a mini-Transformer classification head (more details below).
1. Deal with misspellings in the dev and test data using adversarial training (more details below).

## CRF Layer

A CRF layer can look at consistent labels (e.g. `I` tags always
follow `B` tags for the same span, and other such consistencies)
and produce more coherent label sequences. Here is a pseudo-code
for a CRF layer that you can add to `default.py` (also see the
comments in the code).

1. Calculate the model prediction probability distributions (`p`) for each subword in the encoded `sentence_input` as the result of applying `softmax` to the prediction scores (`tag_space`).
1. Create a list (let's call it `R`) which will contain normalized label prediction probabilities.
1. For each index of the `sentence_input` sequence, i in (0, 1, 2, ..., `sentence_input` subword length - 1):
    - Find the model prediction probability distribution in position i (`p_i`).
    - Find the transition probability c_{i-1} from the prediction of the previous step (calculated as argmax(`p_{i-1`})) into any label for step i (you can consider a special row of `C` (e.g. the last row) to reflect on the initial transition probability in which we don't have any previous steps). Make sure c_{i-1} is a valid probability distribution using `softmax`.
    - append `(p_i+c_{i-1})/2` to `R`.
1. Convert `R` into a tensor and return its `log` as the result of the `forward` function call.

## Dealing with Misspellings

Look into adversarial training as explained in the following paper:

> [Combating Adversarial Misspellings with Robust Word Recognition](https://www.aclweb.org/anthology/P19-1561/). Danish Pruthi, Bhuwan Dhingra, Zachary C. Lipton. ACL 2019.

## Required files

You must create the following files:

* `answer/chunker.py` -- this is your solution to the homework. start by copying `default.py` as explained below.
* `answer/chunker.ipynb` -- this is the iPython notebook that will be your write-up for the homework.

## Run your solution on the data files

To create the `output.zip` file for upload to Coursys do:

    python3 zipout.py

For more options:

    python3 zipout.py -h

## Check your accuracy

To check your accuracy on the dev set:

    python3 check.py

The output score is the $F_{\beta=1}$ score or [FB1 score](https://en.wikipedia.org/wiki/F1_score)
which is the harmonic mean of the precision and recall
computed over all the output phrasal chunks.

    python3 check.py -h

In particular use the log file to check your output evaluation:

    python3 check.py -l log

The accuracy on `data/input/test.txt` will not be shown.  We will
evaluate your output on the test input after the submission deadline.

## Submit your homework on Coursys

Once you are done with your homework submit all the relevant materials
to Coursys for evaluation.

### Create output.zip

Once you have a working solution in `answer/chunker.py` create
the `output.zip` for upload to Coursys using:

    python3 zipout.py

### Create source.zip

To create the `source.zip` file for upload to Coursys do:

    python3 zipsrc.py

You must have the following files or `zipsrc.py` will complain about it:

* `answer/chunker.py` -- this is your solution to the homework. start by copying `default.py` as explained below.
* `answer/chunker.ipynb` -- this is the iPython notebook that will be your write-up for the homework.

In addition, each group member should write down a short description of what they
did for this homework in `answer/README.username`.

### Upload to Coursys

Go to `Homework 3` on Coursys and do a group submission:

* Upload `output.zip` and `source.zip`
* Make sure your `source.zip` matches your Gitlab repository.
* Make sure you have documented your approach in `answer/chunker.ipynb`.
* Make sure each member of your group has documented their contribution to this homework in `answer/README.username` where `username` is your CSIL/GitLab username.

## Grading

The grading is split up into the following components:

* dev scores (see Table below)
* test scores (see Table below)
* iPython notebook write-up 
   * Make sure that you are not using any external data sources in your solution. You must only use the provided word vector file.
   * Make sure you have implemented the semi-character RNN model yourself.
   * Do **not** change the hyperparameters for the phrasal chunker in `default.py` in the solution to the robust chunking problem.
* Check if each group member has a `answer/README.username`.

Your F-score should be equal to or greater than the score listed for the corresponding marks.

| **Score(dev)** | **Score(test)** | **Marks** | **Grade** |
| 72   | 65   | 0   | F  |
| 72.7 | 65.2 | 55  | D  |
| 73   | 65.5 | 60  | C- |
| 73.2 | 66   | 65  | C  |
| 73.5 | 66.5 | 70  | C+ |
| 73.7 | 67   | 75  | B- |
| 74   | 67.5 | 80  | B  |
| 75.5 | 68.5 | 85  | B+ |
| 76.5 | 70.5 | 90  | A- |
| 77   | 71   | 95  | A  |
| 78   | 72   | 100 | A+ |
{: .table}

The score will be normalized to the marks on Coursys for the dev and test scores.

