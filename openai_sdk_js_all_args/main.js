import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
  organization: "organization",
  project: "project",
  baseURL: process.env['TEST_API_BASE_URL'] ?? 'http://127.0.0.1:4010',
  timeout: 10,
  httpAgent: undefined,
  fetch: undefined,
  maxRetries: 2,
  defaultHeaders: undefined,
  defaultQuery: undefined,
  dangerouslyAllowBrowser: true,
});

async function main() {
  const chatCompletion = await client.chat.completions.create({
      messages: [{ content: 'string', role: 'developer', name: 'name' }],
      model: 'gpt-4o',
      response_format: { type: 'text' },
      temperature: 1,
      audio: { format: 'wav', voice: 'alloy' },
      frequency_penalty: -2,
      function_call: 'none',
      functions: [{ name: 'name', description: 'description', parameters: { foo: 'bar' } }],
      logit_bias: { foo: 0 },
      logprobs: true,
      max_completion_tokens: 0,
      max_tokens: 0,
      metadata: { foo: 'string' },
      modalities: ['text'],
      n: 1,
      parallel_tool_calls: true,
      prediction: { content: 'string', type: 'content' },
      presence_penalty: -2,
      reasoning_effort: 'low',
      seed: 0,
      service_tier: 'auto',
      stop: 'string',
      store: true,
      stream: false,
      stream_options: { include_usage: true },
      tool_choice: 'none',
      tools: [
        {
          function: { name: 'name', description: 'description', parameters: { foo: 'bar' }, strict: true },
          type: 'function',
        },
      ],
      top_logprobs: 0,
      top_p: 1,
      user: 'user-1234',
  });
  console.log(chatCompletion.data.choices[0].message.content);
}

main();
