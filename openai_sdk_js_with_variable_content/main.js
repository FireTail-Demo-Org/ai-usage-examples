import OpenAI from 'openai';

const client = new OpenAI();

const foo = "foo";
var bar = "bar";

async function main() {
  const chatCompletion = await client.chat.completions.create({
    messages: [{ role: 'user', content: `This value will always be the same ${foo}, and this value varies: ${bar}` }],
    model: 'gpt-4o',
  });
  console.log(chatCompletion.data.choices[0].message.content);
}

main();
