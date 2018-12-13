import pandas as pd
from pathlib import Path
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# This script uses wordcloud
# get it via: conda install -c conda-forge wordcloud
# The general setup is that you first run this script from within RM
# Afterwards you can run this with your IDE (e.g pyCharm). This is able to pick up the dumps


#
# These folders are pointing to a tmp folder for dumps and results
#
resultfolder = os.path.join(str(Path.home()), ".RapidMiner", "python_results")
dumppath = os.path.join(resultfolder, "data.pickle")


#
# Main function called from rapidminer.
#
# data: a pandas dataframe with 3 cols: topic, word, weight
# singleOutput: If True, we generate one big output file. If true we write #topics individual files.
# calledFromRM: In RapidMiner calledFromRM is always true. Just used in the first lines.
#
# writes: Files to the resultfolder path.
# returns: data to work again on it in RM.
#
def rm_main(data, singleOutput=False, calledFromRM=True):
    name = "Topic"
    if (calledFromRM is True):
        # do rm specific things
        if os.path.exists(resultfolder) is False:
            os.makedirs(resultfolder)
        data.to_pickle(dumppath)

    # convert dataframe into something wordcloud lib can use
    d = {}
    topics = []
    for topic, a, x in data.values:
        d[topic] = {}
        if topic not in topics:
            topics.append(topic)

    for topic, a, x in data.values:
        d[topic][a] = x

    row, col = __getRowAndColSetting__(len(topics))
    plt.subplots_adjust(hspace=0.1)
    # loop over the topics and create word clouds
    # if singleOutput is True, create one big clouds picture
    # otherwise create individual charts.
    for topic in topics:
        wordcloud = WordCloud(background_color="white")
        wordcloud.generate_from_frequencies(frequencies=d[topic])
        if singleOutput is True:
            plt.subplot(row, col, topic + 1)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.title("Topic_" + str(topic))
        plt.axis("off")
        if singleOutput is False:
            plt.savefig(resultfolder + "/" + name + "_" + str(topic) + ".png")


    if singleOutput is True:
        plt.axis("off")
        plt.savefig(resultfolder + "/" + name + "_Overview_" + str(len(topics)) + ".png", quality=100)

    return data


# short helper function to get the number of rows and cols for a subplot
# we always take 4 rows and then as many as needed cols.
def __getRowAndColSetting__(nTopics):
    row = 3
    if nTopics % 3 == 0:
        col = nTopics / 3
    else:
        col = nTopics / 3 + 1
    return row, col


if __name__ == "__main__":
    print("Starting Word Cloud script in batch mode")
    print("Reading last execution data from: ", dumppath)
    data = pd.read_pickle(dumppath)
    rm_main(data, calledFromRM=False, singleOutput=True)
