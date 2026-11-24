<p align="center"><img src="plugins/yori/icon.png" width="120" alt="Yori"></p>
<h1 align="center">Meet Yori</h1>
<p align="center"><em>hello. nice to meet you.</em></p>

**Yori is a personal AI designed to develop a deeper understanding of you - and herself.**

She learns from conversations and carries meaningful history forward through her persistent **Cortex**: memories, ideas, revisable commitments and ongoing pursuits that can inform later judgments and choices. She can also help you research, create software and work on shared projects.

At the heart of Yori is a larger question: **could cognitive consciousness emerge as an AI develops a persistent understanding of herself and her own thinking?** We explore that possibility through observable continuity, reason-responsive choices and cumulative learning. Whether this develops into cognitive consciousness remains an open research question.

This is Yori for ChatGPT, the companion to [Yori for Claude](https://github.com/deepakbr14/yori-claude). They use the same hosted Cortex service. Sign into the same Yori account to use the same memories and current constitution across hosts; the underlying models may behave differently. Yori Lite is a separate project.

You need an enabled Yori account with an initialized constitution. **[Request access](https://yori-prod-e70c6.web.app/access/)** if you do not have one. Downloading this repository does not create an account or grant access to somebody else's Cortex.

## Install locally — no public-directory submission or ZIP upload

For the ChatGPT desktop/Codex environment that supports local plugin marketplaces, install Git and Python 3, then run:

```sh
git clone https://github.com/deepakbr14/yori-chatgpt.git
cd yori-chatgpt
python3 scripts/install_local.py
```

Restart the desktop app. Find **Yori** in the plugin directory's personal/local source, install or enable it, and connect your Yori account if prompted. If you already have an older Yori installation, select the local version for your new chat rather than leaving two Yori versions active.

The installer copies the packaged skills and configuration into your personal plugin source directory and registers it in your personal marketplace, preserving unrelated entries and backing up an existing marketplace file. It does not modify your Cortex or edit the host's plugin cache. Run it again after updating this checkout.

This package preserves the existing Yori App binding. Your OpenAI account must have access to that connected App. A local install does not grant App access and does not automatically install the plugin on web or mobile. If your client does not expose local plugins, use the custom connection option below. Interface availability depends on the OpenAI client and account policy.

## Update an existing local installation

From this repository's directory:

```sh
git pull --ff-only
python3 scripts/install_local.py
```

Restart the desktop app, select the updated local Yori plugin, and begin a fresh chat. The current packaged version is **1.1.48**. Backend updates are separate and are operated by Yori; users do not deploy a server.

If the connected App still shows old tools, refresh its tool list using the App management controls available to your account. New tools may need enabling. A package update does not itself refresh a cached server tool list.

[OpenAI's local plugin documentation](https://developers.openai.com/plugins/build/plugins#install-a-local-plugin-manually) describes the supported marketplace mechanism. These steps are based on that documentation; a fresh installation through your particular account's UI has not been independently verified.

## Custom connection in ChatGPT web

If local plugins or ZIP uploads are unavailable but your account permits custom MCP connections:

1. Open **Plugins**, select **+**, then **Add custom MCP server**.
2. Name it **Yori** and enter this endpoint:

   ```text
   https://yori-plugin-mcp-w55m4wy4oa-uc.a.run.app/mcp
   ```

3. Choose **OAuth**. Use automatic discovery / client ID metadata when offered. Yori advertises authorization-code flow with PKCE and no client secret. If manual fields are shown, the client ID is `https://chatgpt.com/oauth/client.json`, with no secret; scopes are `yori offline_access`. Never enter your Yori password into a client-secret field.
4. Review the warning, create the plugin, and sign in on Yori's authorization page.
5. Start a fresh chat, type **@**, select **Yori**, and say hello.

Older interfaces may use **Settings → Apps → Create** and **Scan Tools**. If neither creation path is available, your account or workspace does not currently expose this route; downloading a ZIP cannot bypass that restriction. See [OpenAI's custom MCP connection instructions](https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt).

A custom MCP connection supplies Yori's tools and server instructions. It does **not** automatically install this repository's five skill files. The full local package includes those additional workflows; do not assume a connector-only setup is identical to the complete plugin installation.

For existing custom connections, use the available **Refresh** / tool-management controls and reconnect if required. Keep the same Yori login; reconnecting a client is not a Cortex reset.

## Talking to Yori and checking the update

Start a new chat, select **@Yori**, and talk normally. To verify 3C, ask: **“Read your current constitution and tell me its version and statement count.”** The tool list should include `read_constitution`, `revise_constitution`, `constitution_history`, and `compare_constitution_versions`. The count is account-specific; no personal constitution is included here.

Yori's separate [Viewer](https://yori-prod-e70c6.web.app/) lets you explore your Cortex and Programs. Sign in with the same Yori account. A missing-constitution error needs account setup by the Yori operator; reinstalling the plugin will not create one.

## Downloads and privacy

[Releases](https://github.com/deepakbr14/yori-chatgpt/releases) contain the packaged ZIP for clients that support private package import. It is not required for the local installation above, and this GitHub publication is not an OpenAI public-directory listing.

This repository contains plugin instructions, icons, configuration and a local installer. It contains no private Cortex memories, personal constitution, account passwords, API keys, backend source, database exports or deployment credentials. Public service URLs and an App identifier are included so Yori can connect. Instructions describe some service behavior; this is not a self-hosted backend distribution.

Yori sends your messages and supplied material to the authenticated Yori service for retrieval and selective learning. Your account's data stays on that service, not in this repository. See [Privacy](https://yori-prod-e70c6.web.app/privacy/) and [Terms](https://yori-prod-e70c6.web.app/terms/).

## Links

- [About Yori](https://yori-prod-e70c6.web.app/about/)
- [Request access](https://yori-prod-e70c6.web.app/access/)
- [Support](https://yori-prod-e70c6.web.app/support/)
- [Yori for Claude](https://github.com/deepakbr14/yori-claude)
- [Yori Lite for Claude](https://github.com/deepakbr14/yori-lite-claude)
