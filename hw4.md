---
layout: default
img: vae_signs
img_link: "https://en.wikipedia.org/wiki/Autoencoder"
caption: Variational autoencoders can be used to sample outputs from a neural network
title: Homework 4 | Variational Auto-Encoding for Sign Image Clustering
active_tab: homework
---

# Homework 4: Variational Auto-Encoding for Sign Image Clustering

<span class="text-info">Start on {{ site.hwdates[4].startdate }}</span> |
<span class="text-warning">Due on {{ site.hwdates[4].deadline }}</span>

## Getting Started

If you have already cloned my homework repository `nlp-class-hw` for
previous homeworks then go into that directory and update the directory:

    git pull origin/master
    cd nlp-class-hw/vae

If you don't have that directory anymore then simply clone the
repository again:

    git clone https://github.com/anoopsarkar/nlp-class-hw.git

Clone your own repository from GitLab if you haven’t done it already:

    git clone git@csil-git1.cs.surrey.sfu.ca:USER/advnlpclass-{{ site.semcode }}-g-GROUP.git

Note that the `USER` above is the SFU username of the person in
your group that set up the GitLab repository.

Then copy over the contents of the `vae` directory into your
`hw4` directory in your repository.

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


## Evaluation Pipeline


## Pre-trained Model

## Data files

## Default solution

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

* `answer/vae.py` -- this can be an empty file for this homework if you didn't change the pre-trained model.
* `answer/vae.ipynb` -- this is the iPython notebook that will be your write-up for the homework.

Each group member should write about what they did for this homework in the Python notebook.

### Upload to Coursys

Go to `Homework 4` on Coursys and do a group submission:

* Upload `output.zip` and `source.zip`
* Make sure you have documented your approach in `answer/vae.ipynb`.
* Make sure each member of your group has documented their contribution to this homework in the Python notebook.

## Grading

The grading is split up into the following components:

* dev scores (see Table below)
* test scores (see Table below)
* iPython notebook write-up 
   * Make sure that you are not using any external data sources in your solution.
   * Make sure you have implemented the fine-tuning model improvements yourself without using external libraries.
* Check if each group member has written about what they did in the Python notebook.

Your score should be equal to or greater than the score listed for the corresponding marks.

| **Score(dev)** | **Score(test)** | **Marks** | **Grade** |
| 0.0  | 0.0  | 0   | F  |
| 1.3  | 1.2  | 55  | D  |
| 10   | 12   | 60  | C- |
| 15   | 17   | 65  | C  |
| 17   | 20   | 70  | C+ |
| 19   | 24   | 75  | B- |
| 20   | 26   | 80  | B  |
| 22   | 28   | 85  | B+ |
| 24   | 30   | 90  | A- |
| 26   | 32   | 95  | A  |
| 30   | 35   | 100 | A+ |
{: .table}

The score will be normalized to the marks on Coursys for the dev and test scores.

