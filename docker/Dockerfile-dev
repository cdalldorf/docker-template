# base image, latest as of 7/9/2025
FROM continuumio/miniconda3:25.3.1-1

# load in the environment.yml file
ADD ./docker/environment.yml /

# create the environmnt
RUN conda update -n base conda -y && conda env update