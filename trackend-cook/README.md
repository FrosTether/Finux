# Track's End Ticket Timer: finux.tech/cook

A kitchen screen for Track's End Railroad Restaurant. The cook snaps the printed ticket or talks it in, and the
dispatcher calls out loud what to lay down next. It reminds the cook to oil the flat-top and says whether each
item goes out on a plate, in a red basket or in a to-go box.

This folder is a Cloudflare Worker. It serves the page at `finux.tech/cook/` and passes the page's questions to
the Claude API, so the API key stays on Cloudflare and never reaches a phone.

## Put it live (one time)

1. In the Cloudflare dashboard, go to **Workers & Pages → Create → Import a repository** and pick
   `FrosTether/Finux`.
2. Set the production branch to `trackend-cook` and the root directory to `trackend-cook`. Leave the build command
   empty. The deploy command is `npx wrangler deploy`.
3. After the first deploy, open the Worker's **Settings → Variables and Secrets** and add:
   - `ANTHROPIC_API_KEY` as a **Secret**: your key from console.anthropic.com
   - `KITCHEN_CODE` as a **Secret** (optional, recommended): any code. Each phone asks for it once.
4. Open https://finux.tech/cook/. If your normal site loads instead of the app, the finux.tech DNS record needs to be
   proxied (orange cloud). The app also works at the Worker's `workers.dev` address, under `/cook/`.

From Termux instead of the dashboard: `npx wrangler deploy`, then `npx wrangler secret put ANTHROPIC_API_KEY`.

## Updating

Pushes to the `trackend-cook` branch redeploy automatically once the repository is connected.
`src/cook.html` is the whole page. It is the same page as the Claude artifact version and uses Claude through this
Worker when it isn't running inside Claude.
