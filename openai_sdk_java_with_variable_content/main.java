import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.ChatModel;
import com.openai.models.chat.completions.ChatCompletion;
import com.openai.models.chat.completions.ChatCompletionCreateParams;

// Configures using the `OPENAI_API_KEY`, `OPENAI_ORG_ID` and `OPENAI_PROJECT_ID` environment variables
OpenAIClient client = OpenAIOkHttpClient.fromEnv();

final String constantContent = "This will always be the same";
String variableContent = "This might change";

ChatCompletionCreateParams params = ChatCompletionCreateParams.builder()
    .addUserMessage(constantContent + variableContent)
    .model(ChatModel.O3_MINI)
    .build();
ChatCompletion chatCompletion = client.chat().completions().create(params);
