from transformers import AutoTokenizer, BartForConditionalGeneration

model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")


def summarize_text(text_to_summarize):
    inputs = tokenizer([text_to_summarize], max_length=1024, return_tensors="pt")
    summary_ids = model.generate(
        inputs["input_ids"], num_beams=2, min_length=0, max_length=100
    )
    summarized_text = tokenizer.batch_decode(
        summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False
    )[0]
    return summarized_text
