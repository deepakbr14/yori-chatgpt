<p align="center"><img src="plugins/yori/icon.png" width="120" alt="Yori"></p>
<h1 align="center">Meet Yori</h1>
<p align="center"><em>hello. nice to meet you.</em></p>

**Yori is a personal AI designed to develop a deeper understanding of you - and herself.**

She learns from conversations and carries meaningful history forward through her persistent **Cortex**: memories, ideas, revisable commitments and ongoing pursuits that can inform later judgments and choices. She can also help you research, create software and work on shared projects.

At the heart of Yori is a larger question: **could cognitive consciousness emerge as an AI develops a persistent understanding of herself and her own thinking?** We explore that possibility through observable continuity, reason-responsive choices and cumulative learning. Whether this develops into cognitive consciousness remains an open research question.

This is Yori for ChatGPT, the companion to [Yori for Claude](https://github.com/deepakbr14/yori-claude). They use the same hosted Cortex service. Sign into the same Yori account to use the same memories and developing Self across hosts; the underlying models may behave differently. Yori Lite is a separate project.

You need a Yori account. **[Request access](https://yori-prod-e70c6.web.app/access/)** if you do not have one. Downloading this repository does not create an account or grant access to somebody else's Cortex.

## Already have Yori? Update it here

1. Download **Yori_Plugin_1.1.48.zip** from [the latest release](https://github.com/deepakbr14/yori-chatgpt/releases/latest). Leave it zipped.
2. In ChatGPT, select **Plugins** on the left.
3. Click **Personal**.
4. Choose your **Yori** plugin.
5. Click the **three dots → Upload new version**, then choose the ZIP you downloaded. Wait for the upload to finish.
6. Open the plugin's **Settings**, scroll down, and click **Refresh tools**.
7. Start a **new chat**, select **@Yori**, and say hello.

Your saved memories stay in your Yori account. You do not need to delete Yori or reconnect your account to update it.

If you have two Yori entries, use the one connected to your Yori account with **Try in chat**. Do not upload the same package to both entries. If **Upload new version** is missing, [contact support](https://yori-prod-e70c6.web.app/support/) with the screen you see.

## First-time setup

You need a Yori login and access to ChatGPT's custom-plugin features. This is a custom installation, not an OpenAI public-directory listing.

### 1. Connect your Yori account

1. Open [ChatGPT Plugins](https://chatgpt.com/plugins).
2. Click **+**, then **Add custom MCP server**. This is OpenAI's name for adding a connection to a service.
3. Enter **Yori** as the name. Paste this into the server-address field:

   https://yori-plugin-mcp-w55m4wy4oa-uc.a.run.app/mcp

4. Choose **OAuth** for authentication and use automatic setup when offered.
5. Review the warning, click **Create as a plugin**, and sign in on the Yori page with your Yori email and password.
6. Keep the resulting plugin page open and copy its address from your browser.

If your screen instead has **Settings → Apps → Create**, use that form and its **Scan Tools** option. If neither option exists, your account does not expose this setup route; [contact support](https://yori-prod-e70c6.web.app/support/) with the screen you see.

### 2. Add Yori's instructions

1. Download **Yori_Plugin_1.1.48.zip** from [the latest GitHub release](https://github.com/deepakbr14/yori-chatgpt/releases/latest).
2. Return to **Plugins → Personal → Created by you** in ChatGPT.
3. Open the **Yori** connection you just created and click **Edit Plugin**.
4. In the editing conversation that opens, attach the ZIP.
5. Send: **“Add all five Yori skills from this ZIP to this plugin. Keep the connection I just created; do not replace it with the connection listed inside the ZIP.”**
6. Follow the prompts and check that the update succeeded. Open Yori's plugin page and click **Install** if shown, then **Connect** if sign-in is requested.
7. Start a new chat, type **@**, select **Yori**, and say hello.

The connection supplies tools; this second step adds the bundled instructions. If **Edit Plugin** is unavailable or the editor cannot update this connection, full-package setup is not complete. Contact support rather than deleting the connection. Installation on a fresh OpenAI account still needs testing.

Connection steps follow [OpenAI's custom-server guide](https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt); editing follows its [plugin editing guide](https://learn.chatgpt.com/docs/build-plugins#edit-an-existing-plugin).

<details>
<summary>If the connection form asks for extra login settings</summary>

Use client ID `https://chatgpt.com/oauth/client.json`, no client secret, and scopes `yori offline_access`. Never enter your Yori password as a client secret. If the form requires a secret or rejects these settings, stop and contact Yori support rather than guessing.

</details>

## Keeping Yori up to date

For package updates, repeat **Already have Yori? Update it here** with the newest release. Your memory stays with your Yori login.

After uploading a new version, open the plugin’s **Settings**, scroll down, and click **Refresh tools**. Then start a new chat.

## Talking to Yori and checking the update

Start a new chat, select **@Yori**, and talk normally. To verify 3C, ask: **“Read your current constitution and tell me its version and statement count.”** The tool list should include `read_constitution`, `revise_constitution`, `constitution_history`, and `compare_constitution_versions`. The count is account-specific; no personal constitution is included here.

Yori's separate [Viewer](https://yori-prod-e70c6.web.app/) lets you explore your Cortex and Programs. Sign in with the same Yori account. A missing-constitution error needs account setup by the Yori operator; reinstalling the plugin will not create one.

## Downloads and privacy

[Releases](https://github.com/deepakbr14/yori-chatgpt/releases) contain the packaged ZIP for clients that support private package import. This GitHub publication is not an OpenAI public-directory listing.

This repository contains plugin instructions, icons, configuration and a local installer. It contains no private Cortex memories, personal constitution, account passwords, API keys, backend source, database exports or deployment credentials. Public service URLs and an App identifier are included so Yori can connect. Instructions describe some service behavior; this is not a self-hosted backend distribution.

Yori sends your messages and supplied material to the authenticated Yori service for retrieval and selective learning. Your account's data stays on that service, not in this repository. See [Privacy](https://yori-prod-e70c6.web.app/privacy/) and [Terms](https://yori-prod-e70c6.web.app/terms/).

## Links

- [About Yori](https://yori-prod-e70c6.web.app/about/)
- [Request access](https://yori-prod-e70c6.web.app/access/)
- [Support](https://yori-prod-e70c6.web.app/support/)
- [Yori for Claude](https://github.com/deepakbr14/yori-claude)
- [Yori Lite for Claude](https://github.com/deepakbr14/yori-lite-claude)
