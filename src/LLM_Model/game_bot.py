from transformers import AutoTokenizer, pipeline
import torch

class GameBot:
    def __init__(self, model_path):
        self.model_name = model_path
        self.tokenizer = None
        self.pipeline = None
        self.terminators = None
        self.max_new_tokens = 1024
        self.temperature = 0.1
        self.do_sample = True
        self.top_p = 0.4
        self.top_k = 10
        self.num_beams = 4
        self.early_stopping = True

        self.setup_pipeline()


    def setup_pipeline(self):
        print('-' * 100)
        print(f"Initializing model from {self.model_name}")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, padding_sides='left')
        self.pipeline = pipeline("text-generation",
                                 model=self.model_name,
                                 tokenizer=self.tokenizer,
                                 model_kwargs = {"torch_dtype": torch.float16},
                                 device_map="auto")

        self.pipeline.tokenizer.pad_token_id = self.pipeline.model.config.eos_token_id

        self.terminators = [
            self.pipeline.tokenizer.eos_token_id,
            self.pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
        ]

        print(f"Model Loaded")
        print('-' * 100)