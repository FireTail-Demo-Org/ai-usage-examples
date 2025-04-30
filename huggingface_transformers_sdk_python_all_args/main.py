from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

EXAMPLE_PROMPT = "Cats are better than dogs because"


def automodel_example() -> str:
    model_name = "facebook/opt-125m"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    inputs = tokenizer(EXAMPLE_PROMPT, return_tensors="pt")
    outputs = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=100,
        do_sample=True,
        temperature=0.9,
    )
    output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return output


def automodel_example_2() -> str:
    return AutoTokenizer.from_pretrained("facebook/opt-125m").decode(
        AutoModelForCausalLM.from_pretrained("facebook/opt-125m").generate(
            input_ids=AutoTokenizer.from_pretrained("facebook/opt-125m")(
                "Cats are better than dogs because", return_tensors="pt"
            )["input_ids"],
            attention_mask=AutoTokenizer.from_pretrained("facebook/opt-125m")(
                "Cats are better than dogs because", return_tensors="pt"
            )["attention_mask"],
            max_length=100,
            do_sample=True,
            temperature=0.9,
        )[0],
        skip_special_tokens=True,
    )


def pipeline_example() -> str:
    model_name = "facebook/opt-125m"
    pipe = pipeline("text-generation", model=model_name)
    output = pipe(EXAMPLE_PROMPT, max_length=50, do_sample=True, top_k=50, top_p=0.95, temperature=0.7)[0][
        "generated_text"
    ]
    return output


def pipeline_example_2() -> str:
    return pipeline("text-generation", model="facebook/opt-125m")(
        "Cats are better than dogs because", max_length=50, do_sample=True, top_k=50, top_p=0.95, temperature=0.7
    )[0]["generated_text"]


if __name__ == "__main__":
    for example in [
        automodel_example,
        automodel_example_2,
        pipeline_example,
        pipeline_example_2,
    ]:
        print(f"🤖 {example.__name__.replace('_',' ')}: {example()}")
