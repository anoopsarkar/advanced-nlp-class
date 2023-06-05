---
layout: default
img: loch_fyne
img_link: "https://aclanthology.org/W17-5525.pdf"
caption: Pictorial representation of the meaning representation for the E2E table to text generation task
title: Homework 2 | Prefix Tuning for Text Generation
active_tab: homework
---

# Homework 2: Prefix Tuning for Text Generation

<span class="text-info">Start on {{ site.hwdates[2].startdate }}</span> |
<span class="text-warning">Due on {{ site.hwdates[2].deadline }}</span>

## Getting Started

If you have already cloned my homework repository `nlp-class-hw` for
previous homeworks then go into that directory and update the directory:

    git pull origin/master
    cd nlp-class-hw/prefixtune

If you don't have that directory anymore then simply clone the
repository again:

    git clone https://github.com/anoopsarkar/nlp-class-hw.git

Clone your own repository from GitLab if you haven’t done it already:

    git clone git@csil-git1.cs.surrey.sfu.ca:USER/advnlpclass-{{ site.semcode }}-g-GROUP.git

Note that the `USER` above is the SFU username of the person in
your group that set up the GitLab repository.

Then copy over the contents of the `prefixtune` directory into your
`hw2` directory in your repository.

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


## Data set


## Data files

The data files provided are:

* `data/train.txt.gz` -- the training data used to train the `answer/default.py` model
* `data/input` -- input files `dev.txt` and `test.txt` infected with noise
* `data/reference/dev.out` -- the reference output for the `dev.txt` input file

## Default solution

The default solution is provided in `answer/default.py`. To use the default
as your solution:

    cd answer
    cp default.py prefixtune.py
    cp default.ipynb prefixtune.ipynb
    cd ..
    python3 zipout.py
    python3 check.py

The default solution will look for the file `prefixtune.pt`
in the data directory. If it does not find this file it
will start training on the `data/train.txt.gz` file. This
will take about 15-20 minutes.

You can also download the [`prefixtune.pt` model
file](https://drive.google.com/file/d/1Cob8vewgpvNhJ2KnZlYq2Tntkgc0l2yx/view)
that was trained using `default.py`.

Please do not commit the file into your git repository as it is
moderately large and you can go over your disk quota. 

If you have a `prefixtune.pt` in the `data` directory then you can simply run:

    python3 answer/default.py > output.txt

And then you can check the score on the dev output file called `output.txt` by running:

    python3 conlleval.py -o output.txt

which produces the following detailed evaluation:

    processed 23663 tokens with 11896 phrases; found: 11847 phrases; correct: 10764.
    accuracy:  94.01%; (non-O)
    accuracy:  94.37%; precision:  90.86%; recall:  90.48%; FB1:  90.67
                 ADJP: precision:  79.29%; recall:  69.47%; FB1:  74.06  198
                 ADVP: precision:  74.25%; recall:  74.62%; FB1:  74.44  400
                CONJP: precision:  66.67%; recall:  85.71%; FB1:  75.00  9
                 INTJ: precision: 100.00%; recall: 100.00%; FB1: 100.00  1
                   NP: precision:  90.22%; recall:  91.57%; FB1:  90.89  6330
                   PP: precision:  96.80%; recall:  94.31%; FB1:  95.54  2378
                  PRT: precision:  80.56%; recall:  64.44%; FB1:  71.60  36
                 SBAR: precision:  92.27%; recall:  75.53%; FB1:  83.06  194
                   VP: precision:  90.48%; recall:  90.36%; FB1:  90.42  2301
    (90.85844517599392, 90.48419636852724, 90.67093459124794)

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
assuming that you are in the `nlp-class-hw/prefixtune` directory or
if you have the `data` directory in your current directory with the
training data and the model file:

    from default import *
    prefixtune = FinetuneTagger('data/prefixtune', '.pt', 'distilbert-base-uncased')
    print(prefixtune.model_str())

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

## Implementing the model

## Required files

You must create the following files:

* `answer/prefixtune.py` -- this is your solution to the homework. start by copying `default.py` as explained below.
* `answer/prefixtune.ipynb` -- this is the iPython notebook that will be your write-up for the homework.

## Run your solution on the data files

To create the `output.zip` file for upload to Coursys do:

    python3 zipout.py

For more options:

    python3 zipout.py -h

## Check your accuracy

To check your accuracy on the dev set:

    python3 check.py

The output score is the BLEU score.

    python3 check.py -h

In particular use the log file to check your output evaluation:

    python3 check.py -l log

The accuracy on `data/input/test.txt` will not be shown.  We will
evaluate your output on the test input after the submission deadline.

## Submit your homework on Coursys

Once you are done with your homework submit all the relevant materials
to Coursys for evaluation.

### Create output.zip

Once you have a working solution in `answer/prefixtune.py` create
the `output.zip` for upload to Coursys using:

    python3 zipout.py

### Create source.zip

To create the `source.zip` file for upload to Coursys do:

    python3 zipsrc.py

You must have the following files or `zipsrc.py` will complain about it:

* `answer/prefixtune.py` -- this is your solution to the homework. start by copying `default.py` as explained below.
* `answer/prefixtune.ipynb` -- this is the iPython notebook that will be your write-up for the homework.

In addition, each group member should write down a short description of what they
did for this homework in `answer/README.username`.

### Upload to Coursys

Go to `Homework 2` on Coursys and do a group submission:

* Upload `output.zip` and `source.zip`
* Make sure you have documented your approach in `answer/prefixtune.ipynb`.
* Make sure each member of your group has documented their contribution to this homework in the Python notebook.

## Grading

The grading is split up into the following components:

* dev scores (see Table below)
* test scores (see Table below)
* iPython notebook write-up 
   * Make sure that you are not using any external data sources in your solution.
   * Make sure you have implemented the fine-tuning model improvements yourself without using external libraries.
* Check if each group member has written about what they did in the Python notebook.

Your BLEU score should be equal to or greater than the score listed for the corresponding marks.

| **Score(dev)** | **Score(test)** | **Marks** | **Grade** |
| Nan  | Nan  | 0   | F  |
| 90.5 | 82   | 55  | D  |
| 91   | 83   | 60  | C- |
| 91.5 | 84   | 65  | C  |
| 92   | 85   | 70  | C+ |
| 92.5 | 86   | 75  | B- |
| 93   | 87   | 80  | B  |
| 93.5 | 88   | 85  | B+ |
| 94   | 90   | 90  | A- |
| 94.5 | 92   | 95  | A  |
| 96   | 95   | 100 | A+ |
{: .table}

The score will be normalized to the marks on Coursys for the dev and test scores.

