# ProjectProposalTemplate
Repository for the project proposal

This repository contains a latex template for your proposal. To build the paper run `make`. In order to do so you will need to have latex installed. [Texlivefull](https://linuxconfig.org/how-to-install-latex-on-ubuntu-20-04-focal-fossa-linux) should be sufficient. 

For your convenience I've included a plotting script with matplotlib to demonstrate how to add a figure into a latex file.

There are a number of tex files to break up your submission. The main files for editing are

* paper.tex - Top level file, contains author names, and links other tex files together
* pitch.tex - First text file, a few sentence description of your project
* proposal.tex - Description of your project, details in the document itself
* timeline.tex - Week by week description of your plan to complete your project

Some helper tex files are also included

* annotations.tex - contains helpers for leaving comments such as `/TODO`
* paper.bib - source for bibtex. Contains many sample bibtex entries. These entries can be referenced with the `\cite{}` command.

/fig contains some files for generating figures, and storing the output of generated charts

* matplotlibexample.py - a python script which produces the sample chart fig/example.py. It uses matplotlib as a plotting tool, and will require a complete install of matplotlib to execute
* example.pdf - an example plot. Vector graphics such as .svg and .pdf work the best with LaTeX.
