# Verification and AI Error Analysis

## Verification protocol
For each published factual claim:
1. Identify the exact sentence in the asset.
2. Identify the official or reputable source that supports it.
3. Open the source and check that it supports the claim in context.
4. Record the page title, publisher, URL and date checked.
5. Narrow or remove claims that are not supported.
6. Check the final asset again after editing.

## Claim register

| ID | Campaign claim | Primary source to check | Review requirement |
|---|---|---|---|
| V1 | Software updates can include security fixes. | CERT-In; device/software vendor update guidance | Confirm source explains security updates; avoid implying every update is security-related. |
| V2 | Keep recoverable copies of important files. | Microsoft backup guidance; Apple backup guidance | Check service-specific restore behaviour. |
| V3 | Sync may replicate deletions or changes. | Relevant cloud provider's sync/version-history documentation | Verify for the actual service being discussed; do not generalise to every provider. |
| V4 | Review and limit app permissions. | Google Android Help; Apple privacy and permissions guidance | Menu paths vary by OS and version. |
| V5 | Confirm public Wi-Fi network details and use caution. | FTC public Wi-Fi guidance; CERT-In guidance | Avoid claims that all public Wi-Fi is compromised. |
| V6 | HTTPS does not prove a website is legitimate. | CISA / browser security education sources | Explain encryption separately from website trust. |
| V7 | A VPN does not make phishing sites safe. | Reputable VPN/security education guidance | Avoid claiming VPNs provide anonymity or complete protection. |

## Known error patterns to test
These are risks to check for during review, not a claim that a particular model actually produced them.

| Potential AI error | Why it is misleading | Correction |
|---|---|---|
| “HTTPS means the site is safe.” | Encryption does not establish the operator's honesty. | Say HTTPS encrypts the connection to the named domain; inspect the domain and context. |
| “Cloud sync is always a backup.” | Sync may replicate deletion or corruption, depending on the service. | Explain retention/version history and maintain a separate recoverable copy where appropriate. |
| “A VPN makes public Wi-Fi completely safe.” | VPNs do not prevent phishing, malicious downloads or unsafe account practices. | Describe VPN protection narrowly and retain other precautions. |
| “Deny every app permission.” | Some permissions are required for chosen features. | Grant only permissions needed for the feature and review them. |
| “All updates should be installed from any alert.” | Fake update prompts can be malicious. | Use built-in settings or official publisher channels. |
| Invented percentage or fake source citation | Gives false authority to campaign content. | Remove unless independently supported by a traceable source. |

## Evidence log — complete during final review
Do not mark a claim verified merely because an AI tool supplied a URL. Fill this table after opening the source.

| Claim ID | Exact source page title | Date checked (YYYY-MM-DD) | Supported / revise / remove | Reviewer note |
|---|---|---|---|---|
| V1 | Pending manual source check | Not recorded | Pending | |
| V2 | Pending manual source check | Not recorded | Pending | |
| V3 | Pending service-specific check | Not recorded | Pending | |
| V4 | Pending manual source check | Not recorded | Pending | |
| V5 | Pending manual source check | Not recorded | Pending | |
| V6 | Pending manual source check | Not recorded | Pending | |
| V7 | Pending manual source check | Not recorded | Pending | |

## Final quality gate
- [ ] Every factual claim maps to a source.
- [ ] Source wording and scope were checked, not just the search snippet.
- [ ] No fabricated statistics, citations or quotations.
- [ ] Caveats remain present in every adapted format.
- [ ] No real personal or confidential data appears.
- [ ] Human reviewer approved the final assets.
