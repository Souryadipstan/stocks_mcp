uv# 📈 Stocks MCP

**Stocks MCP** is a Python-based MCP (Modular Command Platform) server designed to provide various functionalities related to stock data and operations. The project is currently under active development.

> ⚠️ Current Version: `0.0.1`

---

## 🚀 Features

- Modular MCP server framework
- Extensible to support multiple stock-related functionalities
- Easy integration with MCP clients (e.g., Claude Desktop)

---

## 🛠 Installation

1. **Install `uv`**  
   Follow the instructions here: [uv Installation Guide](https://docs.astral.sh/uv/getting-started/installation/)  
2. Clone repository then `cd stocks_mcp`
3. **Install dependencies**  
   Run the following command in the project root:
   ```bash
   uv init
   uv venv
   source .venv/bin/activate
   uv pip install -r requirements.txt
   ```

## Usage with MCP Clients

To integrate Stocks MCP with a MCP client (for example, Claude Desktop), add the following configuration to your claude_desktop_config.json:

```
{"mcpServers" : {
    "stocks_mcp" : {
        "command" : "/Users/{user}/.local/bin/uv",
        "args" : [
            "--directory",
            "/path/to/stocks_mcp",
            "run",
            "main.py"
        ]
    }
  }
}
```