import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.ChatModel;
import com.openai.models.chat.completions.ChatCompletion;
import com.openai.models.chat.completions.ChatCompletionCreateParams;

OpenAIClient client = OpenAIOkHttpClient.builder()
    .baseUrl("https://api.deepseek.com") // Custom base URL if needed
    .checkJacksonVersionCompatibility("checkJacksonVersionCompatibilityValue")
    .jsonMapper("jsonMapperValue")
    .streamHandlerExecutor("streamHandlerExecutorValue")
    .clock("clockValue")
    .headers("headersValue")
    .queryParams("queryParamsValue")
    .timeout("timeoutValue")
    .maxRetries("maxRetriesValue")
    .proxy("proxyValue")
    .responseValidation("responseValidationValue")
    .apiKey("apiKeyValue")
    .credential("credentialValue")
    .azureServiceVersion("azureServiceVersionValue")
    .organization("organizationValue")
    .project("projectValue")
    .fromEnv("fromEnvValue")
    .build();

ChatCompletionCreateParams params = ChatCompletionCreateParams.builder()
    // There's numerous ways to add messages
    .addUserMessage("Say this is a test")
    .addDeveloperMessage("This is a test")
    .addSystemMessage("This is a test")
    // Temperature is a double but it can also be a optional or in a JsonField
    .temperature(0.5)
    // Model is an enum but it can also be a Jsonfield or a regular string
    .model("deepseek-chat")
    // Everything else goes in the metadata
    .additionalBodyProperties("additionalBodyPropertiesValue")
    .additionalHeaders("additionalHeadersValue")
    .additionalQueryParams("additionalQueryParamsValue")
    .audio("audioValue")
    .frequencyPenalty("frequencyPenaltyValue")
    .functionCall("functionCallValue")
    .functions("functionsValue")
    .logitBias("logitBiasValue")
    .logprobs("logprobsValue")
    .maxCompletionTokens("maxCompletionTokensValue")
    .maxTokens("maxTokensValue")
    .metadata("metadataValue")
    .modalities("modalitiesValue")
    .n("nValue")
    .parallelToolCalls("parallelToolCallsValue")
    .prediction("predictionValue")
    .presencePenalty("presencePenaltyValue")
    .reasoningEffort("reasoningEffortValue")
    .removeAdditionalBodyProperty("removeAdditionalBodyPropertyValue")
    .removeAdditionalHeaders("removeAdditionalHeadersValue")
    .removeAdditionalQueryParams("removeAdditionalQueryParamsValue")
    .removeAllAdditionalBodyProperties("removeAllAdditionalBodyPropertiesValue")
    .removeAllAdditionalHeaders("removeAllAdditionalHeadersValue")
    .removeAllAdditionalQueryParams("removeAllAdditionalQueryParamsValue")
    .replaceAdditionalHeaders("replaceAdditionalHeadersValue")
    .replaceAdditionalQueryParams("replaceAdditionalQueryParamsValue")
    .replaceAllAdditionalHeaders("replaceAllAdditionalHeadersValue")
    .replaceAllAdditionalQueryParams("replaceAllAdditionalQueryParamsValue")
    .responseFormat("responseFormatValue")
    .seed("seedValue")
    .serviceTier("serviceTierValue")
    .stop("stopValue")
    .stopOfStrings("stopOfStringsValue")
    .store("storeValue")
    .streamOptions("streamOptionsValue")
    .toolChoice("toolChoiceValue")
    .tools("toolsValue")
    .topLogprobs("topLogprobsValue")
    .topP("topPValue")
    .user("userValue")
    .webSearchOptions("webSearchOptionsValue")
    .build();
ChatCompletion chatCompletion = client.chat().completions().create(params);
