# Research Report: AI Cyber Hygiene Awareness Campaign for Students

**Project:** Capstone 15  
**Prepared by:** Nithyasri  
**Target audience:** Students aged 15–24, with emphasis on learners without a technical background

## 1. Executive summary
Everyday digital activity exposes students to risks that can often be reduced through a small set of repeatable habits. This campaign focuses on keeping software updated, maintaining recoverable backups, reviewing app permissions, using public Wi-Fi carefully and recognising unsafe browsing situations. AI can accelerate the production of accessible educational material, but it can also introduce inaccurate or overconfident claims. The project therefore uses AI for drafting and transformation—not as the final authority for security facts.

## 2. Problem statement
Cybersecurity advice is frequently presented in technical language or as disconnected warnings. Students need short, actionable guidance that fits common activities such as installing apps, using campus or café networks, storing coursework and browsing links shared in messages. A campaign should make the recommended action clear without implying that one setting or tool guarantees complete safety.

## 3. Objectives
- Translate authoritative cyber-hygiene guidance into plain language.
- Create consistent messages across multiple formats.
- Apply prompt engineering to constrain audience, scope, tone and evidence.
- Verify factual claims against official or reputable sources.
- Identify and correct misleading AI-generated statements.
- Demonstrate a reproducible content-generation workflow.

## 4. Scope and audience
The campaign is designed for students aged 15–24. It covers five behaviours:
1. Install operating-system, browser and app updates from trusted update mechanisms.
2. Keep more than one recoverable copy of important files, including a copy not continuously exposed to the same account or device.
3. Grant apps only the permissions needed for their functions and review them periodically.
4. Treat public Wi-Fi as an untrusted network; prefer HTTPS, avoid sensitive activity on networks you do not trust, and use a trusted VPN where appropriate.
5. Check the actual destination and context of links; HTTPS alone does not prove a site is legitimate.

This is general awareness education, not a penetration test, audit or incident-response service.

## 5. Research method
The research approach is a focused review of public guidance from national cyber-security agencies, consumer-protection bodies and platform vendors. Sources are used to establish the practical behaviour behind each message. AI-generated summaries are treated as secondary working notes. Before publication, each factual sentence should be mapped to a source and checked against the source's actual wording and scope.

### Source selection
Priority is given to:
- Government cyber-security guidance (CERT-In and CISA).
- Consumer-protection guidance (FTC).
- Official platform documentation for operating-system and app controls (Google, Apple and Microsoft).

## 6. Findings and recommended behaviours

### 6.1 Software updates
Updates can fix security vulnerabilities and improve software reliability. Students should enable automatic updates where appropriate and install updates through the device's built-in settings or the software publisher's official channel. Unexpected pop-ups or messages asking users to install an update through an unfamiliar link should be treated cautiously.

**Campaign message:** Update through trusted settings—not random links.

### 6.2 Backups
A backup is useful only if it can be recovered. Cloud synchronisation may mirror deletions or unwanted changes and should not automatically be treated as an independent backup. Keep important files in a suitable backup location, protect the account with strong authentication and periodically check that files can be restored. For critical data, maintain a separate copy that is not permanently exposed to the same device or account.

**Campaign message:** Save a second copy, keep it separate, and test recovery.

### 6.3 App permissions
Apps may request access to location, camera, microphone, contacts, photos or files. Permission should make sense for the feature being used. Students can review permissions in their device settings and remove access that is no longer needed. Menu names and available controls vary by operating-system version.

**Campaign message:** If an app does not need it, do not grant it automatically.

### 6.4 Public Wi-Fi
Public networks may be operated by parties the user does not know. Users should verify the network name with the venue, keep device software current, use secure websites and avoid entering sensitive information when the network or site cannot be trusted. A VPN can protect traffic between the device and VPN provider, but it does not make phishing sites safe or guarantee anonymity.

**Campaign message:** Public Wi-Fi is convenient, not automatically trustworthy.

### 6.5 Safe browsing
Students should inspect the domain name, be cautious with unexpected attachments and links, and navigate to important services using a known address or trusted app. HTTPS encrypts the connection to the site named in the address bar; it does not certify that the site itself is honest. Never enter credentials after following a suspicious message link.

**Campaign message:** Check the destination—not just the padlock.

## 7. How AI is used
AI supports:
- Research question generation and source-summary drafts.
- Plain-language rewriting for a student audience.
- Content adaptation into posts, quiz questions and a short video script.
- Consistency checks across campaign messages.
- Formatting structured tips into draft social copy using a local Python script.

AI does not decide whether a claim is true. A human reviewer checks the source, wording, caveats and suitability for the audience.

## 8. Limitations
- Platform settings change; instructions must be checked against the device's current version.
- General guidance cannot account for every institution's network or device policy.
- A short campaign cannot measure long-term behaviour change without follow-up.
- No audience survey or controlled experiment is reported in this repository.
- No measured campaign reach, engagement or learning gain is claimed.
- The local automation produces drafts only; it does not publish content.

## 9. Conclusion
A useful student cyber-hygiene campaign should prioritise simple actions, avoid absolute guarantees and cite trustworthy guidance. AI can make content production faster and more consistent, provided factual verification and editorial responsibility remain with a human.

## 10. References
1. CERT-In, official portal and cyber-hygiene advisories: https://www.cert-in.org.in/
2. CISA, Secure Our World: https://www.cisa.gov/secure-our-world
3. Federal Trade Commission, How to Use Public Wi-Fi Networks: https://consumer.ftc.gov/articles/how-use-public-wi-fi-networks
4. Google Android Help, Change app permissions: https://support.google.com/android/answer/9431959
5. Apple Support, How to back up your iPhone: https://support.apple.com/en-in/HT203977
6. Microsoft Support, Backup and restore in Windows: https://support.microsoft.com/windows

**Verification status:** These are the intended primary references for the campaign. Before final academic submission, open each source, record the exact page title and access date, and ensure the cited page supports the specific claim used.
