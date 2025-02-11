# How to Run deepseek locally and access using python.

STEP 1:
Download the ollama from https://ollama.com/download

STEP 2: Pull the deepseek-r1 model container locally.

> ollama pull deepseek-r1:1.5b  ## you can change the model parameter size. Here, I am using deepseek-r1 model with 1.5 billions parameters

STEP 3:  run the deepseek model 

> ollama run deepseek-r1:1.5b

Step 4: curl command to inference deepseek:

STEP 5: check if deepseek contaner  running locally:

> ollama ps

NAME                ID              SIZE      PROCESSOR    UNTIL              
deepseek-r1:1.5b    a42b25d8c10a    2.1 GB    100% GPU     4 minutes from now 


STEP 6:  Stopping deepseek service locally:
> ollam stop deepseek-r1:1.5b


curl --location 'http://localhost:11434/api/chat' \
--header 'Content-Type: application/json' \
--data '{
    "model": "deepseek-r1:1.5b",
    "messages": [
        {
            "role": "user",
            "content": " write python code for adding two number"
        }
    ],
    "stream": false
}'


Response:

{
    "model": "deepseek-r1:1.5b",
    "created_at": "2025-02-10T06:25:47.390631Z",
    "message": {
        "role": "assistant",
        "content": "<think>\nOkay, I need to write a Python function to add two numbers. Let me think about how to approach this.\n\nFirst, I should consider the parameters the function will take. The most straightforward way is to have two arguments, let's call them num1 and num2.\n\nNext, I'll use the addition operator, which in Python is the '+' symbol. So the function can simply return the sum of these two numbers.\n\nI should also think about edge cases. What if the inputs are not integers? For example, if they're strings that represent numbers. But since the question doesn't specify handling such cases, maybe I'll just assume num1 and num2 are integers or floats.\n\nI'll name my function something clear, like add_numbers. It's descriptive enough. Inside the function, I'll define it as def add_numbers(num1, num2):.\n\nThen, inside the function body, return the sum: return num1 + num2.\n\nWait, but what if someone passes non-numeric types? Maybe using try-except blocks to handle cases where adding isn't possible. But again, since the question doesn't ask for that, I'll stick with basic addition.\n\nSo putting it all together, the function should be straightforward.\n</think>\n\nHere's a simple Python function to add two numbers:\n\n```python\ndef add_numbers(num1, num2):\n    return num1 + num2\n```\n\n### Explanation:\n- **Function Definition**: The function `add_numbers` takes two parameters: `num1` and `num2`.\n- **Return Statement**: It returns the sum of `num1` and `num2`.\n\nYou can call this function like:\n\n```python\nresult = add_numbers(3, 5)\nprint(result)  # Output: 8\n```\n\nThis function adds two numbers in a straightforward manner."
    },
    "done_reason": "stop",
    "done": true,
    "total_duration": 12843554250,
    "load_duration": 582903291,
    "prompt_eval_count": 13,
    "prompt_eval_duration": 888000000,
    "eval_count": 376,
    "eval_duration": 11370000000
}


