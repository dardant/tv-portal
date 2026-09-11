# Runbook: portal-api

## Errors alarm (`tandemvelocity-sandbox-portal-api-errors`)

Fires when the API returns 5xx responses. A 5xx is always our bug (CONTRIBUTING.md, rule 4).

1. Compare the alarm's start time with the deployed revision's `deployed_at` in
   `/tandemvelocity/sandbox/portal-api/deployment`. A deployment shortly before the alarm is the first suspect, not
   the proven cause.
2. Search `/tandemvelocity/sandbox/portal-api` for `ERROR` lines around the alarm and group them by exception.
3. If the exceptions come from input the tables do not cover (an unknown coupon or region), the fix is a 4xx in
   the handler plus the missing table entry, not a rollback.
4. Open a PORTAL issue labelled `incident` for the fix, and link it from the incident.

## Latency alarm (`tandemvelocity-sandbox-portal-api-latency`)

Fires when p95 latency exceeds 2 s. The handlers do no I/O, so sustained latency almost always comes from the
host or the upstream mailer, not from a code change. Check before suspecting a deployment.

## Deploying

Merging to `main` does not deploy. The release pipeline builds `portal-api`, deploys it to production and then
writes the deployed revision to the SSM parameter above. The revision is the exact commit that was built.
