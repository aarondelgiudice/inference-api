import torch
from transformers import AutoTokenizer, AutoModel

from typing import List, Tuple

DEFAULT_MODEL = "bert-base-uncased"


def get_vector(text: str, model_name: str = None) -> List[float]:
    model_name = model_name or DEFAULT_MODEL
    tokenizer, model = load_model(model_name)

    inputs = tokenizer(
        text, return_tensors="pt", padding=True, truncation=True, max_length=512
    )

    with torch.no_grad():
        outputs = model(**inputs)

    embeddings = outputs.last_hidden_state.mean(dim=1).squeeze()
    return embeddings.tolist()


def load_model(
    model_name: str = DEFAULT_MODEL,
) -> Tuple[AutoTokenizer, AutoModel]:
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    return tokenizer, model
