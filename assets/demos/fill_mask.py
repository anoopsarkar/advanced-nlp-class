from transformers import AutoConfig, AutoTokenizer, RobertaForMaskedLM, pipeline
import torch

config = AutoConfig.from_pretrained('distilroberta-base')
tokenizer = AutoTokenizer.from_pretrained('distilroberta-base')
model = RobertaForMaskedLM.from_pretrained('distilroberta-base', config=config)

fill_mask = pipeline(
    "fill-mask",
    model=model,
    tokenizer=tokenizer
)

mask = fill_mask.tokenizer.mask_token

print(fill_mask(f"the {mask} had a heart attack."))
print(fill_mask(f"the capital of Cuba is {mask}."))
