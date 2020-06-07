# from src.dataset_reader import TweetReader
from sentiment_extraction.util import create_ser_folder
from allennlp.common import Params
import allennlp.commands.train as allentrain

#datasets
dataset_url = [".experiments/tweet_extraction/data/"]

#params
extraction_params = "sentiment_extraction/sentiment_extraction.json"


# training flags
extraction = True

if __name__ == "__main__":

    if extraction:
        # result = BotaiApi.train(dataset_url, extraction_params, True)
        # print(result.result)
        ser_file = create_ser_folder()

        params = Params.from_file(extraction_params)
        model = allentrain.train_model(params, ser_file)