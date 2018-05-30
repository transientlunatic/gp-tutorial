A Gaussian Process Tutorial
===========================

This repository is intended to serve as a tutorial on the use of
Gaussian process regression techniques, principly for surrogate
modelling in astrophysics, but will also touch on other topics, such
as latent variable GP priors as it develops.

Right now this repository is very much a draft, and it's likely to
change quite a lot as it develops.

Contents
========

1. Introduction
2. Covariance Functions
3. Gaussian Process Regression
4. Surrogate modelling with GPR
5. Latent Variable GP Priors

Getting the Code
===================

The easiest way to get the code and information in this tutorial is to
clone this repository. You can do that by running
::
   git clone https://github.com/transientlunatic/gp-tutorial.git

in a terminal. Your mileage may vary if you're running a non-Unix
system, such as Windows.

Setting-up Your Python Environment
==================================

The code examples in this repository are provided as Jupyter
notebooks. If you want to play around with them yourself you'll need
to install the correct Python libraries. If you're running on a
machine which has the `pip` package manager for Python installed you
can have it install everything that you need by running `pip
install -r requirements.txt` in the top level of this repository.

I strongly recommend that you install the libraries in a virtual
environment on your machine.

Author
======

This tutorial is written by Daniel Williams, who is a postgraduate
researcher at the Institute for Gravitational Research at the
University of Glasgow.
