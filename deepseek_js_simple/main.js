import OpenAI from 'openai';

const client = new OpenAI({
  baseURL: 'https://api.deepseek.com',
});

async function main() {
  const chatCompletion = await client.chat.completions.create({
    messages: [{ role: 'user', content: 'Say this is a test' }],
    model: 'deepseek-chat',
  });
  console.log(chatCompletion.data.choices[0].message.content);
}

main();

export { client };
