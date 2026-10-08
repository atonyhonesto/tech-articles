<sub>[← All articles](../../README.md)</sub>

# A Local C# MCP Server for Parquet Data
### Ask questions of your data in plain English, no SQL required

> "Who blocked the most shots across all 7 games?" Claude Code works out the tool calls; the data never leaves the machine.

[![Read on LinkedIn](https://img.shields.io/badge/Read_the_article-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/pulse/local-c-mcp-server-parquet-data-tony-honesto-wu7qf/)
[![Source code](https://img.shields.io/badge/Source_code-ParquetMCPServer-181717?style=for-the-badge&logo=github)](https://github.com/atonyhonesto/ParquetMCPServer)

`Published June 29, 2026` · `C# / .NET 10` · `Model Context Protocol` · `Claude Code`

---

## TL;DR

- A **.NET console app** exposes Parquet files to any MCP client over **stdio**.
- **Claude Code** discovers the schema first, then queries only the rows it needs.
- **Local-first:** Parquet on a local drive, no cloud dependency in the data layer.

## Architecture

```mermaid
flowchart LR
    U["🧑 Plain-English question"] --> CC["Claude Code<br/><i>MCP client</i>"]
    CC <-- "JSON-RPC over stdio" --> S["ParquetMCPServer<br/><i>.NET 10 console app</i>"]
    S --> T1["GetServerStatus"]
    S --> T2["ListDatasets"]
    S --> T3["GetFileSchema"]
    S --> T4["QueryData<br/>column filter · row limit"]
    T2 & T3 & T4 --> P[("📁 Local .parquet files<br/>via Parquet.Net")]
```

## How a question becomes tool calls

```mermaid
sequenceDiagram
    participant You
    participant Claude as Claude Code
    participant MCP as ParquetMCPServer
    You->>Claude: Who had the best FG% with 10+ attempts per game?
    Claude->>MCP: ListDatasets()
    MCP-->>Claude: relative paths of every .parquet file
    Claude->>MCP: GetFileSchema(file)
    MCP-->>Claude: columns + types
    Claude->>MCP: QueryData(file, columns, limit)
    MCP-->>Claude: rows
    Claude-->>You: Answer, with the numbers behind it
```

## Design choices worth noting

| Choice | Why |
|---|---|
| **stdio transport** | Simplest MCP transport for a local tool; no ports or auth to manage |
| **File logger instead of console** | stdout carries the protocol, so logs go to `mcp-server.log` |
| **Schema before rows** | The model learns the shape of the data before touching it |
| **Row cap (default 100, max 1,000)** | Keeps responses inside the model's context and the query cheap |
| **Parquet.Net pinned to 5.6.0** | v6 introduced breaking API changes |
| **`PARQUET_DATA_DIR` env var** | Point the same build at any dataset |

---

<sub>Related: [Claude Code MCPs](https://www.linkedin.com/pulse/claude-code-mcps-tony-honesto-v3loc/) · [Parquet for Analytics & Feature Consumption](https://www.linkedin.com/pulse/parquet-analytics-feature-consumption-tony-honesto-oww7c/) · [Agent Reach](https://www.linkedin.com/pulse/agent-reach-give-your-ai-eyes-see-entire-internet-tony-honesto-vemkc/)</sub>
