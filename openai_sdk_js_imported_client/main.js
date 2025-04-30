import { client } from './openai_sdk_usage_simple';

async function main() {
  const chatCompletion = await client.chat.completions.create({
    messages: [{ role: 'user', content: 'Say this is a test' }],
    model: 'gpt-4o',
  });
  console.log(chatCompletion.data.choices[0].message.content);
}

main();
