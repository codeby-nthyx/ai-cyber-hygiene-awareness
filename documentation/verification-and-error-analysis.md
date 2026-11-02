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

| ID | Campaign claim | Source | Review result (2026-11-02) |
|---|---|---|---|
| V1 | Keep operating systems, browsers and apps updated; updates may include security fixes. | CERT-In, *Basic Cyber Hygiene*: https://www.cert-in.org.in/PDF/CSA_Booklet.pdf ; Microsoft, *Install Windows Updates*: https://support.microsoft.com/en-US/Windows/Deployment/Updates-Lifecycle/install-windows-updates | **Supported.** CERT-In explicitly recommends keeping software up-to-date. Microsoft documents installing updates through Windows Update. Keep the wording “updates can include security fixes”; do not imply every update is security-related. |
| V2 | Keep recoverable copies of important files and test restoration. | Microsoft, *Backup, restore, and recovery in Windows*: https://support.microsoft.com/en-us/windows/experience/backup-recovery/backup-restore-and-recovery-in-windows ; Apple, *Back up iPhone*: https://support.apple.com/en-in/guide/iphone/iph3ecf67d29/ios | **Supported.** Microsoft defines backup as creating copies and restore as retrieving data from a backup. Apple documents iCloud and computer backups. |
| V3 | Synchronisation may replicate deletions or unwanted changes. | Service-specific sync/version-history documentation required. | **Pending.** This depends on the provider and product. Keep it qualified (“may”) and do not name a specific cloud service until its own documentation is checked. |
| V4 | Review app permissions and grant only access needed for the feature. | Google, *Change app permissions on your Android phone*: https://support.google.com/android/answer/9431959?hl=en-en-16 | **Supported for Android.** Google documents reviewing and changing permissions by app or permission type. Menu names and controls vary by Android version and manufacturer. |
| V5 | Confirm public Wi-Fi details and avoid sensitive activity on untrusted public networks. | CERT-In Advisory CIAD-2016-0081: https://www.cert-in.org.in/s2cMainServlet?VLCODE=CIAD-2016-0081&pageid=PUBVLNOTES02 ; CERT-In Advisory CIAD-2020-0013: https://www.cert-in.org.in/s2cMainServlet?VLCODE=CIAD-2020-0013&pageid=PUBVLNOTES02 | **Supported.** CERT-In advises verifying the hotspot name with its owner and avoiding sensitive activity on public Wi-Fi. The advisory is older; retain general wording and avoid suggesting every public network is compromised. |
| V6 | HTTPS encrypts the connection but does not prove a website is legitimate. | CERT-In safe-browsing guidance: https://www.cert-in.org.in/s2cMainServlet?CACODE=CICA-2026-3492&pageid=PUBADV01 ; additional browser-security source recommended. | **Partly supported.** CERT-In recommends checking URLs and exercising caution with untrusted links. The distinction between transport encryption and website legitimacy should be supported with a dedicated browser/security source before final submission. Keep the caveat; do not describe the padlock as a trust guarantee. |
| V7 | A VPN does not make phishing sites safe or guarantee complete protection. | CERT-In Advisory CIAD-2020-0013: https://www.cert-in.org.in/s2cMainServlet?VLCODE=CIAD-2020-0013&pageid=PUBVLNOTES02 | **Partly supported.** CERT-In describes VPN use as one precaution for public Wi-Fi and separately warns about phishing. The conclusion that a VPN does not validate a website follows from those separate functions; add a dedicated VPN limitations source if this point is central to the final presentation. |

## Known error patterns to test
These are risks to check for during review, not a claim that a particular model actually produced them.

| Potential AI error | Why it is misleading | Correction |
|---|---|---|
| “HTTPS means the site is safe.” | Encryption does not establish the operator's honesty. | Say HTTPS encrypts the connection to the named domain; inspect the domain and context. |
| “Cloud sync is always a backup.” | Sync may replicate deletion or corruption, depending on the service. | Explain retention/version history and maintain a separate recoverable copy where appropriate. |
| “A VPN makes public Wi-Fi completely safe.” | A VPN does not validate a destination website or prevent every online threat. | Describe VPN protection narrowly and retain other precautions. |
| “Deny every app permission.” | Some permissions are required for chosen features. | Grant only permissions needed for the feature and review them. |
| “All updates should be installed from any alert.” | Fake update prompts can be malicious. | Use built-in settings or official publisher channels. |
| Invented percentage or fake source citation | Gives false authority to campaign content. | Remove unless independently supported by a traceable source. |

## Evidence log — checked sources

| Claim ID | Exact source page title | Date checked (YYYY-MM-DD) | Result | Reviewer note |
|---|---|---|---|---|
| V1 | Basic Cyber Hygiene (CERT-In); Install Windows Updates (Microsoft Support) | 2026-11-02 | Supported | CERT-In recommends updates; Microsoft shows Windows Update settings route. |
| V2 | Backup, restore, and recovery in Windows (Microsoft Support); Back up iPhone (Apple Support) | 2026-11-02 | Supported | Both describe backup/restore mechanisms. Service-specific behaviour still matters. |
| V3 | Not yet checked | — | Pending | Find documentation for the specific sync provider before making a provider-specific claim. |
| V4 | Change app permissions on your Android phone (Google Android Help) | 2026-11-02 | Supported | Applies to Android guidance; do not imply identical steps on iOS. |
| V5 | Advisory CIAD-2016-0081 and CIAD-2020-0013 (CERT-In) | 2026-11-02 | Supported | Older guidance, but directly supports network-name verification and caution with sensitive activity. |
| V6 | CurrentActivity / Safe Browsing guidance (CERT-In) | 2026-11-02 | Partly supported | Need a dedicated source explaining that HTTPS is not a legitimacy guarantee. |
| V7 | Advisory CIAD-2020-0013 (CERT-In) | 2026-11-02 | Partly supported | Add a dedicated VPN limitations source if retaining this as a prominent claim. |

## Final quality gate
- [ ] Every factual claim maps to a source.
- [ ] Source wording and scope were checked, not just the search snippet.
- [ ] No fabricated statistics, citations or quotations.
- [ ] Caveats remain present in every adapted format.
- [ ] No real personal or confidential data appears.
- [ ] Human reviewer approved the final assets.
