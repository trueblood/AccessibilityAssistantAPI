from haystack.nodes import FARMReader
from gtts import gTTS
import os

class MachineLearning():
    def read_page(context, question):
        reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=False)
        data_dir = "data/"
        reader.train(data_dir=data_dir, train_filename="machinelearningdata.json", use_gpu=False, n_epochs=1, save_dir="my_model",)
        reader.save(directory="my_model")
        new_reader = FARMReader(model_name_or_path="my_model")
        new_reader.predict_on_texts(question,[context])
        from haystack import Pipeline, Document
        from haystack.utils import print_answers
        p = Pipeline()
        p.add_node(component=new_reader, name="Reader", inputs=["Query"])
        res = p.run(
            query=question, documents=[Document(content=context)]
        )
        text_answer = str(res.get('answers')[0])
        #print(text_answer)
        start_index = text_answer.index('=')
        end_index = text_answer.index('score')
        cleaned_answer = text_answer[start_index+1:end_index]
        return cleaned_answer

    def run_machine_learning(context, question):
        reader = FARMReader(model_name_or_path="distilbert-base-uncased-distilled-squad", use_gpu=True)
        #reader = FARMReader(model_name_or_path="monologg/koelectra-small-v2-distilled-korquad-384", use_gpu=False)
        data_dir = "data/"
        reader.train(data_dir=data_dir, train_filename="machinelearningdata.json", use_gpu=False, n_epochs=1, save_dir="my_model",)
        reader.save(directory="my_model")
        new_reader = FARMReader(model_name_or_path="my_model")
        new_reader.predict_on_texts(question,[context])
        from haystack import Pipeline, Document
        from haystack.utils import print_answers
        # reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2")
        p = Pipeline()
        p.add_node(component=new_reader, name="Reader", inputs=["Query"])
        res = p.run(
            query=question, documents=[Document(content=context)]
        )
        print_answers(res, details="medium", max_text_len=50000)    
        text_answer = str(res.get('answers')[0])         
        startindex = text_answer.index('=')
        endindex = text_answer.index('score')
        cleanedanswer = text_answer[startindex+1:endindex]   
        return cleanedanswer
