Title: Running LLM on an M2 Macbook Air
Date: 2023-11-27 20:00
Category: Machine Learning
Tags: tips

I wanted to see if I could run an LLM on my personal Macbook Air.  I don't expect magic, but
thought it'd be interesting to play around with prompts and such without having to worry about
cloud costs or internet connections.

Instructions are mostly from [this blog](https://simonwillison.net/2023/Aug/1/llama-2-mac/), which
appears to be a bit out of date as of this writing.  The updated instructions on 
[Github](https://github.com/simonw/llm-llama-cpp/tree/main) did work.

```shell
brew install llm
llm install llm-llama-cpp
llm install llama-cpp-python
llm llama-cpp download-model \
  https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q2_K.gguf \
  --alias llama2-chat --alias l2c --llama2-chat
llm -m l2c 'Tell me a joke about a llama' --system 'You are very funny'
```

One troubleshooting tip:  adding `-o verbose 1` helped me realize what was wrong with the first
instructions I tried.

```shell
llm -m l2c 'Tell me a joke about a llama' -o verbose 1
```
