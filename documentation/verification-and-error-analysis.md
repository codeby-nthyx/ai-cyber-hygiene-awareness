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
| V3 | Synchronisation may replicate deletions or unwanted changes. | Microsoft Support, *Sync your computer's files and folders with OneDrive*: https://support.microsoft.com/en-us/onedrive/sync-your-computer-s-files-and-folders-with-onedrive | **Supported for OneDrive.** Microsoft explicitly says adding, changing or deleting a file in the synced OneDrive folder is reflected on the OneDrive website and vice versa. Do not generalise identical behaviour to every provider; service-specific retention and version-history features vary. |
| V4 | Review app permissions and grant only access needed for the feature. | Google, *Change app permissions on your Android phone*: https://support.google.com/android/answer/9431959?hl=en-en-16 | **Supported for Android.** Google documents reviewing and changing permissions by app or permission type. Menu names and controls vary by Android version and manufacturer. |
| V5 | Confirm public Wi-Fi details and avoid sensitive activity on untrusted public networks. | CERT-In Advisory CIAD-2016-0081: https://www.cert-in.org.in/s2cMainServlet?VLCODE=CIAD-2016-0081&pageid=PUBVLNOTES02 ; CERT-In Advisory CIAD-2020-0013: https://www.cert-in.org.in/s2cMainServlet?VLCODE=CIAD-2020-0013&pageid=PUBVLNOTES02 | **Supported.** CERT-In advises verifying the hotspot name with its owner and avoiding sensitive activity on public Wi-Fi. The advisory is older; retain general wording and avoid suggesting every public network is compromised. |
| V6 | HTTPS encrypts the connection but does not prove a website is legitimate. | UK Government, *How to spot a fake website*: https://stopthinkfraud.campaign.gov.uk/how-to-spot-fraud/how-to-spot-a-fake-website/ | **Supported.** The UK Government explicitly states that HTTPS/padlock does not guarantee a site is legitimate or reputable; it indicates that the connection is secure and information entered is encrypted. |
| V7 | A VPN does not make phishing sites safe or guarantee complete protection. | National Cyber Security Centre, Bahrain, *VPN Security & Risks*: https://www.ncsc.gov.bh/en/cyberwiser/individuals/safeguard/vpn.html ; CERT-In Advisory CIAD-2020-0013: https://www.cert-in.org.in/s2cMainServlet?VLCODE=CIAD-2020-0013&pageid=PUBVLNOTES02 | **Supported with careful wording.** Bahrain's NCSC states that VPNs do not provide virus or malware protection; CERT-In separately warns about phishing and recommends caution on public Wi-Fi. Say a VPN does not replace checking links, website addresses or downloads; do not claim it has no security value. |

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
| V3 | Sync your computer's files and folders with OneDrive (Microsoft Support) | 2026-11-02 | Supported for OneDrive | Microsoft confirms additions, changes and deletions sync both ways. Avoid provider-wide generalisation. |
| V4 | Change app permissions on your Android phone (Google Android Help) | 2026-11-02 | Supported | Applies to Android guidance; do not imply identical steps on iOS. |
| V5 | Advisory CIAD-2016-0081 and CIAD-2020-0013 (CERT-In) | 2026-11-02 | Supported | Older guidance, but directly supports network-name verification and caution with sensitive activity. |
| V6 | How to spot a fake website (UK Government, Stop! Think Fraud) | 2026-11-02 | Supported | Explicitly distinguishes encrypted connection from site legitimacy. |
| V7 | VPN Security & Risks (National Cyber Security Centre, Bahrain); Advisory CIAD-2020-0013 (CERT-In) | 2026-11-02 | Supported with careful wording | NCSC notes VPNs do not provide virus/malware protection; CERT-In separately covers phishing and public Wi-Fi precautions. |

## Final quality gate
- [ ] Every factual claim maps to a source.
- [ ] Source wording and scope were checked, not just the search snippet.
- [ ] No fabricated statistics, citations or quotations.
- [ ] Caveats remain present in every adapted format.
- [ ] No real personal or confidential data appears.
- [ ] Human reviewer approved the final assets.
