---
layout: default
img: model_sizes
img_link: "https://babylm.github.io"
caption: Datasets have grown by orders of magnitude remarkably quickly
title: Homework 3 | BabyLM Challenge
active_tab: homework
---

# Homework 3: BabyLM Challenge

<span class="text-info">Start on {{ site.hwdates[3].startdate }}</span> |
<span class="text-warning">Due on {{ site.hwdates[3].deadline }}</span>

## Getting Started

If you have already cloned my homework repository `nlp-class-hw` for
previous homeworks then go into that directory and update the directory:

    git pull origin/master
    cd nlp-class-hw/babylm

If you don't have that directory anymore then simply clone the
repository again:

    git clone https://github.com/anoopsarkar/nlp-class-hw.git

Clone your own repository from GitLab if you haven’t done it already:

    git clone git@csil-git1.cs.surrey.sfu.ca:USER/advnlpclass-{{ site.semcode }}-g-GROUP.git

Note that the `USER` above is the SFU username of the person in
your group that set up the GitLab repository.

Then copy over the contents of the `babylm` directory into your
`hw3` directory in your repository.

Set up the virtual environment:

    python3.10 -m venv venv
    source venv/bin/activate

You must use Python 3.10 (or later) for this homework.

## Background

The goal for this homework is to get started with the zero-shot
task for the BabyLM challenge.

> [BabyLM Challenge: Sample-efficient pretraining on a developmentally
  plausible corpus.](https://arxiv.org/abs/2301.11796). Alex Warstadt,
  Leshem Choshen, Aaron Mueller, Adina Williams, Ethan Wilcox, Chengxu
  Zhuang.

The BabyLM challenge evaluates language models in three categories:
strict, strict-small and loose.

Strict: you are allowed to train on ~100M words of English language
data.

Loose: similar to Strict and you are allowed to train on ~100M words
of English language data but unlimited non-linguistic data (images,
videos, etc.).

Strict-small: you are allowed to train on ~10M words of English
language data.

For this homework we will be using the Strict-small setting only.

The dataset for training the language models are available from this URL:

     https://github.com/babylm/babylm.github.io/raw/main/babylm_data.zip

You should use only the data in the `babylm_data/babylm_10M` directory
for this homework which contains the following files:

    aochildes.train         cbt.train
    gutenberg.train         qed.train
    switchboard.train       bnc_spoken.train
    children_stories.train  open_subtitles.train
    simple_wikipedia.train  wikipedia.train

A pre-trained language model which was trained on the `babylm_10M`
data is available from this link:

Zero-shot evaluation in the BabyLM challenge involves evaluating a
large language model on just one task: the BLiMP task.

> [BLiMP: The Benchmark of Linguistic Minimal Pairs for
  English](https://arxiv.org/abs/1912.00582). Alex Warstadt, Alicia
  Parrish, Haokun Liu, Anhad Mohananey, Wei Peng, Sheng-Fu Wang,
  Samuel R. Bowman. TACL 2023.

Once you have accomplished zero-shot evaluation, you are encouraged
to also try the fine-tuning tasks such as SuperGLUE, but fine-tuning
your BabyLM is not required for this homework.

## Evaluation Pipeline

The main goal of this homework is to set up the evaluation pipeline
for the BabyLM challenge and submit the scores you get on the BLiMP
task as your deliverable for this homework.

The rationale behind this homework is to get you started on a
plausible project activity even if you do not eventually use the
BabyLM challenge as part of your project.

The first step is to clone the official evaluation pipeline for the
BabyLM challenge and expand the necessary data files for the
evaluation. Make sure you are in the `nlp-class-hw/babylm` directory
when you clone the BabyLM github repository:

    cd nlp-class-hw/babylm
    source venv/bin/activate # see intro section
    git clone https://github.com/babylm/evaluation-pipeline
    cd evaluation-pipeline
    unzip filter_data.zip
    pip install -U .

On line 49 of the file `babylm_eval.py` change from `cuda` to `cpu`
if you are going to run the evaluation without using a GPU. You
might want to use your own GPU or the ones in CSIL or the free GPUs
available on Google CoLab. Note that it takes between 4-6 hours to
finish the zero-shot evaluation on the BLiMP data on a CPU. Speed
can be improved easily to 30-60 mins by doing each section of BLiMP
in parallel but that is not currently supported by the official
evaluation pipeline.

There is also a CoLab demo of the evaluation pipeline available here:

    https://colab.research.google.com/drive/1HX2D3wztO81tKcqCeV_ecRcEUseBVuTc?usp=sharing

## Pre-trained Model

A pre-trained model trained on the `babylm_10M` data (see above for
details) has been made available for you so you don't need to train
a new model from scratch on the 10M data. Follow the link below to
download the model:

    https://drive.google.com/drive/folders/1M85dyfSngIrChY4u-w2jCtSxC60mHZJz?usp=sharing

When downloaded keep the directory `roberta-base-strict-small`
inside the `evaluation-pipeline` directory where you checked out
the BabyLM evaluation pipeline repository.

You can run the unmodified pre-trained model through the evaluation pipeline as follows:

    python babylm_eval.py "roberta-base-strict-small" "encoder" > babylm_eval.output

This will produce scores on the BLiMP task:

    Scores:
    anaphor_agreement:         81.54%
    argument_structure:        67.12%
    binding:                   67.26%
    control_raising:           67.85%
    determiner_noun_agreement: 90.75%
    ellipsis:                  76.44%
    filler_gap:                63.48%
    irregular_forms:           87.43%
    island_effects:            39.87%
    npi_licensing:             55.92%
    quantifiers:               70.53%
    subject_verb_agreement:    65.42%

It will also create the directories and files in:
`babylm/roberta-base-strict-small/zeroshot/` for each of the BLiMP subtasks.

Make sure you have the following directory contents before running `zipout.py`:

    ls evaluation-pipeline/babylm/roberta-base-strict-small/zeroshot/

Should show you these files:

    anaphor_agreement   binding           determiner_noun_agreement
    filler_gap          island_effects    quantifiers
    argument_structure  control_raising   ellipsis
    irregular_forms     npi_licensing     subject_verb_agreement

The directory name `roberta-base-strict-small` could be different
depending on your pre-trained language model name.

Keep this directory intact since `zipout.py` will be using the above
directory to prepare you homework submission.

**Warning**: the time taken for the basic evaluation (shown above)
is about 6 hours on a CPU. It is substantially faster if you have
access to a GPU.

## Data files

The data files for this homework are:

* The official evaluation pipeline for BabyLM: `https://github.com/babylm/evaluation-pipeline`
* The dataset for the various LM sizes for this challenge: `https://github.com/babylm/babylm.github.io/raw/main/babylm_data.zip`
* A pre-trained model on the Strict-small BabyLM data: `https://drive.google.com/drive/folders/1M85dyfSngIrChY4u-w2jCtSxC60mHZJz?usp=sharing`

## Default solution

There is no default solution except for the evaluation pipeline
provided by the BabyLM challenge (as described above).

However, any code you write to improve the pre-trained language
model or train a new language model on the Strict-small data should
be added to the `answer` directory.

You still have `zipout.py` and `check.py` to submit your final
evaluation scores on the zero-shot task for the BabyLM challenge,
which is the BLiMP evaluation.

    python3 zipout.py

This should create an `output.zip` file from the evaluation
scores computed by the `evaluation-pipeline`. This should be
very quick since all the hard work was already done during
the evaluation phase.

Next you can check the overall score by running `check.py`:

    python3 check.py

Which should return a macro-average accuracy score for 
the entire BLiMP task (e.g.):

    score: 75.0570 

For this homework, it is acceptable to submit the evaluation scores
produced by the provided pre-trained model, since this homework is
to evaluate if you can get started on a project and run the evaluation
pipeline to evaluate your project work on standard benchmark
dataset(s).

## The Challenge

Since the BLiMP task involves various pairwise comparison tasks
based on the language model score your best bet to improve the
discriminative power of the language model to changes in
the grammar of the sentence. Here are some ideas, but there
are many equally good ideas you can come up with:

* The classification task uses the `[CLS]` token (in RoBERTa this is actually `<s>`). So creating a fine-tuning task for the strict small model that allows it to discriminate between corrupted sentences (by replacing a content word like a verb, noun or adjective at random with another content word) and also allows it to recognize benign changes that do not make the sentence ungrammatical (replacing a content word with a synonym from Wordnet).
* Use an ELECTRA model to train a discriminator that should do better on the BLiMP task.
* Fine-tune the strict small model on the BLiMP data (this is technically cheating, but it would be interesting to see if fine-tuning helps). If fine-tuning on BLiMP helps, then try using an online LLM service to generate fine-tuning data for your small model to do better on the BLiMP task.
* Since the BLiMP task is about recognizing syntax errors it might help to read the background on each sub-task and tailor the fine-tuning for each sub-task differently for higher accuracy.

One thing to keep in mind is that your first evaluation on the
provided pre-trained model is going to be sufficient to get you a
pretty good grade on this homework. If you want to aim for higher
than that, you can pursue one of the above ideas or some of your
own.

## Submit your homework on Coursys

Once you are done with your homework submit all the relevant materials
to Coursys for evaluation.

### Create output.zip

Once you have run the BabyLM evaluation pipeline create `output.zip`
for upload to Coursys using:

    python3 zipout.py

### Create source.zip

To create the `source.zip` file for upload to Coursys do:

    python3 zipsrc.py

You must have the following files or `zipsrc.py` will complain about it:

* `answer/babylm.py` -- this can be an empty file for this homework if you didn't change the pre-trained model.
* `answer/babylm.ipynb` -- this is the iPython notebook that will be your write-up for the homework.

Each group member should write about what they did for this homework in the Python notebook.

### Upload to Coursys

Go to `Homework 3` on Coursys and do a group submission:

* Upload `output.zip` and `source.zip`
* Make sure you have documented your approach in `answer/babylm.ipynb`.
* Make sure each member of your group has documented their contribution to this homework in the Python notebook.

## Grading

The grading is split up into the following components:

* evaluation scores (see Table below)
* iPython notebook write-up 
   * Make sure that you are not using any external data sources in your solution.
   * Make sure you have implemented the fine-tuning model improvements yourself without using external libraries.
* Check if each group member has written about what they did in the Python notebook.

Your score should be equal to or greater than the score listed for the corresponding marks.

| **Score** | **Marks** | **Grade** |
| 25  | 0   | F  |
| 30  | 55  | D  |
| 35  | 60  | C- |
| 40  | 65  | C  |
| 45  | 70  | C+ |
| 50  | 75  | B- |
| 55  | 80  | B  |
| 60  | 85  | B+ |
| 65  | 90  | A- |
| 69  | 95  | A  |
| 75  | 100 | A+ |
{: .table}

