// Minimal MCP server over stdio (JSON-RPC 2.0, newline-delimited).
// No dependencies, so the extension installs with nothing to download.

const PROTOCOL_VERSION = "2025-06-18";

function startServer({ name, version, tools }) {
  const byName = new Map(tools.map((t) => [t.name, t]));
  let buffer = "";

  function send(msg) {
    process.stdout.write(JSON.stringify(msg) + "\n");
  }

  async function handle(msg) {
    const { id, method, params } = msg;
    const isRequest = id !== undefined && id !== null;

    if (method === "initialize") {
      return send({
        jsonrpc: "2.0",
        id,
        result: {
          protocolVersion: params?.protocolVersion || PROTOCOL_VERSION,
          capabilities: { tools: {} },
          serverInfo: { name, version },
        },
      });
    }
    if (method === "ping") return send({ jsonrpc: "2.0", id, result: {} });
    if (method === "tools/list") {
      return send({
        jsonrpc: "2.0",
        id,
        result: {
          tools: tools.map(({ name, title, description, inputSchema, annotations }) => ({
            name,
            title,
            description,
            inputSchema,
            annotations,
          })),
        },
      });
    }
    if (method === "tools/call") {
      const tool = byName.get(params?.name);
      if (!tool) {
        return send({ jsonrpc: "2.0", id, error: { code: -32602, message: `Unknown tool: ${params?.name}` } });
      }
      let result;
      try {
        const out = await tool.handler(params.arguments || {});
        result = { content: [{ type: "text", text: JSON.stringify(out, null, 2) }], isError: false };
      } catch (err) {
        // Error messages never carry candidate data: see errors thrown in recruitee.js.
        result = { content: [{ type: "text", text: `Error: ${err.message}` }], isError: true };
      }
      return send({ jsonrpc: "2.0", id, result });
    }
    if (isRequest) {
      send({ jsonrpc: "2.0", id, error: { code: -32601, message: `Method not found: ${method}` } });
    }
    // Notifications (notifications/initialized, cancelled, ...) need no reply.
  }

  process.stdin.setEncoding("utf8");
  process.stdin.on("data", (chunk) => {
    buffer += chunk;
    let nl;
    while ((nl = buffer.indexOf("\n")) >= 0) {
      const line = buffer.slice(0, nl).trim();
      buffer = buffer.slice(nl + 1);
      if (!line) continue;
      let msg;
      try {
        msg = JSON.parse(line);
      } catch {
        send({ jsonrpc: "2.0", id: null, error: { code: -32700, message: "Parse error" } });
        continue;
      }
      handle(msg).catch((err) => {
        if (msg.id !== undefined) send({ jsonrpc: "2.0", id: msg.id, error: { code: -32603, message: err.message } });
      });
    }
  });
  process.stdin.on("end", () => process.exit(0));
}

module.exports = { startServer };
