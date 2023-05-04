---
layout: default
img: C-3PO
img_link: "http://en.wikipedia.org/wiki/Languages_in_Star_Wars"
caption: "In Star Wars, C-3PO is fluent in over six million forms of communication."
title: Course Information
active_tab: main_page 
---

## Advanced Methods in NLP <span class="text-muted">Summer 2023</span>

Deep learning for NLP has been successful at improving results on
many NLP tasks by relying on scaling up models, and as a consequence
the models that scale better are the ones that are studied and used
both in research and in industry. This course will be focused on
current advanced methods that are considered state-of-the-art in
NLP. These approaches are built on the Transformer model which gets
rid of difficult-to-train recurrent models in favor of positional
encoding, multi-headed self-attention and various techniques to
allow training multiple feed-forward layers scaling to millions and
even trillions of parameters. This course will focus on the various
aspects of training large models on natural language, fine-tuning
them to specific NLP tasks and then using inference and model
selection to run these models.

The course will focus on the following topics, with an emphasis on
efficient approaches that can be run without an expensive compute
budget:

1. Transformer models in NLP
1. Data Collection and Preprocessing
1. Model design choices
1. Pre-training (PLMs - pre-trained language models)
1. Fine-tuning PLMs
1. Inference
1. Model Selection

We will be reading papers on these topics and students will be
presenting the papers and leading the discussion in class in
collaboration with the instructor. The overall goal of the course
will be for each student to produce a project that focuses on
improving efficiency in one or more of these aspects of advanced
methods in NLP.

## Educational Goals

At the end of this course, the student should:

1. Understand advanced NLP models such as Transformers.
1. Be able to write code to implement such models.
1. Fine-tune an existing pre-trained language model for a particular
   NLP task or tasks.
1. Fine-tune an existing pre-trained language model with frozen
   parameters.
1. Write the inference code necessary to solve an NLP task.
1. Understand hyperparameter search.
1. Be able to modify the basic model architecture to improve the
   state-of-the-art in at least one of the topics covered in this
   course.

#### Instructor
* [Anoop Sarkar](http://anoopsarkar.github.io) 

#### Teaching Assistants
<ul>
{% for ta in site.tas %}
<li>{{ ta.name }}, <code>{{ ta.email }}</code>, Office hour: {{ ta.officehour }}.</li>
{% endfor %}
</ul>

#### Asking for help
* Use [ChatGPT](https://chat.openai.com) and [Codex](https://platform.openai.com/docs/guides/code)
* Ask for help on [the discussion board]({{ site.coursys }}/discussion)
* Instructor office hours: TBD
* <b>No emails</b> to the TAs and only emails that cannot go to discussion board can be sent to the instructor
* Use only SFU email address and use `cmpt419:` or `cmpt983:` (for ugrad and grad respectively) as subject prefix

#### Time and place
* Mon 10:30-12:20 [WMC 3210](http://www.sfu.ca/campuses/maps-and-directions/burnaby-map.html) 
* Wed 10:30-11:20 [WMC 3260](http://www.sfu.ca/campuses/maps-and-directions/burnaby-map.html)
* Last day of classes: {{ site.lastday }}

#### Calendar
* [Subscribe]({{ site.calendar }})

#### Textbook
* No required textbook. Online readings provided in Syllabus.

#### Grading
* Submit homework source code and check your grades on [Coursys]({{ site.coursys }})
* Programming setup homework: HW0 due on {{ site.hwdates[0].deadline }} (2%)
* Four programming homeworks. Due dates: HW1 on {{ site.hwdates[1].deadline }}, HW2 on {{ site.hwdates[2].deadline }}, HW3 on {{ site.hwdates[3].deadline }}, HW4 on {{ site.hwdates[4].deadline }} (12% each)
* Participation: Helping other students on the discussion board in a positive way (5%)
* In class presentation (5%)
* Final Project Proposal: Due on {{ site.hwdates[5].proposal }} (10%)
* Final Project: Due on {{ site.hwdates[5].deadline }} (30%)
* Final Project Poster Session:
    * Time: {{ site.hwdates[5].deadline }} {{ site.hwdates[5].time }}. 
    * Location: {{ site.hwdates[5].location }}
