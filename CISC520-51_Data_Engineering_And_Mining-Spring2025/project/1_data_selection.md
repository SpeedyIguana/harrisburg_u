# Deliverale 1: Final Project Data Selection

Course: CISC 520-51-B-2025/Spring 2025
Student name: Akassh

## Data

For this project, I inted to use the following paper's data set. I orignnally, wanted to find my own dataset from the U.S. Gov sites, but a lot of them were simply agregates that only had close to 25 rows or they did not have enough attributes to gain something meaniningful out of them.

- [Accident Risk Prediction based on Heterogeneous Sparse Data: New Dataset and Insights](https://dl.acm.org/doi/pdf/10.1145/3347146.3359078)

I have a personal connection with this data set too, since I myself had a motorcycle crash last year, I would like to know if there are certain factors, other than some basic ones, to judge when we might see a general traffic accident.

### When was the data collected

Start: Feb 2016
End: March 2019

### Who collected the data

- Sobhan Moosavi
- Mohammad Hossein Samavatian
- Srinivasan Parthasarathy
- Radu Teodorescu
- Rajiv Ramnath

### For what purposes was the data initially collected

To predict traffic accident patterns.

### What is the context and content of the data, what dimensions/attributes does it describe

The source of the data is crowdsourced information from open map apps. The data simply shows when and where accidents happened, along with some attributes regarding weather and other traffic patterns. The dataset has 46 columns with the information I mentioned above. It does have spacial and temporal data. It also notes where the incedent occurred and the repurcussions of it, such as traffic jams.

### How big is your data, number of rows and columns?

The overall dataset size is around 3GB after I downloaded and unpacked it. It has 46 columns and around 7.73 million records.

### Discuss the quality of your data, how complete is it? Are there any known sources of errors or biases?

Orignally, I would be worried about duplicates and biases regarding any crowdsourced data. This can be due to human error in reporting or simply due to multiple reports of the same incident in question.

There is not a keen way for us to eliminate the human error part completely, but it shoud be within a margin of error.

Another bias this data source may also have is absent data. For example, in a small, sparsely populated town, people may not use phone map apps to navigate and simply may not report such incidents. This does not mean these incidents did not occur, but it does mean that the incidents were un-reported to this dataet. This does reduce some data points for inference or mining purposes.

## End Note

I really wanted a U.S. Gov dataset, but I found it hard to find something as extensive as this set. To be honest, I am not curious in following the same pattern of pulling my own dataset from the sources with 2025 onwards data.
