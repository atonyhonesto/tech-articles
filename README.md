<div align="center">

# 📰 Tech Articles by Tony Honesto

**Cloud, integration, data, AI and motorsports technology, written up on LinkedIn<br>and backed here with diagrams, takeaways and runnable code.**

![Articles](https://img.shields.io/badge/articles-142-0A66C2?style=flat-square)
![Deep dives](https://img.shields.io/badge/deep_dives-8-6f42c1?style=flat-square)
[![With code](https://img.shields.io/badge/articles_with_code-81-181717?style=flat-square&logo=github)](#-runnable-code)
[![LinkedIn](https://img.shields.io/badge/follow-LinkedIn-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/tony-honesto-4195023)

</div>

---

## ⭐ Start here: deep dives

Each deep dive turns an article into a one-page visual brief (architecture diagrams, comparison tables and the key arguments) with a link to the full piece and to code where it exists.

| | Article | What's on the page |
|:-:|---|---|
| 📺 | **[Three Stakeholders, One Proof of Concept](articles/2026-10-watch-session-tracker/README.md)**<br><sub>A real-time watch session tracker, built twice</sub> | The session state machine, the trade-off table, zero-deps vs Express + Zod · [💻 TypeScript ×2 + simulator](https://github.com/atonyhonesto/watch-session-tracker-lightweight) |
| 🏁 | **[AI/ML at Race Speed](articles/2026-05-ai-ml-at-race-speed/README.md)**<br><sub>Low-latency inference, confidence thresholds & fallback</sub> | The 25 ms pit-wall pipeline, dual-threshold gate, three-tier fallback · [💻 runnable Python](https://github.com/atonyhonesto/race-speed-inference) |
| 🔌 | **[A Local C# MCP Server for Parquet Data](articles/2026-06-csharp-mcp-server-for-parquet/README.md)**<br><sub>Plain-English questions over local data with Claude Code</sub> | Architecture and tool-call sequence · [💻 .NET 10 source](https://github.com/atonyhonesto/ParquetMCPServer) |
| 🏥 | **[Azure Logic Apps for HL7 ADT](articles/2026-02-logic-apps-hl7-adt/README.md)**<br><sub>Decoding hospital admission messages without parsers</sub> | Workflow diagram, HL7 → JSON walkthrough · [💻 Logic App workflow](https://github.com/atonyhonesto/logicapp-hl7-adt-a01-decoder) |
| 🔄 | **[Matillion and BizTalk](articles/2026-06-matillion-and-biztalk/README.md)**<br><sub>Two platforms, one purpose</sub> | Seven shared pillars, the 2030 modernization path · [💻 X12 850 → JSON → 997 in Python](https://github.com/atonyhonesto/edi-x12-mapper) · [📁 migration case study](https://github.com/atonyhonesto/biztalk-azure-modernization) |
| ❄️ | **[Snowflake and Databricks](articles/2026-06-snowflake-and-databricks/README.md)**<br><sub>Two platforms, one data universe</sub> | Where they converge, where they split, a "use both" architecture · [💻 medallion layers in SQL](https://github.com/atonyhonesto/article-labs/tree/main/labs/medallion-sql) |
| 📡 | **[SignalR vs .NET 10 Server-Sent Events](articles/2026-05-signalr-vs-dotnet10-sse/README.md)**<br><sub>Pick the lightest real-time tool that works</sub> | Six-gap comparison and a decision flowchart · [💻 both, side by side in .NET 10](https://github.com/atonyhonesto/signalr-vs-sse-dotnet10) |
| 💸 | **[The AI Coding Tax](articles/2026-05-ai-coding-tax/README.md)**<br><sub>Stop AI tools from quietly accumulating technical debt</sub> | Five flavours of AI debt and the review pipeline that catches them · [💻 measure it from git history](https://github.com/atonyhonesto/ai-coding-tax-analyzer) |

## 💻 Runnable code

81 of the articles link to code you can clone and run, every repo tested in CI on each push.

| Repo | What it is | Articles |
|---|---|---|
| **[article-labs](https://github.com/atonyhonesto/article-labs)** | 50 small, runnable labs, one per article idea: motorsports analytics, AI/ML, cloud and data, architecture, simulation | 65 |
| **[race-speed-inference](https://github.com/atonyhonesto/race-speed-inference)** | Latency budgets, confidence gate and fallback for a 25 ms pit-wall call | AI/ML at Race Speed |
| **[watch-session-tracker-lightweight](https://github.com/atonyhonesto/watch-session-tracker-lightweight)** · [express-zod](https://github.com/atonyhonesto/watch-session-tracker-express-zod) · [simulator](https://github.com/atonyhonesto/watch-session-event-simulator) | One real-time tracker built two ways, plus a load generator | Three Stakeholders, One Proof of Concept |
| **[signalr-vs-sse-dotnet10](https://github.com/atonyhonesto/signalr-vs-sse-dotnet10)** | The same live feed over .NET 10 Server-Sent Events and SignalR | SignalR vs SSE · Real-Time Applications with SignalR |
| **[csharp-fargate-stepfunctions](https://github.com/atonyhonesto/csharp-fargate-stepfunctions)** | A C# batch job on Fargate, retried by Step Functions on its exit code | Deploying a C# Console App to Fargate |
| **[race-data-redis-streams](https://github.com/atonyhonesto/race-data-redis-streams)** | Live timing over Redis Streams: consumer groups, claims, replay | Race Data Streaming with Redis |
| **[oauth2-pkce-jwt-walkthrough](https://github.com/atonyhonesto/oauth2-pkce-jwt-walkthrough)** | Authorization code + PKCE and JWT validation, plus nine attacks it stops | OAuth 2.0 · Microsoft Entra ID |
| **[nodejs-architecture-patterns](https://github.com/atonyhonesto/nodejs-architecture-patterns)** | One TypeScript API, layered and feature-based, with boundary tests | Three Node.js architecture articles |
| **[edi-x12-mapper](https://github.com/atonyhonesto/edi-x12-mapper)** | X12 850 → canonical JSON → 997 acknowledgment | Matillion and BizTalk · Integration Accounts |
| **[ai-coding-tax-analyzer](https://github.com/atonyhonesto/ai-coding-tax-analyzer)** | Rework, duplication and hotspots from git history | The AI Coding Tax |
| **[ParquetMCPServer](https://github.com/atonyhonesto/ParquetMCPServer)** | A .NET 10 MCP server for querying Parquet from Claude Code | A Local C# MCP Server for Parquet Data |
| **[logicapp-hl7-adt-a01-decoder](https://github.com/atonyhonesto/logicapp-hl7-adt-a01-decoder)** | Logic App Standard workflow decoding HL7 ADT^A01 | Azure Logic Apps for HL7 ADT |

## 📚 Every article, by theme

<!-- CATALOG:START -->
**142 articles**, newest first within each theme.

<details>
<summary><b>🏎️ Motorsports & Sports Technology</b> (23)</summary>

- [Python Machine Learning in Motorsports](https://www.linkedin.com/pulse/python-machine-learning-motorsports-tony-honesto-aqmmc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/tire-deg-pit-window)
- [AWS Lambda](https://www.linkedin.com/pulse/aws-lambda-tony-honesto-5risc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/lambda-race-events)
- [Amazon S3](https://www.linkedin.com/pulse/amazon-s3-tony-honesto-o8hmc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/s3-telemetry-lake)
- [Zebra Technologies MotionWorks RFID](https://www.linkedin.com/pulse/zebra-technologies-motionworks-rfid-tony-honesto-pa5mc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/rfid-player-tracking)
- [AI/ML at Race Speed — Low-Latency Inference, Confidence Thresholds & Fallback Logic](https://www.linkedin.com/pulse/aiml-race-speed-low-latency-inference-confidence-fallback-honesto-hwmbc/) · [📊 deep dive](articles/2026-05-ai-ml-at-race-speed/README.md) · [💻 code](https://github.com/atonyhonesto/race-speed-inference)
- [Machine Learning Approaches for Motorsports Competitive Advantage](https://www.linkedin.com/pulse/machine-learning-approaches-motorsports-competitive-tony-honesto-agstc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/lap-time-model-comparison)
- [Motorsports - Streaming Telemetry & Real-Time Performance](https://www.linkedin.com/pulse/motorsports-streaming-telemetry-real-time-tony-honesto-rfexc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/streaming-telemetry-windows)
- [Winning in NASCAR with AI/ML](https://www.linkedin.com/pulse/winning-nascar-aiml-tony-honesto-tkdvc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/pit-strategy-monte-carlo)
- [Motorsports competitive edge via AI use cases](https://www.linkedin.com/pulse/motorsports-competitive-edge-via-ai-use-cases-tony-honesto-d2j3c/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/pit-strategy-monte-carlo)
- [VAR Graphics in FIFA](https://www.linkedin.com/pulse/var-graphics-fifa-tony-honesto-yo01c/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/var-offside-homography)
- [Helmut Schmidt University - Vehicle Dynamics Certificate](https://www.linkedin.com/pulse/helmut-schmidt-university-vehicle-dynamics-tony-honesto-lanoc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/anti-dive-geometry)
- [MGU-H Removed from F1 Power Units in 2026](https://www.linkedin.com/pulse/mgu-h-removed-from-f1-power-units-2026-tony-honesto-oahtc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/ers-energy-budget)
- [Anti-Dive & Downwash Geometry in F1](https://www.linkedin.com/pulse/anti-dive-downwash-geometry-f1-tony-honesto-b5xlc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/anti-dive-geometry)
- [SaaS Is Quietly Reshaping the Motorsports Industry](https://www.linkedin.com/pulse/saas-quietly-reshaping-motorsports-industry-tony-honesto-y0m7c/)
- [Race Data Streaming with Redis](https://www.linkedin.com/pulse/race-data-streaming-redis-tony-honesto-c8dwc/) · [💻 code](https://github.com/atonyhonesto/race-data-redis-streams)
- [WinDarab](https://www.linkedin.com/pulse/windarab-tony-honesto-9myqc/)
- [ATLAS Data-Driven Race Strategy](https://www.linkedin.com/pulse/atlas-data-driven-race-strategy-tony-honesto-5s2gc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/stint-pace-analyzer)
- [F1 Lap Time Analyzer — Python, Streamlit & FastF1 in Action](https://www.linkedin.com/pulse/f1-lap-time-analyzer-python-streamlit-fastf1-action-tony-honesto-qlmgc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/stint-pace-analyzer)
- [ML Pipelines for Athlete Evaluation](https://www.linkedin.com/pulse/ml-pipelines-athlete-evaluation-tony-honesto-q1vsc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/athlete-evaluation-pipeline)
- [ML Pipelines Powering Dynamic Ticket Pricing](https://www.linkedin.com/pulse/ml-pipelines-powering-dynamic-ticket-pricing-tony-honesto-8kcrc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/dynamic-ticket-pricing)
- [Prime Vision + Next Gen Stats](https://www.linkedin.com/pulse/prime-vision-next-gen-stats-tony-honesto-7yt8c/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/fuel-burn-bar)
- [Amazon Prime Video: Burn Bar, Tech behind the display](https://www.linkedin.com/pulse/amazon-prime-video-burn-bar-tech-behind-display-tony-honesto-p6mgc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/fuel-burn-bar)
- [F1, AWS & Real-Time Storytelling](https://www.linkedin.com/pulse/f1-aws-real-time-storytelling-tony-honesto-v1eac/)

</details>

<details>
<summary><b>🤖 AI, Machine Learning & Agents</b> (48)</summary>

- [Agent Reach | Give your AI Agent Eyes to see the entire Internet](https://www.linkedin.com/pulse/agent-reach-give-your-ai-eyes-see-entire-internet-tony-honesto-vemkc/)
- [Local C# MCP Server for Parquet Data](https://www.linkedin.com/pulse/local-c-mcp-server-parquet-data-tony-honesto-wu7qf/) · [📊 deep dive](articles/2026-06-csharp-mcp-server-for-parquet/README.md) · [💻 code](https://github.com/atonyhonesto/ParquetMCPServer)
- [Claude Code MCPs](https://www.linkedin.com/pulse/claude-code-mcps-tony-honesto-v3loc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/mcp-server-stdio)
- [Grok 4.3](https://www.linkedin.com/pulse/grok-43-tony-honesto-oljdc/)
- [Claude Cowork on your Mobile device — Simple Automation](https://www.linkedin.com/pulse/claude-cowork-your-mobile-device-simple-automation-tony-honesto-lnpcc/)
- [ChatGPT vs Codex for a Product Requirement](https://www.linkedin.com/pulse/chatgpt-vs-codex-product-requirement-tony-honesto-rcgbc/)
- [Claude vs Claude Code vs Claude Cowork — What's the Difference](https://www.linkedin.com/pulse/claude-vs-code-cowork-whats-difference-tony-honesto-eki0f/)
- [Real-Time Video Processing with OpenCV (Python)](https://www.linkedin.com/pulse/real-time-video-processing-opencv-python-tony-honesto-bmgvc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/opencv-motion-insight)
- [Real-Time Video Insight with OpenCV + Python](https://www.linkedin.com/pulse/real-time-video-insight-opencv-python-tony-honesto-yrfic/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/opencv-motion-insight)
- [PyTorch for Predictive Analytics](https://www.linkedin.com/pulse/pytorch-predictive-analytics-tony-honesto-1z0lc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/pytorch-lap-time)
- [TensorFlow for Predictive Analytics & Strategy](https://www.linkedin.com/pulse/tensorflow-predictive-analytics-strategy-tony-honesto-6qt0c/)
- [MagicSchool AI](https://www.linkedin.com/pulse/magicschool-ai-tony-honesto-yhz8c/)
- [Leveraging AI-Powered Image Generation](https://www.linkedin.com/pulse/leveraging-ai-powered-image-generation-tony-honesto-zf31c/)
- [ChatGPT 5.1](https://www.linkedin.com/pulse/chatgpt-51-tony-honesto-ueh1c/)
- [Perplexity AI](https://www.linkedin.com/pulse/perplexity-ai-tony-honesto-5hqtc/)
- [Creating AI-Avatar Digital Twins - 2Wai](https://www.linkedin.com/pulse/creating-ai-avatar-digital-twins-2wai-tony-honesto-jmy6c/)
- [Vertex AI](https://www.linkedin.com/pulse/vertex-ai-tony-honesto-qs4fc/)
- [LLM: Gemini](https://www.linkedin.com/pulse/llm-gemini-tony-honesto-nytwc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/llm-provider-adapter)
- [Conversational ML](https://www.linkedin.com/pulse/conversational-ml-tony-honesto-rsycc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/intent-classifier)
- [Statistics: Causal Inference](https://www.linkedin.com/pulse/statistics-causal-inference-tony-honesto-6bkyc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/causal-inference-basics)
- [LangChain](https://www.linkedin.com/pulse/langchain-tony-honesto-gl8oc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/rag-retrieval-pipeline)
- [Physical AI](https://www.linkedin.com/pulse/physical-ai-tony-honesto-y27bc/)
- [ChatGPT Connectors](https://www.linkedin.com/pulse/chatgpt-connectors-tony-honesto-ceffc/)
- [ChatGPT + Slack](https://www.linkedin.com/pulse/chatgpt-slack-tony-honesto-jcmjc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/chat-webhook-bot)
- [ChatGPT Atlas](https://www.linkedin.com/pulse/chatgpt-atlas-tony-honesto-gc1fc/)
- [ChatGPT + Webex Webhooks](https://www.linkedin.com/pulse/chatgpt-webex-webhooks-tony-honesto-uh5tc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/chat-webhook-bot)
- [Gemma 2](https://www.linkedin.com/pulse/gemma-2-tony-honesto-iiegc/)
- [Why Most AI Projects Don't Deliver](https://www.linkedin.com/pulse/why-most-ai-projects-dont-deliver-tony-honesto-yuhac/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/ai-eval-harness)
- [ChatGPT + Open-Source Models](https://www.linkedin.com/pulse/chatgpt-open-source-models-tony-honesto-ngf1c/)
- [ChatGPT + Hugging Face Transformers](https://www.linkedin.com/pulse/chatgpt-hugging-face-transformers-tony-honesto-tohrc/)
- [ChatGPT + CUDA](https://www.linkedin.com/pulse/chatgpt-cuda-tony-honesto-e1zbc/)
- [ChatGPT and Augmented Reality](https://www.linkedin.com/pulse/chatgpt-augmented-reality-tony-honesto-0bs6c/)
- [PyTorch Reinforcement Learning](https://www.linkedin.com/pulse/pytorch-reinforcement-learning-tony-honesto-jh6ec/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/q-learning-pit-stops)
- [AI Performance Insights](https://www.linkedin.com/pulse/ai-performance-insights-tony-honesto-dbtuc/)
- [ML Pipeline Use Case](https://www.linkedin.com/pulse/ml-pipeline-tony-honesto-avk7c/)
- [ChatGPT Agents as "Research and Execution Assistants"](https://www.linkedin.com/pulse/chatgpt-agents-research-execution-assistants-tony-honesto-pc5yc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/agent-tool-loop)
- [GenAI Apps with Streamlit](https://www.linkedin.com/pulse/genai-apps-streamlit-tony-honesto-dwcoc/)
- [Forecasting with XGBoost](https://www.linkedin.com/pulse/forecasting-xgboost-tony-honesto-pdwmc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/gradient-boosting-forecast)
- [The Cosmopolitan's AI Rose SMS Chatbot](https://www.linkedin.com/pulse/cosmopolitans-ai-rose-sms-chatbot-tony-honesto-rxmec/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/intent-classifier)
- [ChatGPT + Databricks](https://www.linkedin.com/pulse/chatgpt-databricks-tony-honesto-x9yhc/)
- [Azure AI Foundry + Azure Functions + SignalR](https://www.linkedin.com/pulse/azure-ai-foundry-functions-signalr-tony-honesto-pmb6f/)
- [ChatGPT + Python](https://www.linkedin.com/pulse/chatgpt-python-tony-honesto-bjsac/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/llm-provider-adapter)
- [ChatGPT Codex](https://www.linkedin.com/pulse/chatgpt-codex-tony-honesto-dnhrc/)
- [Use Case: Agentic Workflow to Build a Stock Analysis & Reporting Agent](https://www.linkedin.com/pulse/use-case-agentic-workflow-build-stock-analysis-agent-tony-honesto-qetxc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/agent-tool-loop)
- [ChatGPT Agent Use Case: Presentation Builder](https://www.linkedin.com/pulse/chatgpt-agent-use-case-presentation-builder-tony-honesto-eqrnc/)
- [Generative AI Chatbots & Virtual Assistants](https://www.linkedin.com/pulse/generative-ai-chatbots-virtual-assistants-tony-honesto-0b0mc/)
- [Generative AI](https://www.linkedin.com/pulse/generative-ai-tony-honesto-q2c5c/)
- [Amazon Bedrock](https://www.linkedin.com/pulse/amazon-bedrock-tony-honesto-gxmpc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/llm-provider-adapter)

</details>

<details>
<summary><b>☁️ Cloud, Data & Integration</b> (24)</summary>

- [Pub/Sub | AWS AppSync](https://www.linkedin.com/pulse/pubsub-aws-appsync-tony-honesto-qy7cc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/pubsub-subscriptions)
- [Splunk AI Toolkit | Digital Twins](https://www.linkedin.com/pulse/splunk-ai-toolkit-digital-twins-tony-honesto-5o2fc/)
- [Deploying a C# Console Application to AWS Fargate](https://www.linkedin.com/pulse/deploying-c-console-application-aws-fargate-tony-honesto-yejac/) · [💻 code](https://github.com/atonyhonesto/csharp-fargate-stepfunctions)
- [Snowflake and Databricks — Two Platforms, One Data Universe](https://www.linkedin.com/pulse/snowflake-databricks-two-platforms-one-data-universe-tony-honesto-nzyic/) · [📊 deep dive](articles/2026-06-snowflake-and-databricks/README.md) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/medallion-sql)
- [Matillion and BizTalk — Two Platforms, One Purpose](https://www.linkedin.com/pulse/matillion-biztalk-two-platforms-one-purpose-tony-honesto-mfkcc/) · [📊 deep dive](articles/2026-06-matillion-and-biztalk/README.md) · [💻 code](https://github.com/atonyhonesto/edi-x12-mapper)
- [Amazon Kinesis Streams vs DynamoDB Streams](https://www.linkedin.com/pulse/amazon-kinesis-streams-vs-dynamodb-tony-honesto-ble7c/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/kinesis-vs-dynamodb-streams)
- [Leveraging Azure Logic Apps for HL7 ADT](https://www.linkedin.com/pulse/leveraging-azure-logic-apps-hl7-adt-tony-honesto-qa9ac/) · [📊 deep dive](articles/2026-02-logic-apps-hl7-adt/README.md) · [💻 code](https://github.com/atonyhonesto/logicapp-hl7-adt-a01-decoder)
- [Azure Databricks AI/BI Genie](https://www.linkedin.com/pulse/azure-databricks-aibi-genie-tony-honesto-bvric/)
- [Managing Huge Data Sets in SharePoint Online](https://www.linkedin.com/pulse/managing-huge-data-sets-sharepoint-online-tony-honesto-nazyc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/graph-api-paging)
- [Microsoft Integration Accounts now enhanced in Logic Apps](https://www.linkedin.com/pulse/microsoft-integration-accounts-now-enhanced-logic-apps-tony-honesto-zwucc/) · [💻 code](https://github.com/atonyhonesto/edi-x12-mapper)
- [SharePoint — More Than Just File Storage](https://www.linkedin.com/pulse/sharepoint-more-than-just-file-storage-tony-honesto-p2eic/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/graph-api-paging)
- [IFS assyst - Enterprise Service Delivery](https://www.linkedin.com/pulse/ifs-assyst-enterprise-service-delivery-tony-honesto-sncfc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/itsm-sla-engine)
- [KML Data Into Actionable Geospatial Insights](https://www.linkedin.com/pulse/kml-data-actionable-geospatial-insights-tony-honesto-bf14c/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/kml-track-analysis)
- [Microsoft Entra ID](https://www.linkedin.com/pulse/microsoft-entra-id-tony-honesto-srp8c/) · [💻 code](https://github.com/atonyhonesto/oauth2-pkce-jwt-walkthrough)
- [ITSM Platforms Are More Strategic Than Ever](https://www.linkedin.com/pulse/itsm-platforms-more-strategic-than-ever-tony-honesto-j8msc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/itsm-sla-engine)
- [Apache Kafka | Real-Time Event Streaming](https://www.linkedin.com/pulse/apache-kafka-real-time-event-streaming-tony-honesto-odsrc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/kafka-consumer-groups)
- [Hybrid-Cloud SaaS Platform with Terraform](https://www.linkedin.com/pulse/hybrid-cloud-saas-platform-terraform-tony-honesto-adfac/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/terraform-hybrid-cloud)
- [Twilio for Customer Engagement](https://www.linkedin.com/pulse/twilio-customer-engagement-tony-honesto-hevsc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/twilio-sms-webhook)
- [Google BigQuery](https://www.linkedin.com/pulse/google-bigquery-tony-honesto-w6fyc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/medallion-sql)
- [Geotab API Integration](https://www.linkedin.com/pulse/geotab-api-integration-tony-honesto-kzdac/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/geotab-feed-client)
- [Databricks APIs and AI Apps](https://www.linkedin.com/pulse/databricks-apis-ai-apps-tony-honesto-ooxgc/)
- [Powered Data Narratives Inside Grafana](https://www.linkedin.com/pulse/powered-data-narratives-inside-grafana-tony-honesto-yzq7c/)
- [User Journey Analytics with PySpark](https://www.linkedin.com/pulse/user-journey-analytics-pyspark-tony-honesto-ckqbc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/user-journey-funnel)
- [Parquet for Analytics & Feature Consumption](https://www.linkedin.com/pulse/parquet-analytics-feature-consumption-tony-honesto-oww7c/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/parquet-feature-store)

</details>

<details>
<summary><b>🧱 Software Architecture & Engineering Practice</b> (22)</summary>

- [Three Stakeholders, One Proof of Concept: Building a Real-Time Watch Session Tracker](https://www.linkedin.com/pulse/three-stakeholders-one-proof-concept-tony-honesto-rvkqc/) · [📊 deep dive](articles/2026-10-watch-session-tracker/README.md) · [💻 code](https://github.com/atonyhonesto/watch-session-tracker-lightweight)
- [SignalR vs .NET 10 Server-Sent Events - Real-Time Communication](https://www.linkedin.com/pulse/signalr-vs-net-10-server-sent-events-real-time-tony-honesto-ofigc/) · [📊 deep dive](articles/2026-05-signalr-vs-dotnet10-sse/README.md) · [💻 code](https://github.com/atonyhonesto/signalr-vs-sse-dotnet10)
- [The AI Coding Tax — Stop AI Tools From Quietly Accumulating Technical Debt](https://www.linkedin.com/pulse/ai-coding-tax-stop-tools-from-quietly-accumulating-debt-tony-honesto-ikagc/) · [📊 deep dive](articles/2026-05-ai-coding-tax/README.md) · [💻 code](https://github.com/atonyhonesto/ai-coding-tax-analyzer)
- [Node.js Applications with Feature-Based Architecture](https://www.linkedin.com/pulse/nodejs-applications-feature-based-architecture-tony-honesto-e38dc/) · [💻 code](https://github.com/atonyhonesto/nodejs-architecture-patterns)
- [Structuring Node.js Applications with Layered Architecture](https://www.linkedin.com/pulse/structuring-nodejs-applications-layered-architecture-tony-honesto-ewjmc/) · [💻 code](https://github.com/atonyhonesto/nodejs-architecture-patterns)
- [Node.js + TypeScript for Scalable Applications](https://www.linkedin.com/pulse/nodejs-typescript-scalable-applications-tony-honesto-n9phc/) · [💻 code](https://github.com/atonyhonesto/nodejs-architecture-patterns)
- [Enforcing Java Coding Standards with SONAR (SonarQube)](https://www.linkedin.com/pulse/enforcing-java-coding-standards-sonar-sonarqube-tony-honesto-ku4lc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/java-coding-standards)
- [XMPP — Real-Time, Federated Communication](https://www.linkedin.com/pulse/xmpp-real-time-federated-communication-tony-honesto-rdq1c/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/xmpp-routing)
- [Age of AI Scrapers - Robots.txt](https://www.linkedin.com/pulse/age-ai-scrapers-robotstxt-tony-honesto-m1h4c/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/robots-txt-audit)
- [OAuth 2.0 in Modern Applications](https://www.linkedin.com/pulse/oauth-20-modern-applications-tony-honesto-b3aec/) · [💻 code](https://github.com/atonyhonesto/oauth2-pkce-jwt-walkthrough)
- [gRPC Still Matters](https://www.linkedin.com/pulse/grpc-still-matters-tony-honesto-rdexc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/grpc-telemetry)
- [Real-Time Applications with SignalR](https://www.linkedin.com/pulse/real-time-applications-signair-tony-honesto-4celc/) · [💻 code](https://github.com/atonyhonesto/signalr-vs-sse-dotnet10)
- [Podman - Containerized Deployment & Secure DevOps Pipelines](https://www.linkedin.com/pulse/podman-containerized-deployment-secure-devops-tony-honesto-wfryc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/podman-container)
- [Tekton Scalable CI/CD for Modern DevOps](https://www.linkedin.com/pulse/tekton-scalable-cicd-modern-devops-tony-honesto-8vl0c/)
- [Windows Desktop Applications with WPF](https://www.linkedin.com/pulse/windows-desktop-applications-wpf-tony-honesto-h0kmc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/wpf-mvvm)
- [Spring Boot](https://www.linkedin.com/pulse/spring-boot-tony-honesto-ijwqc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/spring-boot-api)
- [Flutter](https://www.linkedin.com/pulse/flutter-tony-honesto-opbfc/)
- [Qt](https://www.linkedin.com/pulse/qt-tony-honesto-fdn6c/)
- [BrightScript for Roku](https://www.linkedin.com/pulse/brightscript-roku-tony-honesto-p60mf/)
- [Leveraging XP Practices](https://www.linkedin.com/pulse/leveraging-xp-practices-tony-honesto-fesyc/)
- [Python + QR Codes](https://www.linkedin.com/pulse/python-qr-codes-tony-honesto-98olc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/qr-codes)
- [Rapid Prototyping & Feature Scaffolding](https://www.linkedin.com/pulse/rapid-prototyping-feature-scaffolding-tony-honesto-uqtuc/)

</details>

<details>
<summary><b>🛠️ Simulation, Engineering Tools & Hardware</b> (25)</summary>

- [Elysia - Battery Management Software | Digital Twin Intelligence](https://www.linkedin.com/pulse/elysia-battery-management-software-digital-twin-tony-honesto-adm1c/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/battery-digital-twin)
- [Raspberry Pi AI Hat+ 2](https://www.linkedin.com/pulse/raspberry-pi-ai-hat-2-tony-honesto-pkvgc/)
- [3DEXPERIENCE](https://www.linkedin.com/pulse/3dexperience-tony-honesto-jlxic/)
- [MathWorks - MATLAB Onramp - Interactive Introduction](https://www.linkedin.com/pulse/matlab-onramp-free-interactive-introduction-tony-honesto-yg5pc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/python-vs-matlab)
- [Product Development with Autodesk Fusion 360](https://www.linkedin.com/pulse/product-development-autodesk-fusion-360-tony-honesto-qb7fc/)
- [Simulation & Visualization - Norxe P60 8K Projection](https://www.linkedin.com/pulse/norxe-p60-8k-projection-tony-honesto-gxf2c/)
- [NVIDIA GeForce RTX 4090 - 48k Image Rendering](https://www.linkedin.com/pulse/nvidia-geforce-rtx-4090-48k-image-rendering-tony-honesto-pi3lc/)
- [6-DOF HexaRev Simulator](https://www.linkedin.com/pulse/6-dof-hexarev-simulator-tony-honesto-irmuc/)
- [UniFi Device Bridge Switch](https://www.linkedin.com/pulse/unifi-device-bridge-switch-tony-honesto-hs0kc/)
- [UniFi SFP Wizard](https://www.linkedin.com/pulse/unifi-sfp-wizard-tony-honesto-jyumc/)
- [NETGEAR M4300](https://www.linkedin.com/pulse/netgear-m4300-tony-honesto-b3uic/)
- [Juniper SRX1500](https://www.linkedin.com/pulse/juniper-srx1500-tony-honesto-ohufc/)
- [Cisco Catalyst 8300 Series Edge Platform](https://www.linkedin.com/pulse/cisco-catalyst-8300-series-edge-platform-tony-honesto-104sc/)
- [Virtual Testing with MSC Adams](https://www.linkedin.com/pulse/virtual-testing-msc-adams-tony-honesto-wwq4c/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/quarter-car-virtual-testing)
- [AI-Enhanced On-Demand Packaging with Packsize](https://www.linkedin.com/pulse/ai-enhanced-on-demand-packaging-packsize-tony-honesto-d6qmc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/packaging-box-optimizer)
- [Functional Mock-up Interface](https://www.linkedin.com/pulse/functional-mock-up-interface-tony-honesto-6f81c/)
- [Dymola](https://www.linkedin.com/pulse/dymola-tony-honesto-85vrc/)
- [Starlink Receiver Saturation](https://www.linkedin.com/pulse/starlink-receiver-saturation-tony-honesto-vw1df/)
- [ROMER Absolute Arm](https://www.linkedin.com/pulse/romer-absolute-arm-tony-honesto-cr6ac/)
- [Speedify - Bonding Internet Connections](https://www.linkedin.com/pulse/speedify-bonding-internet-connections-tony-honesto-oflyc/)
- [AnyViewer](https://www.linkedin.com/pulse/anyviewer-tony-honesto-7flhc/)
- [Smart-City Ecosystem](https://www.linkedin.com/pulse/smart-city-ecosystem-tony-honesto-x99nc/)
- [Python vs MATLAB](https://www.linkedin.com/pulse/python-vs-matlab-tony-honesto-4bg9c/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/python-vs-matlab)
- [Real-Time Prototyping](https://www.linkedin.com/pulse/real-time-prototyping-tony-honesto-cdydc/)
- [MATLAB and Simulink](https://www.linkedin.com/pulse/matlab-simulink-tony-honesto-ltrfc/) · [💻 code](https://github.com/atonyhonesto/article-labs/tree/main/labs/quarter-car-virtual-testing)

</details>
<!-- CATALOG:END -->

## 🗂️ How this repo is organised

```text
articles/<yyyy-mm>-<slug>/README.md   one-page deep dive per featured article
articles.csv                          the full catalog: title, theme, LinkedIn link, code repo, deep dive
scripts/build_readme.py               regenerates the catalog section above from articles.csv
```

Code that goes with an article lives outside this repo so it can be cloned, tested and run on its own: small examples in [article-labs](https://github.com/atonyhonesto/article-labs), bigger ones in their own repositories. Each catalog entry links to its code.

---

<div align="center">
<sub>Written by <b>Tony Honesto</b> · Cloud & Integration Engineer · Carmel, Indiana<br>
<a href="https://github.com/atonyhonesto">GitHub</a> · <a href="https://www.linkedin.com/in/tony-honesto-4195023">LinkedIn</a></sub>
</div>
